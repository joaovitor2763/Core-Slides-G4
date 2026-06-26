# Publicar no g4os-pages

> Como publicar um deck de slides HTML no `https://sites.g4oscloud.com/s/<slug>/` com tudo inline (imagens, vídeo, CSS, dados).

## TL;DR

```bash
# 1. Build do "deck-inlined" (todos os slides inlinados num único HTML)
python3 build-deck-inlined.py

# 2. Publicar (≤5MB por arquivo)
mcp__g4os-pages__publish_page(
  slug="aula-ia-ge",
  title="G4 Gestão e Estratégia",
  html=<conteúdo de deck-inlined.html>
)
# → https://sites.g4oscloud.com/s/aula-ia-ge/

# 3. Pra atualizar
mcp__g4os-pages__republish_page(
  slug="aula-ia-ge",
  html=<conteúdo de deck-inlined.html>
)
# NÃO use publish_page pra atualizar — vai incrementar slug (aula-ia-ge-2)
```

## Por que **inline tudo** num único HTML?

O g4os-pages é um host de páginas HTML estáticas simples:
- Recebe **1 arquivo HTML por página** (o `index.html` da página)
- **Sem** suporte multi-file, **sem** servidor HTTP
- Limite: **5MB por arquivo**

Pra um deck de 29 slides com imagens e vídeo:
- Multi-file via `files` array → bug conhecido (schema retorna "received object" em array)
- Referências `src="assets/X.png"` → não funcionam (path relativo não é resolvido)
- CSS em arquivo separado `<link href="style.css">` → não carrega em iframe via srcdoc

Solução: cada slide vira um `<script type="application/json" id="slide-NN">{file, html}</script>` no head. Imagens e vídeo viram data URIs. CSS fica inline em cada slide também.

## Estratégia "deck-inlined"

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <title>Meu Deck</title>
  <link href="https://fonts.googleapis.com/css2?family=..." rel="stylesheet" />
  <style>
    /* style.css inline */
    :root { --bg: #F5F4F3; --fg: #0F1419; --accent: #B9915B; /* ... */ }
    .slide { /* canvas fixo 1600x900 */ }
  </style>

  <!-- Slides inlinados como JSON -->
  <script type="application/json" id="slide-01">
    {"file": "01-capa.html", "html": "<!doctype html>...com style.css inline...com imagens data: URI..."}
  </script>
  <script type="application/json" id="slide-02">...</script>
  <!-- ... -->
</head>
<body>
  <!-- Passador -->
  <div class="grid" id="grid"></div>
  <button class="present-btn" id="presentBtn">▶ Apresentar do 1º</button>
  <div class="present" id="present">
    <iframe id="presentFrame" src=""></iframe>
  </div>
  <nav class="hud">
    <button id="prevBtn">← Anterior</button>
    <span class="counter" id="counter"><b>01</b> / 29</span>
    <button id="nextBtn">Próximo →</button>
    <button id="closeBtn">Fechar (Esc)</button>
  </nav>

  <script>
    // Carrega slides via getElementById + JSON.parse
    const slides = [];
    for (let i = 1; i <= 29; i++) {
      const el = document.getElementById('slide-' + String(i).padStart(2, '0'));
      if (el) {
        try { slides.push(JSON.parse(el.textContent)); }
        catch(e) { console.error('Slide ' + i + ' parse error', e); }
      }
    }

    // Monta cards via DOM (não template literal — evita quebra com aspas)
    const grid = document.getElementById('grid');
    slides.forEach(s => {
      const a = document.createElement('a');
      a.className = 'card';
      a.href = '#' + s.file;
      a.addEventListener('click', (e) => { e.preventDefault(); loadFromCard(s); });
      const frame = document.createElement('div');
      frame.className = 'frame';
      const ifr = document.createElement('iframe');
      ifr.setAttribute('srcdoc', s.html);  // setAttribute lida com escape
      ifr.setAttribute('scrolling', 'no');
      frame.appendChild(ifr);
      a.appendChild(frame);
      // ... info, name, open
      grid.appendChild(a);
    });

    // Apresentação
    const present = document.getElementById('present');
    const frame = document.getElementById('presentFrame');
    let idx = 0;
    function load(i){
      idx = (i + slides.length) % slides.length;
      frame.setAttribute('srcdoc', slides[idx].html);
      counter.innerHTML = `<b>${String(idx+1).padStart(2,'0')}</b> / ${slides.length}`;
      setTimeout(fitPresent, 100);
    }
    function loadFromCard(s){
      const i = slides.findIndex(x => x.file === s.file);
      if (i >= 0) load(i);
    }
    function fitPresent(){
      const s = Math.min(window.innerWidth / 1600, window.innerHeight / 900);
      frame.style.position = 'absolute';
      frame.style.top = '50%'; frame.style.left = '50%';
      frame.style.transform = `translate(-50%, -50%) scale(${s})`;
    }

    // Bind controles
    document.getElementById('presentBtn').onclick = () => { load(0); document.body.classList.add('presenting'); fitPresent(); };
    document.getElementById('nextBtn').onclick = () => load(idx+1);
    document.getElementById('prevBtn').onclick = () => load(idx-1);
    document.getElementById('closeBtn').onclick = () => { document.body.classList.remove('presenting'); frame.setAttribute('srcdoc', ''); };
    document.addEventListener('keydown', (e) => {
      if (!document.body.classList.contains('presenting')) return;
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') load(idx+1);
      if (e.key === 'ArrowLeft' || e.key === 'Backspace') load(idx-1);
      if (e.key === 'Escape') { document.body.classList.remove('presenting'); frame.setAttribute('srcdoc', ''); }
    });
  </script>
</body>
</html>
```

## Bugs comuns

| Bug | Causa | Fix |
|---|---|---|
| `files: [...]` retorna "received object" | Schema MCP com bug | Use `html` string única com tudo inline |
| `files` aceita `< 100 chars` | Limite ridículo no schema | Mesma solução |
| `html` com 30MB retorna "limit 5MB" | Limite hard do g4os-pages | Comprima imagens, comprima vídeo, remova audio |
| Slide fica sem CSS no srcdoc | iframe não herda CSS do parent | Inline `style.css` em cada slide também |
| Aspas no `srcdoc="${s.html}"` quebram atributo | Template literal JS não escapa | Use `ifr.setAttribute('srcdoc', s.html)` |
| Vídeo MP4 não carrega | Muitos MB | Comprima com ffmpeg (veja EXPORT-PDF.md) |
| Imagens sumindo após publicação | Path relativo `src="assets/X.png"` | Use data URI inline |

## URL final

```
https://sites.g4oscloud.com/s/aula-ia-ge/
```

- `noindex` por padrão (não aparece em Google)
- Slug fixo: `aula-ia-ge` (ou outro que você escolher)
- Pra atualizar: `republish_page` com mesmo slug (NÃO `publish_page` — vai criar `aula-ia-ge-2`)
- Para despublicar: `unpublish_page(slug="aula-ia-ge", confirm=true)`

## Tamanho esperado

- Deck 29 slides light: ~1.5-2.5MB
- Deck 29 slides com 1 vídeo comprimido: ~2.5-3.5MB
- Deck 29 slides com várias imagens grandes: ~4-5MB (limite)
