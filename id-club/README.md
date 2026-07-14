# id-club — pele G4 Club sobre a base Órbita

Clone das três coleções (`templates-short-deck`, `templates-expanded-deck`, `deck-frameworks`)
com o esquema visual do **G4 Club** (extraído de `NÃO EDITAR_G4CLUB_TEMPLATE.pptx`):
identidade escura e sóbria — navy quase-preto + gold da marca.

- **Fontes**: Libre Baskerville (display serif) + Manrope (corpo e números). IBM Plex Mono nos labels.
- **Paleta**: navy quase-preto `#121722/#101823` como dark, paper da base nos slides claros,
  e **gold** como accent único (`--gold-300 #CAA977 · --gold-500 #B9915B · --gold-700 #8F6A3F`).
  No claro o accent usa o tom fundo `#8F6A3F` (contraste); no dark, o gold da marca `#B9915B`
  com texto escuro sobre preenchimentos (`--on-gold #121722`). A família decorativa `--wine-*`
  também aponta para gold (nomes mantidos por compatibilidade).
- **Motivo gráfico**: ghost "CLUB" em letterpress — `assets/bg-club-ghost.png` (letras no topo),
  `bg-club-ghost-v.png` (letras verticais) e `bg-club-gold.png` (painel dourado, para quotes).
  O arco orgânico `.armilar` foi recolorido em gradiente gold.
- **Itálico serif**: sempre gold (`#8F6A3F` no claro, `#CAA977` no dark).
- **Logo**: `assets/g4club-logo.png` (texto claro + armilar gold — fundos escuros).
- **Cache-bust**: todos os HTML usam `style.css?v=club1`.

Slides-herói (capa, divisor, mentor, encerramento, quote mínima) usam `#121722` +
ghost CLUB via `style` inline no `<article>` (atributo `data-next-bg` mantido como marcador).

## Estrutura e uso

| Coleção | Conteúdo | Entrada |
|---|---|---|
| `templates-short-deck/` | 52 layouts essenciais com identidade Club | [`templates-short-deck/index.html`](templates-short-deck/index.html) |
| `templates-expanded-deck/` | 109 layouts completos com identidade Club | [`templates-expanded-deck/index.html`](templates-expanded-deck/index.html) |
| `deck-frameworks/` | 18 frameworks visuais com identidade Club | [`deck-frameworks/index.html`](deck-frameworks/index.html) |

Abra [`backgrounds.html`](backgrounds.html) para consultar os backgrounds letterpress. Ao criar um deck, copie HTML, `style.css` e `assets/` da mesma coleção dentro de `id-club/`; não aplique esta skin apenas trocando o CSS de um slide da raiz, porque os slides-herói incluem fundos e overrides inline.

## Manutenção

Esta pasta é uma variante visual da base Órbita, não uma quarta biblioteca de layouts. Quando um template canônico mudar, replique primeiro a mudança estrutural correspondente e depois preserve tokens, logos, letterpress e overrides Club. Valide cada coleção pelo respectivo `index.html` e mantenha os paths de assets relativos à própria pasta.
