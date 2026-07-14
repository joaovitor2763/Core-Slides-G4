# id-next — pele G4 Next sobre a base Órbita

Clone das três coleções (`templates-short-deck`, `templates-expanded-deck`, `deck-frameworks`)
com o esquema visual do **G4 Next** (extraído de `NÃO EDITAR_G4 Next_Template Aulas_2026.pptx`):

- **Fontes**: Libre Baskerville (display serif) + Manrope (corpo e números). IBM Plex Mono segue nos labels.
- **Paleta**: paper + navy + gold da marca, com a família **vinho** do Next
  (`--wine-300 #8D4949 · --wine-500 #612525 · --wine-700 #3A1616`, gradiente `--wine-grad`).
- **Dark**: fundo petróleo profundo `#051D2C` (o navy do template Next).
- **Esfera armilar Next**: `assets/armilar-next.png` (navy, light) e `assets/armilar-next-gold.png` (gold, dark),
  já ligadas em `--armilar-solid/--armilar-eng`. Logo lockup em `assets/g4next-logo.png`.
- **Helpers novos** no style.css: `.next-arch` (arco orgânico em gradiente vinho), `.chip--wine`, `.surface--wine`, `.wine`.

## Estrutura e uso

| Coleção | Conteúdo | Entrada |
|---|---|---|
| `templates-short-deck/` | 52 layouts essenciais com identidade Next | [`templates-short-deck/index.html`](templates-short-deck/index.html) |
| `templates-expanded-deck/` | 109 layouts completos com identidade Next | [`templates-expanded-deck/index.html`](templates-expanded-deck/index.html) |
| `deck-frameworks/` | 18 frameworks visuais com identidade Next | [`deck-frameworks/index.html`](deck-frameworks/index.html) |

Abra [`backgrounds.html`](backgrounds.html) para consultar os backgrounds da identidade. Ao criar um deck, copie HTML, `style.css` e `assets/` da mesma coleção dentro de `id-next/`; não aplique esta skin apenas trocando o CSS de um slide da raiz, porque há ajustes e backgrounds definidos nos próprios HTML.

## Manutenção

Esta pasta é uma variante visual da base Órbita, não uma quarta biblioteca de layouts. Quando um template canônico mudar, replique primeiro a mudança estrutural correspondente e depois preserve os tokens, logos, fundos e overrides Next. Valide cada coleção pelo respectivo `index.html` e mantenha os paths de assets relativos à própria pasta.
