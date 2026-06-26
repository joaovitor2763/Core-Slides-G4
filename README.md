# Core Slides G4

> **20 templates HTML canônicos + design system + playbook** pra construir slides de aula no padrão visual G4 (navy + gold + paper, 1600×900, accent único).

Catálogo base usado nas aulas da **Imersão em IA G4** (projeto `Aulas G4 - IA`) e nos decks de produtos do G4 OS. Foi refinado em **4 sessões** com aprendizados de bugs comuns e publicados em **2 decks de 29 slides** (`G4 Academia de IA` e `G4 Gestão e Estratégia`).

---

## TL;DR

```bash
# 1. Copia o template mais próximo
cp templates/05-grafico.html meu-slide.html

# 2. Edita copy + dados + CSS local

# 3. Valida visualmente (abre examples/index.html no navegador, vai no card)

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
├── templates/                 ← 20 templates canônicos + style.css compartilhado
│   ├── style.css              ← design tokens + classes semânticas
│   ├── 01-capa.html           ← abertura dark
│   ├── 02-palestrante.html    ← bio + retrato
│   ├── 03-quote-com-imagem.html
│   ├── 04-quote-sem-imagem.html
│   ├── 05-grafico.html
│   ├── 06-texto-focado.html
│   ├── 07-timeline.html
│   ├── 08-divisor.html        ← dark
│   ├── 09-comparacao.html
│   ├── 10-stats.html
│   ├── 11-agenda.html
│   ├── 12-imagem-legenda.html
│   ├── 13-lista.html
│   ├── 14-tres-pilares.html
│   ├── 15-encerramento.html
│   ├── 16-grafico-vertical.html
│   ├── 17-a-vs-b.html
│   ├── 18-bento.html
│   ├── 19-stepper.html
│   └── 20-quote-hero.html     ← dark
│
├── examples/
│   ├── index.html             ← passador de slides (grid 2 col + modo apresentação)
│   └── deck-inlined.html      ← exemplo de deck pronto pra g4os-pages
│
├── assets/                    ← logos, padrões, imagens exemplo
│   ├── logos/                 ← g4-logo-branca.svg
│   ├── patterns/              ← pattern-shield.png, pattern-symbol.png (low-opacity)
│   └── images/                ← imagens exemplo (Ethan, João, Satya, etc)
│
└── docs/                      ← como publicar + exportar + customizar
    ├── EXPORT-PDF.md          ← Chrome headless, 1 slide por vez, sem mesclar
    ├── PUBLISH.md             ← g4os-pages, deck-inlined, ≤5MB
    ├── CUSTOMIZE.md           ← como criar variantes dos 20 templates
    └── CHANGELOG.md           ← v1 → v2 → v3 (resumo das iterações)
```

---

## Os 20 templates (vocabulário visual)

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

**Detalhes completos de cada template** (snippet, anatomia, quando NÃO usar) estão em `playbook.md` §5.

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
- **20 templates limpos** → `templates/`
- **style.css compartilhado** → `templates/style.css`
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

**Projeto**: `Aulas G4 - IA` (id: `project_c1402fb9-6848-4cea-9fef-489da1fbf7fe`)

---

## Licença

MIT — use, modifique, distribua. Mantenha os créditos.
