# id-scale — pele G4 Scale sobre a base Órbita

Clone das três coleções (`templates-short-deck`, `templates-expanded-deck`, `deck-frameworks`)
com o esquema visual do **G4 Scale** (extraído de `NÃOEDITAR_G4_TEMPLATE_G4SCALE.pptx`):

- **Fontes**: Libre Baskerville (display serif) + Manrope (corpo e números). IBM Plex Mono segue nos labels.
- **Paleta**: paper + navy da base, com **azul petróleo** como accent protagonista
  (`--gold-300 #298CC2 · --gold-500 #1E5C80 · --gold-700 #184560`) — gráficos, barras,
  nós e chips são azuis, como no template oficial. O **rubi** `#95253B` é toque pontual:
  só no itálico serif dos títulos em fundo claro (`.h-serif em`). A família decorativa
  `--wine-*` também aponta para petróleo (`#2E86AC · #1E5C80 · #0F3A52` — nomes mantidos
  para compatibilidade com os HTML).
- **Dark**: fundo petróleo oficial `#1E5C80` (lt2 do theme do PPTX); accent no dark é o
  azul claro `#298CC2/#53ABDB`, itálico dos títulos em `#8FC6E8` — sem vermelho no dark.
- **Motivo gráfico**: friso de barras verticais ("fringe") do template oficial —
  `assets/fringe-wave.png`, `fringe-diag.png`, `fringe-dome.png` (+ variantes `-up`
  espelhadas verticalmente, para o friso subir do rodapé). O arco orgânico `.armilar`
  foi recolorido em petróleo e ganhou overlay de frisos verticais.
- **Logos**: `assets/g4scale-logo.png` (texto navy, fundos claros) e
  `assets/g4scale-logo-light.png` (texto claro + armilar gold, fundos petróleo).
- **Cache-bust**: todos os HTML usam `style.css?v=scale2`.

Slides-herói (capa, divisor, mentor, encerramento, quote mínima) usam fundo petróleo
sólido + fringe posicionado via `style` inline no `<article>` (atributo `data-next-bg`
mantido apenas como marcador).

## Estrutura e uso

| Coleção | Conteúdo | Entrada |
|---|---|---|
| `templates-short-deck/` | 52 layouts essenciais com identidade Scale | [`templates-short-deck/index.html`](templates-short-deck/index.html) |
| `templates-expanded-deck/` | 109 layouts completos com identidade Scale | [`templates-expanded-deck/index.html`](templates-expanded-deck/index.html) |
| `deck-frameworks/` | 18 frameworks visuais com identidade Scale | [`deck-frameworks/index.html`](deck-frameworks/index.html) |

Abra [`backgrounds.html`](backgrounds.html) para consultar os motivos de fundo e frisos. Ao criar um deck, copie HTML, `style.css` e `assets/` da mesma coleção dentro de `id-scale/`; não aplique esta skin apenas trocando o CSS de um slide da raiz, porque os slides-herói incluem backgrounds e overrides inline.

## Manutenção

Esta pasta é uma variante visual da base Órbita, não uma quarta biblioteca de layouts. Quando um template canônico mudar, replique primeiro a mudança estrutural correspondente e depois preserve tokens, logos, frisos e overrides Scale. Valide cada coleção pelo respectivo `index.html` e mantenha os paths de assets relativos à própria pasta.
