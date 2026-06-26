#!/usr/bin/env python3
"""
build-deck-inlined.py — Constrói um deck HTML único pronto pra publicar no g4os-pages.

Uso:
    python3 build-deck-inlined.py --slides ./templates --assets ./assets --out deck-inlined.html --title "Meu Deck" --index ./examples/index.html

O que faz:
1. Carrega o `style.css` (inlinado no parent + em cada slide)
2. Carrega cada slide `[0-9][0-9]-*.html`
3. Inline as imagens como data URI (PNG, JPG, SVG)
4. Inline vídeos como data URI (MP4)
5. Inline o `style.css` em cada slide também (srcdoc não herda)
6. Constrói o array `slides = [{file, html}]` no `index.html`
7. Monta os `<script type="application/json" id="slide-NN">` no `<head>`
8. Reescreve a lógica JS pra usar `getElementById` + `JSON.parse` (em vez de `iframe src`)

Saída: `deck-inlined.html` pronto pra `mcp__g4os-pages__publish_page(html=...)`
"""

import argparse
import base64
import json
import os
import re
import sys


def load_b64(path: str) -> str:
    """Carrega arquivo e retorna base64 string (sem prefixo data:)."""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def mime_for(path: str) -> str:
    ext = path.split(".")[-1].lower()
    return {
        "svg": "image/svg+xml",
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "gif": "image/gif",
        "webp": "image/webp",
        "mp4": "video/mp4",
    }.get(ext, "application/octet-stream")


def is_embedded_asset(path: str) -> bool:
    return path.lower().endswith((
        ".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp", ".mp4"
    ))


def inline_assets(html: str, slides_dir: str, assets_dir: str) -> str:
    """Substitui <img src="assets/X"> por data URI inline."""

    def sub(match):
        attr = match.group(1)  # "src" ou "poster"
        path = match.group(2)
        # Resolve caminho relativo ao slide
        if path.startswith("assets/"):
            full = os.path.join(slides_dir, path)
        elif path.startswith("/"):
            full = os.path.join(slides_dir, path.lstrip("/"))
        else:
            full = os.path.join(slides_dir, path)

        if not os.path.exists(full):
            # Tenta no assets_dir
            full2 = os.path.join(assets_dir, os.path.basename(path))
            if os.path.exists(full2):
                full = full2
            else:
                return match.group(0)  # mantém original

        if not is_embedded_asset(path):
            return match.group(0)

        mime = mime_for(path)
        b64 = load_b64(full)
        return f'{attr}="data:{mime};base64,{b64}"'

    # src e poster
    html = re.sub(r'(src)="([^"]+)"', sub, html)
    html = re.sub(r'(poster)="([^"]+)"', sub, html)
    return html


def inline_style(html: str, style_css: str) -> str:
    """Inline o style.css em cada slide (srcdoc não herda CSS do parent)."""
    if 'href="style.css"' in html:
        return html.replace(
            '<link rel="stylesheet" href="style.css" />',
            f'<style>\n{style_css}\n</style>'
        )
    # Insere no <head> se não tiver
    return re.sub(
        r'(<head[^>]*>)',
        r'\1\n<style>\n' + style_css + '\n</style>',
        html, count=1
    )


def build_slides_data(slides_dir: str, assets_dir: str, style_css: str) -> list:
    """Carrega cada slide, inlina assets e CSS."""
    data = []
    for name in sorted(os.listdir(slides_dir)):
        if not (name.startswith(tuple(f"{i:02d}" for i in range(100))) and name.endswith(".html")):
            continue
        path = os.path.join(slides_dir, name)
        with open(path) as f:
            html = f.read()
        html = inline_assets(html, slides_dir, assets_dir)
        html = inline_style(html, style_css)
        data.append((name, html))
    return data


def build_deck(slides: list, style_css: str, index_template: str, title: str) -> str:
    """Constrói o deck-inlined.html."""

    # Inline style.css no parent
    deck = index_template.replace(
        '<link rel="stylesheet" href="style.css" />',
        f'<style>\n{style_css}\n</style>'
    )

    # Substitui o array slides antigo por carregamento via getElementById
    new_slides_js = """const slides = [];
for (let i = 1; i <= __N__; i++) {
  const el = document.getElementById('slide-' + String(i).padStart(2, '0'));
  if (el) {
    try { slides.push(JSON.parse(el.textContent)); }
    catch(e) { console.error('Slide ' + i + ' parse error', e); }
  }
}""".replace("__N__", str(len(slides)))

    start_marker = "const slides = ["
    end_marker = "];"
    start_idx = deck.find(start_marker)
    end_idx = deck.find(end_marker, start_idx) + len(end_marker)
    if start_idx < 0 or end_idx <= start_idx:
        print(f"ERRO: array slides não encontrado no template", file=sys.stderr)
        sys.exit(1)
    deck = deck[:start_idx] + new_slides_js + deck[end_idx:]

    # Monta os <script type="application/json"> no head
    script_blocks = []
    for i, (name, html) in enumerate(slides, 1):
        payload = json.dumps({"file": name, "html": html}, ensure_ascii=False)
        # Escapa </script> pra não fechar a tag
        payload = payload.replace("</script>", "<\\/script>")
        script_blocks.append(
            f'<script type="application/json" id="slide-{i:02d}">{payload}</script>'
        )
    slides_data = "\n".join(script_blocks)

    # Insere antes do </head>
    slide_data_block = f"\n<!-- Slides inlined -->\n{slides_data}\n"
    deck = deck.replace("</head>", slide_data_block + "</head>", 1)

    # Substitui o template de cards (template literal) por DOM manipulation
    old_cards_block = """  slides.forEach(s => {
    const a = document.createElement('a');
    a.className = 'card';
    a.href = s.file;
    a.innerHTML = `
      <div class="frame">
        <iframe src="${s.file}" scrolling="no"></iframe>
      </div>
      <div class="info">
        <span class="num">${String(s.n).padStart(2,'0')}</span>
        <span class="name">${s.name}</span>
        <span class="open">Abrir ↗</span>
      </div>`;
    grid.appendChild(a);
  });"""

    new_cards_block = """  slides.forEach(s => {
    const a = document.createElement('a'); a.className = 'card'; a.href = '#' + s.file;
    a.addEventListener('click', (e) => { e.preventDefault(); loadFromCard(s); });
    const frame = document.createElement('div'); frame.className = 'frame';
    const ifr = document.createElement('iframe');
    ifr.setAttribute('srcdoc', s.html); ifr.setAttribute('scrolling', 'no');
    frame.appendChild(ifr); a.appendChild(frame);
    const info = document.createElement('div'); info.className = 'info';
    const num = document.createElement('span'); num.className = 'num';
    num.textContent = s.file.replace(/^[0-9]+-/, '').replace(/\\.html$/, '').split('-')[0];
    info.appendChild(num);
    const name = document.createElement('span'); name.className = 'name';
    name.textContent = s.file.replace(/^[0-9]+-/, '').replace(/\\.html$/, '').replace(/-/g, ' ').trim();
    info.appendChild(name);
    const open = document.createElement('span'); open.className = 'open'; open.textContent = 'Abrir ↗';
    info.appendChild(open); a.appendChild(info);
    grid.appendChild(a);
  });"""
    if old_cards_block in deck:
        deck = deck.replace(old_cards_block, new_cards_block)

    # Reescreve a função load pra usar srcdoc em vez de src
    old_load = """  function load(i){
    idx = (i + slides.length) % slides.length;
    frame.src = slides[idx].file;
    counter.innerHTML = `<b>${String(idx+1).padStart(2,'0')}</b> / ${slides.length}`;
  }"""
    new_load = """  function load(i){
    idx = (i + slides.length) % slides.length;
    frame.setAttribute('srcdoc', slides[idx].html);
    counter.innerHTML = `<b>${String(idx+1).padStart(2,'0')}</b> / ${slides.length}`;
    setTimeout(fitPresent, 100);
  }
  function loadFromCard(s){
    const i = slides.findIndex(x => x.file === s.file);
    if (i >= 0) load(i);
  }"""
    deck = deck.replace(old_load, new_load)
    deck = deck.replace("frame.src=''", "frame.setAttribute('srcdoc', '')")

    # Centraliza o frame no modo apresentação
    old_fit = """  function fitPresent(){
    const s = Math.min(window.innerWidth / 1600, window.innerHeight / 900);
    frame.style.transform = `scale(${s})`;
  }"""
    new_fit = """  function fitPresent(){
    const s = Math.min(window.innerWidth / 1600, window.innerHeight / 900);
    frame.style.position = 'absolute'; frame.style.top = '50%'; frame.style.left = '50%';
    frame.style.transform = `translate(-50%, -50%) scale(${s})`;
  }"""
    deck = deck.replace(old_fit, new_fit)

    # Adiciona transform-origin no .present iframe
    old_css = """  .present iframe {
    width: 1600px; height: 900px;
    border: 0;
    flex-shrink: 0;
  }"""
    new_css = """  .present iframe {
    width: 1600px; height: 900px;
    border: 0;
    flex-shrink: 0;
    transform-origin: center center;
  }"""
    deck = deck.replace(old_css, new_css)

    # Atualiza o título
    deck = re.sub(r"<title>[^<]+</title>", f"<title>{title}</title>", deck, count=1)

    return deck


def main():
    ap = argparse.ArgumentParser(description="Build deck-inlined.html")
    ap.add_argument("--slides", default="./templates", help="Pasta com os slides [0-9][0-9]-*.html")
    ap.add_argument("--assets", default="./assets", help="Pasta com assets base")
    ap.add_argument("--index", default="./examples/index.html", help="Template do passador (index.html)")
    ap.add_argument("--style", default=None, help="Caminho do style.css (default: <slides>/style.css)")
    ap.add_argument("--out", default="deck-inlined.html", help="Arquivo de saída")
    ap.add_argument("--title", default="G4 Slides", help="Título do deck")
    args = ap.parse_args()

    style_path = args.style or os.path.join(args.slides, "style.css")
    if not os.path.exists(style_path):
        print(f"ERRO: style.css não encontrado em {style_path}", file=sys.stderr)
        sys.exit(1)
    with open(style_path) as f:
        style_css = f.read()
    with open(args.index) as f:
        index_template = f.read()

    print(f"Carregando slides de {args.slides}...")
    slides = build_slides_data(args.slides, args.assets, style_css)
    print(f"  {len(slides)} slides carregados")

    print(f"Inlinando assets de {args.assets}...")
    print(f"Buildando deck com título '{args.title}'...")
    deck = build_deck(slides, style_css, index_template, args.title)

    with open(args.out, "w") as f:
        f.write(deck)
    size_mb = os.path.getsize(args.out) / 1024 / 1024
    print(f"OK: {args.out} ({size_mb:.1f}MB)")


if __name__ == "__main__":
    main()
