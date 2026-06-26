# Changelog — Core Slides G4

## v3.0 — 2026-06-26

**Primeira release pública.**

- **20 templates canônicos** validados (01-20) em `templates/`
- **`style.css` compartilhado** com paleta navy + gold, 3 famílias de fonte (Space Grotesk + IBM Plex Sans + IBM Plex Mono)
- **`AGENTS.md`** consolidado com regras firmes (canvas 1600×900, accent único, modo dark, etc)
- **`playbook.md`** com prosa + exemplos + padrões de bug
- **`examples/index.html`** — passador de slides funcional
- **`assets/`** — logos, patterns e imagens exemplo
- **`docs/EXPORT-PDF.md`** — técnica de export PDF via Chrome headless
- **`docs/PUBLISH.md`** — publicação no g4os-pages
- **`docs/CUSTOMIZE.md`** — padrões de customização + bugs comuns
- **Licença MIT**

### Proveniência

| Sessão | Contribuição |
|---|---|
| `260614-awake-grove` | Design system v1 + 15 templates |
| `260614-apt-nebula` | Tokens semânticos no CSS |
| `260615-sunny-dolphin` | 1ª aula (G4 Academia de IA, 29 slides) |
| `260615-awake-creek` | Técnica de export PDF (Chrome headless 1 slide por vez) |
| `260623-misty-lake` | 2ª aula (G4 Gestão e Estratégia) + 5 templates novos (16-20) + publicação g4os-pages |

### Aprendizados canônicos consolidados (do `playbook.md`)

- Slide 16: número da barra precisa estar **dentro do `.stem`** (não do `.bar-v`)
- Slide 14: reservar `top:380+` antes de grids horizontais
- Slide 15: `max-width = (1600 - 96*2) - rail - gap` antes de chutar
- Slide 13: padding da lista = `(900 - top - footer) / n_itens`
- Slide 19: `flex: 1` em flex-direction:column cria vácuo invisível — usar `space-between` no parent
- Slide 6 (vídeo): comprimir MP4 com ffmpeg `crf 28 scale=-2:480` (33MB → 600KB)
- Passador publicado: cada slide precisa ter `style.css` inline também (srcdoc não herda)
- Passador publicado: `ifr.setAttribute('srcdoc', s.html)` em vez de template literal (evita quebra de aspas)

### Mudanças v2 → v3

- **Removido `data-page` do design system** (contagem de slides não é fixa, slides são reaproveitados)
- **Navy-600** virou bg dark (substituindo navy-700 que era muito profundo)
- **Gold accent** voltou pro dourado queimado `#B9915B` (após teste de "royal gold" que ficou pálido demais)
- **`Cormorant Garamond` serif** adicionado pra capa + divisor + perguntas dark (editorial weight)
- **5 templates novos** (16-20): grafico-vertical, a-vs-b, bento, stepper, quote-hero
