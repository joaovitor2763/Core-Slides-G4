# Export PDF — Chrome headless, 1 slide por vez

> Como exportar um deck de slides HTML pra PDF em paisagem 16:9, **sem os bugs** de "mesclar tudo num único HTML".

## TL;DR

```bash
# 1. Setup
mkdir -p pdf
cp -r assets pdf/
cd pdf

# 2. Pra cada slide: copia com overrides + renderiza
for f in ../templates/[0-9][0-9]-*.html; do
  name=$(basename "$f")
  out_name="${name%.html}-pdf.html"
  has_dark=$(grep -c "mode-dark" "$f")
  if [ "$has_dark" -gt 0 ]; then bg="#001A2D"; else bg="#F5F4F3"; fi

  python3 -c "
import re
with open('$f') as fp: content = fp.read()
inject = '''<style>@page { size: 1600px 900px; margin: 0; } html,body { margin:0; padding:0; background:$bg; width:1600px; height:900px; overflow:hidden; }</style>
<style>.slide { position:relative !important; top:0 !important; left:0 !important; transform:none !important; margin:0 !important; width:1600px !important; height:900px !important; }</style>'''
content = re.sub(r'(<head[^>]*>)', r'\1\n' + inject, content, count=1)
with open('$out_name', 'w') as fp: fp.write(content)
"

  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --headless --disable-gpu --no-sandbox \
    --no-pdf-header-footer --no-margins --hide-scrollbars \
    --virtual-time-budget=8000 \
    --print-to-pdf="${name%.html}.pdf" \
    "file://$(pwd)/$out_name" > /dev/null 2>&1
done

# 3. Merge
cd pdf
ls [0-9][0-9]-*.pdf | sort > /tmp/pdfs.txt
pdf-tool merge $(cat /tmp/pdfs.txt) -o Meu-Deck.pdf

# 4. Resultado: 1 página por slide, paisagem 16:9, ~3-5MB
```

## Por que **1 slide por vez**?

O bug clássico é mesclar todos os 29 slides num único HTML e imprimir. O resultado:
- `.slide` usa `position: absolute; top: 50%; left: 50%` (pra centralizar no stage) — colide em cascata
- `@page` do CSS não escala direito
- Slide 16 (Centauro × Cyborg) com 2 colunas vira 1 coluna com texto sobreposto

A solução é renderizar **cada slide individualmente** com Chrome headless, com overrides de CSS que neutralizam o `position: absolute` + `@page` size, e depois mesclar com `pdf-tool merge`.

## O que cada injeção faz

```html
<!-- 1. Força @page em 1600x900 sem margem -->
<style>
  @page { size: 1600px 900px; margin: 0; }
  html, body {
    margin: 0; padding: 0;
    background: #001A2D;  /* navy se dark, paper se light */
    width: 1600px; height: 900px;
    overflow: hidden;
  }
</style>

<!-- 2. Neutraliza o position:absolute do .slide -->
<style>
  .slide {
    position: relative !important;
    top: 0 !important; left: 0 !important;
    transform: none !important;
    margin: 0 !important;
    width: 1600px !important;
    height: 900px !important;
  }
</style>
```

## Pré-requisitos

- **Google Chrome** no path padrão (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` no Mac, ou `google-chrome` no Linux)
- **pdf-tool** no PATH (vem com G4 OS)
- **Python 3** pra injetar o CSS

## Limitações conhecidas

- `--screenshot` (PNG único) do Chrome **não decodifica imagens** antes do print — você vai pegar o frame antes das imagens carregarem
- **Vídeos** `<video>` precisam estar em formato compatível (mp4/h264) e terem thumbnail de poster
- **Fonts externas** (Google Fonts) precisam carregar — `--virtual-time-budget=8000` dá 8s pra carregar

## Comprimir vídeo antes (se algum slide tiver .mp4)

```bash
ffmpeg -y -i original.mp4 -vf "scale=-2:480" -c:v libx264 -preset slow -crf 28 -an -movflags +faststart out.mp4
# 33MB → ~600KB, qualidade suficiente pra projetor
```

## Resultado esperado

- 29 páginas (1 por slide)
- Paisagem 16:9 (16.67" × 9.38")
- ~3-5 MB pra deck sem vídeo, ~5-8 MB com vídeo
- Visual idêntico ao navegador
