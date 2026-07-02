# Core Slides G4

> Biblioteca de slides HTML da G4 Educação (canvas 1600×900, paleta paper + navy + gold), em duas gerações:
>
> - **`templates-v5/` — v5 "Órbita" (ATUAL)**: 50 slides na linguagem editorial-orgânica (serif Playfair, superfícies com radius/sombra, chips, gravura da esfera armilar). Comece por **[templates-v5/GUIA.md](templates-v5/GUIA.md)** e navegue com `templates-v5/index.html`.
> - **`templates/` — v4 (acervo)**: 48 templates no estilo hairline minimalista, mantidos como referência e para decks antigos.

## v5 em 30 segundos

```bash
open templates-v5/index.html    # grid de preview + modo apresentação
cp templates-v5/06-grafico-barras.html meu-slide.html   # copie o mais próximo e edite
```

Regras, tokens, padrões de código e o catálogo slide a slide: [templates-v5/GUIA.md](templates-v5/GUIA.md).

---

## v4 (acervo)

> **48 templates HTML canônicos + design system + playbook** pra construir slides de aula no padrão visual G4 (navy + gold + paper, 1600×900, accent único).

Catálogo base usado nas aulas da **Imersão em IA G4** (projeto `Aulas G4 - IA`) e nos decks de produtos do G4 OS. Foi refinado em **4 sessões** com aprendizados de bugs comuns e publicados em **2 decks de 29 slides** (`G4 Academia de IA` e `G4 Gestão e Estratégia`).

---

## TL;DR

```bash
# 1. Copia o template mais próximo
cp templates/05-grafico.html meu-slide.html

# 2. Edita copy + dados + CSS local

# 3. Valida visualmente (catálogo completo: python3 -m http.server na raiz
#    e abre http://localhost:8000/examples/catalog.html — filtro por categoria + light/dark)

# 4. Publica (opcional)
#   - PDF local: usa a técnica do docs/EXPORT-PDF.md (Chrome headless 1 slide por vez)
#   - Web pública: inline tudo num único HTML ≤5MB e usa g4os-pages (docs/PUBLISH.md)
```

---

## Estrutura do repo

```
Core-Slides-G4/
├── README.md                  ← este arquivo
├── AGENTS.md                  ← regras firmes (canvas, paleta, tipografia, restrições)
├── playbook.md                ← prosa + exemplos + fluxo de uso + padrões de bug
├── LICENSE                    ← MIT
├── .gitignore                 ← ignora .DS_Store, node_modules, etc
│
├── build-deck-inlined.py      ← builda um deck HTML único (≤5MB) pra publicar
│
├── templates/                 ← 48 templates × 2 modos (light + dark) + style.css = 91 arquivos .html
│   ├── style.css              ← design tokens + classes semânticas (compartilhado)
│   ├── 01-capa.html           ← cada template light tem par NN-nome-dark.html,
│   ├── 01-capa-dark.html         exceto os dark-únicos: 08, 20, 33, 34, 39
│   ├── ...
│   ├── 05-grafico.html        ← gráficos: 05, 16, 35 (linha), 36 (donut),
│   ├── ...                       37 (barras duplas), 38 (progresso), 46 (funil)
│   ├── 39-imagem-full-overlay.html   ← imagens: 12, 26, 39, 40 (hero lateral), 41 (galeria)
│   ├── 42-quote-tweet.html    ← quotes: 03, 04, 20, 26, 34, 42, 43 (dupla)
│   └── 48-numero-hero.html    ← lista completa com descrições: AGENTS.md e playbook.md §5
│
├── examples/
│   ├── index.html             ← passador de slides (grid 2 col + modo apresentação, base do build)
│   └── catalog.html           ← catálogo navegável dos 48 templates (filtro por categoria + light/dark)
│
├── assets/                    ← logos, padrões, imagens exemplo
│   ├── logos/                 ← g4-logo-branca.svg
│   ├── patterns/              ← pattern-shield.png, pattern-symbol.png, overlay-raios.png
│   └── images/                ← imagens exemplo (Ethan, João, Satya, etc)
│
└── docs/                      ← como publicar + exportar + customizar
    ├── EXPORT-PDF.md          ← Chrome headless, 1 slide por vez, sem mesclar
    ├── PUBLISH.md             ← g4os-pages, deck-inlined, ≤5MB
    ├── CUSTOMIZE.md           ← como criar variantes dos templates
    └── CHANGELOG.md           ← v1 → v2 → v3 (resumo das iterações)
```

---

## Os 48 templates (vocabulário visual)

| # | Template | Modo | Quando usar |
|---|----------|------|-------------|
| 01 | Capa | dark | Primeira página, abrir seção |
| 02 | Palestrante | light | Bio do mentor com retrato |
| 03 | Quote com imagem | light | Citação atribuída a alguém (com retrato) |
| 04 | Quote sem imagem | light | Citação genérica, aspa marca d'água |
| 05 | Gráfico horizontal | light | Bar chart com 2-5 categorias |
| 06 | Texto focado | light | Tese forte em 2 colunas curtas |
| 07 | Timeline | light | 3-5 eventos cronológicos |
| 08 | Divisor de bloco | dark | Separar seções dentro do deck |
| 09 | Comparação A×B | light | Antes/depois, com/sem |
| 10 | Stats (4 colunas) | light | 4 métricas paralelas |
| 11 | Agenda | light | 3-6 etapas de uma jornada |
| 12 | Imagem + legenda | light | Caso/estudo com screenshot ou foto |
| 13 | Lista numerada | light | 3-7 itens com hierarquia |
| 14 | Três pilares | light | Manifesto, 3 eixos |
| 15 | Encerramento | light | Última página, hero + contato |
| 16 | Gráfico vertical + nota | light | Volume por categoria, com insight |
| 17 | A vs B | light | Split 50/50, accent no B |
| 18 | Bento mosaic | light | 4-6 blocos com proporções variadas |
| 19 | Stepper | light | 4-5 etapas sequenciais com output |
| 20 | Quote hero | dark | Citação grande em dark mode |
| 21 | 2-boxes | light/dark | 2 cards grandes (provocação "Por esporte vs Como profissional") |
| 22 | Mixed grid | light/dark | 4 quadrantes com tipos diferentes (matriz + lista + cards) |
| 23 | Custom 2-col | light/dark | Headline + sub à esquerda, corpo à direita |
| 24 | Pergunta CTA | light/dark | Eyebrow + h1 + sub + seta (pergunta de transição dark) |
| 25 | Hero com logo G4 | light/dark | Header com logo G4 + hairline + tag + barra dourada |
| 26 | Quote galeria split | light/dark | Citação serif + imagem 50% em moldura "mat de galeria" |
| 27 | Mentor hero | light/dark | Bio com nome gigante (140px) + retrato 38% |
| 28 | Transição aceleradores | light/dark | "O que vem a seguir" + fileira de 4 itens numerados |
| 29 | Bento comparativo | light/dark | Dois mosaicos lado a lado (A vs B) |
| 30 | Grid de ferramentas | light/dark | 4 colunas descritivas + faixa gold de takeaway |
| 31 | Narrativa numérica | light/dark | 3 conceitos ensinados com um dado-hero cada |
| 32 | Bento de métricas | light/dark | Mosaico 3×3 assimétrico com bignums |
| 33 | Três pilares percentuais | dark | Regra de alocação (ex: 70/20/10) com % gigante |
| 34 | Encerramento quote | dark | Fechamento com citação serif + CTA entre hairlines |
| 35 | Gráfico de linha | light/dark | Tendência/evolução no tempo (SVG inline) |
| 36 | Gráfico donut | light/dark | Composição/share de um todo (conic-gradient) |
| 37 | Barras duplas | light/dark | 2 séries × 4 categorias (antes vs depois) |
| 38 | Barras de progresso | light/dark | % de adoção/share por item, 1 linha em accent |
| 39 | Imagem full + overlay | dark | Foto full-bleed + gradiente + título na base |
| 40 | Imagem hero lateral | light/dark | Tese + imagem full-bleed 38% com edge-blend |
| 41 | Galeria duo | light/dark | Duas imagens em moldura mat com legendas |
| 42 | Quote de post/tweet | light/dark | Post de LinkedIn/X reproduzido + contexto editorial |
| 43 | Quote dupla | light/dark | Duas visões em contraste com vrule central |
| 44 | Tabela comparativa | light/dark | Matriz critérios × opções, coluna recomendada em accent |
| 45 | Checklist | light/dark | O que funciona (+) vs o que evitar (—) |
| 46 | Funil | light/dark | Conversão em 4 estágios decrescentes |
| 47 | Exercício em passos | light/dark | Dinâmica com 6 passos + tempo por etapa |
| 48 | Número hero | light/dark | Um dado gigante como takeaway |

**Cada template tem versão `-dark.html`**, exceto os dark-únicos (08, 20, 33, 34, 39 — o modo é o design). Total: **91 arquivos `.html`** no repo.

**Detalhes completos de cada template** (snippet, anatomia, quando NÃO usar) estão em `playbook.md` §5 e `AGENTS.md`.

---

## Quick start

### 1. Estrutura de um slide

```html
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<title>XX · Minha seção</title>
<link rel="stylesheet" href="style.css" />
<style>
  /* CSS local — use tokens semânticos do style.css */
  .head { position: absolute; left: var(--pad); top: 132px; right: var(--pad); }
  .head h1 { font-size: 64px; line-height: 1.05; }
  .head h1 em { font-style: italic; font-weight: 500; }
</style>
</head>
<body>
<div class="stage">
  <article class="slide" data-section="Minha seção">
    <header class="head">
      <div class="eyebrow">Eyebrow · tag mono</div>
      <h1>Título com <em>ênfase</em> em italic.</h1>
    </header>
    <!-- conteúdo do slide -->
  </article>
</div>
<script>
  const slide = document.querySelector('.slide');
  function fit(){
    const sx = window.innerWidth  / 1600;
    const sy = window.innerHeight / 900;
    const s  = Math.min(sx, sy);
    slide.style.transform = `translate(-50%, -50%) scale(${s})`;
  }
  fit();
  window.addEventListener('resize', fit);
</script>
</body>
</html>
```

### 2. Canvas fixo

- **1600×900** (16:9). Nenhum elemento deve ultrapassar esse box.
- Padding padrão: `var(--pad) = 96px`.
- JS escala o canvas pro viewport (não use `vw/vh` no conteúdo).

### 3. Paleta

| Token | Light | Dark |
|---|---|---|
| `--bg` | `#F5F4F3` (paper) | `#001A2D` (navy-600) |
| `--fg` | `#0F1419` (ink) | `#E6EEF3` (navy-50) |
| `--muted` | `#6B7278` | `#80AABF` |
| `--rule` | `#D8D6CF` | `#2D3B4A` |
| `--accent` | `#B9915B` (gold) | `#B9915B` (mesmo) |

**Accent: MÁXIMO 1× por slide.**

### 4. Tipografia

| Família | Papel | Classes |
|---|---|---|
| **Space Grotesk** | Display (títulos, números) | `.h1`–`.h4` |
| **IBM Plex Sans** | Corpo (parágrafos) | `.body`, `.lede`, `.caption` |
| **IBM Plex Mono** | Mono (eyebrows, labels) | `.eyebrow`, `.label-mono` |

Hierarquia por **italic + weight**, NUNCA por troca de fonte.

---

## Onde está o quê

- **Regras firmes** (canvas, paleta, tipografia, restrições) → `AGENTS.md`
- **Prosa, exemplos, fluxo, padrões de bug** → `playbook.md`
- **48 templates limpos** → `templates/`
- **style.css compartilhado** → `templates/style.css`
- **Catálogo navegável** → `examples/catalog.html` (via `python3 -m http.server`)
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
| `260614-awake-grove` | Design system v1 + 15 templates canônicos |
| `260614-apt-nebula` | Tokens semânticos no CSS |
| `260615-sunny-dolphin` | 1ª aula (G4 Academia de IA) — 29 slides |
| `260615-awake-creek` | Técnica de export PDF (Chrome headless 1 slide por vez) |
| `260623-misty-lake` | 2ª aula (G4 Gestão e Estratégia) + 5 templates novos (16-20) + publicação g4os-pages |
| deck `founder-ia-conteudo` | Templates 26-34 + padrões de imagem (moldura mat, hero lateral, overlay-raios) |
| expansão v4 (2026-07) | Templates 35-48 (gráficos linha/donut/duplas/progresso/funil, imagens overlay/hero/galeria, quotes tweet/dupla, tabela, checklist, exercício, número hero) + darks 27-32 + catálogo navegável |

**Projeto**: `Aulas G4 - IA` (id: `project_c1402fb9-6848-4cea-9fef-489da1fbf7fe`)

---

## Licença

MIT — use, modifique, distribua. Mantenha os créditos.
