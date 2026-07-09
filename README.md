# Core Slides G4

> **Two decks, one language.** Build G4 slides by picking the deck that matches your project size — not by version number. All official templates share the **"Órbita"** visual language (Playfair serif + Space Grotesk display, navy + gold + paper, sphere armilar overlay, surfaces with radius + soft shadow, chips/pills for meta).
>
> 📦 **`templates-short-deck/` e `templates-expanded-deck/` vão pro git** (são os templates oficiais). `templates-legacy/` e `templates-column/` são gitignored (acervo congelado / skin opcional, local-only).

## The official decks

| Deck | Slides | Use it for |
|---|---|---|
| **[`templates-short-deck/`](templates-short-deck/README.md)** | **52** | Lean projects — aulas, workshops, talks, internal decks. The minimum viable G4. **Start here.** |
| **[`templates-expanded-deck/`](templates-expanded-deck/README.md)** | **109** | Everything: case study (8 etapas), relatório financeiro (DRE, fluxo de caixa, orçamento, cenários, mapa de riscos), pitch de vendas, apresentação de produto. Same language as short-deck, more layouts. |
| **[`templates-legacy/`](templates-legacy/)** | **48** | v4 hairline-minimalista acervo. Frozen. Reference only (use for compatibility with old decks). **Gitignored** — local-only (não vai no `git clone`). |
| `templates-column/` | 52 | Optional third skin — same 52 layouts as short-deck, re-skinned with the [Column](https://column.com) fintech visual language. Drop-in alternative. **Gitignored** — local-only. |

> **Decisão prática:** se você não sabe qual escolher, vá de `short-deck` (52). Ele cobre 90% dos projetos. Se faltar layout (ex: você precisa de um slide de fluxo de caixa), promova o deck para `expanded-deck` e copie o template extra que falta.

---

## Quick start

```bash
# 1. Clone o repo
git clone https://github.com/joaovitor2763/Core-Slides-G4.git
cd Core-Slides-G4

# 2. Coloque os templates oficiais (passo a passo abaixo)
#    — ou baixe o zip oficial e descompacte em templates-short-deck/

# 3. Copie o template mais próximo do seu slide
cp templates-short-deck/06-grafico-barras.html meu-slide.html

# 4. Edite copy + dados + CSS local
#    (use tokens do templates-short-deck/style.css)

# 5. Valide visualmente abrindo no browser
open meu-slide.html

# 6. Publique (opcional)
#   - PDF: docs/EXPORT-PDF.md (Chrome headless, 1 slide por vez)
#   - Web: docs/PUBLISH.md (g4os-pages, deck-inlined ≤5MB)
```

---

## Working with the official templates

Os **dois decks oficiais** (`templates-short-deck/` 52 slides e `templates-expanded-deck/` 109 slides) **vão no `git clone`** — são o produto deste repo. Você abre o `index.html` da pasta e navega no passador, ou copia o template mais próximo e edita:

```bash
# Já funciona após git clone
open templates-short-deck/index.html
cp templates-short-deck/06-grafico-barras.html meu-slide.html
# editar + validar visualmente
```

**As outras duas pastas são local-only (gitignored):**
- `templates-legacy/` (48 v4 hairline) — acervo congelado, mantido em disco pra rodar o skill `g4-slides` mas **não vai no `git clone`**. Se precisar, baixe separadamente.
- `templates-column/` (52 com pele Column) — skin opcional, mesmo caso.

> **Quem precisa commitar `style.css` ou `index.html` dos decks Órbita?** Eles já estão commitados. Não force-add nada a menos que esteja criando uma variante.

---

## "Órbita" visual language

- **Display:** Space Grotesk para h1–h4 + números.
- **Serif:** Playfair Display em capa, dark dividers e quote-hero — itálico dourado na palavra-chave.
- **Body:** IBM Plex Sans. Mono (eyebrows, labels, dados): IBM Plex Mono.
- **Paleta:** paper `#F5F4F3` · navy `#001525` (light e dark) · gold `#B9915B` (light) / `#C9A05C` (dark).
- **1 accent por slide.** Cards com radius 22 + soft shadow; hairlines para hierarquia em tabelas densas.
- **Sphere armilar** (`.armilar` / `.armilar--engraving`) como overlay decorativo, com PNGs pré-tingidos por modo em `templates-*/assets/`. Outras decorações: `.grain` (filme), `.ghost` (linha-eco), `.glow` (halo dourado).
- **Canvas fixo 1600×900** com `fit()` JS que escala pro viewport. Nada de `vw/vh/%` no conteúdo.

Detalhes completos: [`AGENTS.md`](AGENTS.md) (regras firmes) e [`playbook.md`](playbook.md) (prosa, fluxo, padrões de bug).

---

## Estrutura do repo

```
Core-Slides-G4/
├── README.md                    ← este arquivo
├── AGENTS.md                    ← regras firmes (canvas, paleta, tipografia, restrições)
├── playbook.md                  ← prosa + exemplos + fluxo de uso + padrões de bug
├── LICENSE                      ← MIT
├── .gitignore                   ← ignora templates-*/ e *.zip (oficiais são externos)
│
├── build-deck-inlined.py        ← builda um deck HTML único (≤5MB) pra publicar
│
├── templates-short-deck/        ← (COMMITTED) 52 slides Órbita
├── templates-expanded-deck/     ← (COMMITTED) 109 slides Órbita
├── templates-legacy/            ← (LOCAL) 48 templates v4 hairline, gitignored
├── templates-column/            ← (LOCAL) 52 slides com pele Column, gitignored
│
├── examples/
│   ├── index.html               ← passador de slides (grid 2 col + modo apresentação, base do build)
│   └── catalog.html             ← catálogo navegável dos 48 templates legacy (filtro por categoria + light/dark)
│
├── assets/                      ← logos, padrões, imagens exemplo (commitado)
│   ├── logos/                   ← g4-logo-branca.svg
│   ├── patterns/                ← pattern-shield.png, pattern-symbol.png
│   └── images/                  ← imagens exemplo (Ethan, João, Satya, etc)
│
└── docs/                        ← como publicar + exportar + customizar
    ├── EXPORT-PDF.md            ← Chrome headless, 1 slide por vez
    ├── PUBLISH.md               ← g4os-pages, deck-inlined, ≤5MB
    ├── CUSTOMIZE.md             ← como criar variantes dos templates
    └── CHANGELOG.md             ← histórico de iterações (v1 → v4)
```

> **Pastas marcadas `(LOCAL)`** são gitignored — não vêm no `git clone` (vide [Working with the official templates](#working-with-the-official-templates)). O `git clone` traz apenas `templates-short-deck/` + `templates-expanded-deck/` (os decks oficiais) + design system + docs + assets compartilhados.

---

## The legacy acervo (v4)

> **48 templates HTML canônicos + design system + playbook** no estilo hairline minimalista anterior (sem radius, sem sombra, sem serif display).

Catálogo base usado nas aulas da **Imersão em IA G4** (projeto `Aulas G4 - IA`) e nos primeiros decks de produtos do G4 OS. Foi refinado em **4 sessões** com aprendizados de bugs comuns e publicado em **2 decks de 29 slides** (`G4 Academia de IA` e `G4 Gestão e Estratégia`).

Use `templates-legacy/` apenas para compatibilidade com decks antigos. Para projetos novos, use **`templates-short-deck/`** (52) ou **`templates-expanded-deck/`** (109).

Catálogo navegável (filtro por categoria + toggle light/dark) — `python3 -m http.server` na raiz e abrir `http://localhost:8000/examples/catalog.html`.

---

## Onde está o quê

- **Regras firmes** (canvas, paleta, tipografia, restrições) → [`AGENTS.md`](AGENTS.md)
- **Prosa, exemplos, fluxo, padrões de bug** → [`playbook.md`](playbook.md)
- **Catálogo de 52 slides (curto)** → `templates-short-deck/` (local) + [`templates-short-deck/GUIA.md`](templates-short-deck/GUIA.md)
- **Catálogo de 109 slides (expandido)** → `templates-expanded-deck/` (local) + [`templates-expanded-deck/GUIA.md`](templates-expanded-deck/GUIA.md)
- **Catálogo navegável do acervo v4** → `examples/catalog.html` (via `python3 -m http.server`)
- **Passador de exemplo** → `examples/index.html`
- **Assets base** (logos, padrões, imagens) → `assets/`
- **Como exportar PDF** → `docs/EXPORT-PDF.md`
- **Como publicar no g4os-pages** → `docs/PUBLISH.md`
- **Como customizar templates** → `docs/CUSTOMIZE.md`
- **Changelog** → `docs/CHANGELOG.md`

---

## Proveniência

Sessões-chave que produziram este repo:

| Sessão | Contribuição |
|---|---|
| `260614-awake-grove` | Design system v1 + 15 templates canônicos (v3) |
| `260614-apt-nebula` | Tokens semânticos no CSS |
| `260615-sunny-dolphin` | 1ª aula (G4 Academia de IA) — 29 slides no v3 |
| `260615-awake-creek` | Técnica de export PDF (Chrome headless 1 slide por vez) |
| `260623-misty-lake` | 2ª aula (G4 Gestão e Estratégia) + 5 templates novos (16-20) + publicação g4os-pages |
| `deck founder-ia-conteudo` | Templates 26-34 + padrões de imagem (moldura mat, hero lateral, overlay) |
| `expansão v4 (2026-07)` | Templates 35-48 (gráficos linha/donut/duplas/progresso/funil, imagens overlay/hero/galeria, quotes tweet/dupla, tabela, checklist, exercício, número hero) + darks 27-32 + catálogo navegável |
| `geração Órbita (v5 → short-deck, 2026-07-07)` | Nova linguagem visual editorial-orgânica (Playfair, surfaces, chips, armilar). 52 templates, vira o deck curto. |
| `expansão Órbita (v6 → expanded-deck, 2026-07-07)` | +57 templates organizados em 10 categorias (case, financeiro, pitch, produto, aulas). 109 total. |
| `rebrand de folders (2026-07-09)` | `templates-v5/ → templates-short-deck/`, `templates-v6/ → templates-expanded-deck/`, `templates/ → templates-legacy/`. Folders oficiais movidos pra fora do git. README reescrito como "Two decks, one language". |

**Projeto**: `Aulas G4 - IA` (id: `project_c1402fb9-6848-4cea-9fef-489da1fbf7fe`)

---

## Licença

MIT — use, modifique, distribua. Mantenha os créditos.
