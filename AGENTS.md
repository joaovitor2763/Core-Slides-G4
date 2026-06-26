# G4 Aulas IA — AGENTS.md (v3 · consolidada)

> **Source of truth** pra construção/edição dos slides HTML das aulas G4.
> Reúne o que foi aprendido em: `260614-awake-grove` (20 templates), `260615-sunny-dolphin` (29 slides Academia de IA), `260615-awake-creek` (PDF export) e `260623-misty-lake` (29 slides Gestão e Estratégia).

> Para prosa e exemplos, ver `playbook.md` (mesma pasta). Este arquivo é só regras.

---

## Regra de ouro
**UM slide por vez.** Criar/editar → validar visualmente → só então passar ao próximo.
Nunca editar/criar vários slides em lote. Nunca confiar em screenshot headless do Chrome (decodifica imagem tarde demais) — abrir no navegador real ou pedir print ao usuário.

---

## Canvas fixo
- Proporção **16:9** (`1600x900`).
- Padding consistente: **`var(--pad)` = 96px`.
- Nenhum elemento deve ser posicionado fora de `0..1600 × 0..900`.
- Background: `var(--bg)` light = `#F5F4F3` (paper) ou `var(--navy-600)` dark via `.mode-dark`.
- Texto: `var(--fg)` light = `#0F1419` (ink) ou `var(--navy-50)` dark.
- Acento único: `var(--accent)` = `#B9915B` (dourado queimado) — **mesmo em dark mode**.

---

## Paleta (style.css)

### Light mode (default)
| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#F5F4F3` | fundo slide |
| `--bg-2` | `#ECEAE6` | faixa/card secundário |
| `--fg` | `#0F1419` | texto principal |
| `--fg-2` | `#2A2F35` | texto secundário |
| `--fg-muted` | `#6B7278` | labels, captions |
| `--hairline` | `#D8D6CF` | divisores |
| `--accent` | `#B9915B` | **único accent**, máx 1× por slide |
| `--accent-soft` | `#D4B189` | accent em opacity/hover |
| `--accent-deep` | `#8E6F44` | accent em texto bold |

### Dark mode (`.mode-dark`)
| Token | Valor |
|---|---|
| `--bg` | `#001A2D` (navy-600) |
| `--bg-2` | `#001525` (navy-700) |
| `--fg` | `#E6EEF3` (navy-50) |
| `--fg-2` | `#B3CCD9` (navy-100) |
| `--fg-muted` | `#80AABF` (navy-200) |
| `--hairline` | `#2D3B4A` (rule-dark) |
| `--accent` | **mesmo `#B9915B`** |

### Navy scale (sempre disponível)
`50 #E6EEF3 · 100 #B3CCD9 · 200 #80AABF · 300 #4D88A5 · 400 #26668A · 500 #001F35 · 600 #001A2D · 700 #001525 · 800 #00101D · 900 #000B15`

### Gold scale
`300 #D4B189 · 500 #B9915B (principal) · 700 #8E6F44`

---

## Tipografia (3 famílias, papéis distintos)

| Família | Papel | Quando usar | Classes |
|---|---|---|---|
| **Space Grotesk** | Display (títulos, números, hero) | h1/h2/h3, `.h-display`, `--fs-display-*` | `.h1`–`.h4` |
| **IBM Plex Sans** | Corpo (parágrafos, citações, descrições) | `.body`, `.lede`, `.caption`, texto corrido | `.body`, `.lede`, `.caption` |
| **IBM Plex Mono** | Mono (eyebrows, labels técnicas, dados) | `.eyebrow`, `.label-mono`, kickers | `.mono`, `.label-mono` |

**Hierarquia por italic + weight, NUNCA por troca de fonte.** Ênfase sempre na mesma família (italic + 500/600).

**Escala semântica** (use essas classes em vez de font-size solto):
- Display: `.h1` 88px · `.h2` 56px · `.h3` 32px · `.h4` 20px (Space Grotesk)
- Text: `.lede` 24px · `.body` 18px · `.caption` 14px (IBM Plex Sans)
- Mono: `.label-mono` 12px · `.eyebrow` 13px (IBM Plex Mono)
- Tokens CSS: `--fs-display-xl` 148 (capa) · `--fs-display-l` 108 (divisor) · `--fs-display-m` 72 · `--fs-display-s` 44 · `--fs-text-l` 28 · `--fs-text-m` 18 · `--fs-text-s` 14 · `--fs-mono` 12

---

## Modo dark
Adicione a classe `mode-dark` no `<article class="slide">`. Tokens semânticos reescritos automaticamente.

Slides que **devem** ser dark por design: capa (1), divisor de capítulo (24), perguntas de transição dark (9, 18), modo apresentação/CTA (23), encerramento/quote final (29).

---

## Footer dos slides
- **Sem contagem de slides** (`01 / 29` etc.) — templates são reaproveitados em outros decks.
- Footer via `data-section="..."` no `<article class="slide">` → renderiza como eyebrow canto superior esquerdo via `::before` em mono 11px muted. **Opcional** (se vazio, não renderiza nada).
- HTML **nunca** deve duplicar o footer (não escrever `<div>01 / 29</div>`).

---

## Sub-agentes (regras pra delegar)
- **Redesign ou revisão visual**: usar **Opus 4.7** ou **Opus 4.8** via `mcp__session__subagent_run` com `connectionSlug: managed-g4-aigateway` e `model: anthropic.claude-opus-4-7` (ou `anthropic.claude-opus-4-8`).
- Brief do sub-agente deve incluir: **caminho absoluto** do arquivo, **texto que NÃO pode ser alterado**, lista do que está errado, restrições de design.
- **Auditoria visual em batch**: sub-agente lê só o código (sem ferramenta de imagem) e classifica cada slide como ✅/❌ com justificativa de 1 linha.
- **NÃO usar** sub-agente pra 1 slide simples — fazer manualmente, mais rápido.

---

## Restrições de design (rígidas)
1. **Accent dourado: MÁXIMO 1× por slide** (barra do `.eyebrow::before` conta como a mesma pinta). Exceção: o accent pode aparecer em 2 unidades SE uma for a barra do eyebrow e a outra for uma palavra só em `<em>` dentro de texto (não em heading inteiro).
2. **Ênfase tipográfica** = `font-style: italic` + `font-weight: 500/600`. Nunca trocar pra serif (serif só no título da capa + dividers editoriais com Cormorant Garamond).
3. **Layout assimétrico** quando variance > 4 (regra do design-taste-frontend). Evitar hero centralizado.
4. **Sem card/sombra/glass**. Hierarquia com `border-top: 1-2px solid var(--ink)` ou `var(--rule)`.
5. **Sem emoji em títulos, subtitles, headings ou labels** (a menos que carregue significado semântico).
6. **Cores hexadecimais explícitas** no CSS (não `rgb()` a menos que com alpha). Royal gold = `#B9915B`, navy-600 = `#001A2D`.
7. **Mudar 1 slide por vez, validar visualmente, próximo.** Não fazer "batch" de 5 slides sem validar.

---

## Estrutura de arquivos

```
artifacts/
  style.css             ← design tokens + classes semânticas (compartilhado)
  index.html            ← passador de slides (grid 2 col + modo apresentação)
  AGENTS.md             ← este arquivo (regras firmes)
  playbook.md           ← prosa + exemplos + fluxo de uso (legível)
  AUDITORIA.md          ← auditoria visual de cada slide (✅/⚠️/❌)
  assets/               ← imagens, SVGs, vídeos
  01-capa.html          ← 1 slide por arquivo
  02-….html
  29-quote-final.html
  G4-Gestao-Estrategia-Aula-V1.pdf  ← PDF final (exportado)
```

---

## Lista dos 20 templates (catálogo canônico)

| # | Template | Tipo | Modo | Notas |
|---|----------|------|------|-------|
| 01 | Capa | Abertura | dark | Título hero + faixa vertical accent + logo G4 + hairline "Para quem quer mais" |
| 02 | Palestrante | Bio + retrato | light | Retrato dark à direita (38%) + bio à esquerda (55%) |
| 03 | Quote com imagem | Citação | light | Frame de retrato + citação com barra accent 8px |
| 04 | Quote sem imagem | Citação | light | Aspa marca d'água 320px opacity 0.06 + texto respira |
| 05 | Gráfico horizontal | Dados | light | Bar chart P&B + 1 coluna accent |
| 06 | Texto focado | Tese | light | 2 colunas, label à esquerda + lede |
| 07 | Timeline | Linha do tempo | light | 4 etapas com ano+regra+descrição, etapa ativa em accent |
| 08 | Divisor de bloco | Capítulo | **dark** | Navy 600, número gigante, italic, hairline |
| 09 | Comparação A×B | Antes/depois | light | Sem "×" no título, 6h vs 22min como hero |
| 10 | Stats (4 colunas) | Dados | light | Métricas, título com indent assimétrico |
| 11 | Agenda | Roteiro | light | 4 linhas com etapa atual em italic+accent |
| 12 | Imagem + legenda | Caso | light | Frame escuro 62% + sidebar 30% |
| 13 | Lista numerada | 5 princípios | light | Items compactos, tag mono à direita |
| 14 | Três pilares | Manifesto | light | Layout horizontal, 3 eixos |
| 15 | Encerramento | Fechamento | light | Hero + rail de contato |
| 16 | Gráfico vertical + nota | Volume | light | Barras verticais + insight editorial |
| 17 | A vs B | Comparação | light | Split 50/50, hairline divisor, accent no B |
| 18 | Bento mosaic | Mosaico | light | 5 células com proporções variadas |
| 19 | Stepper | 4 etapas | light | Colunas com hairline vertical entre elas |
| 20 | Quote hero | Citação grande | **dark** | Navy 700 + overlay + aspa accent |

**Reaproveitamento**: esses 20 templates são o vocabulário visual. O deck `260615-sunny-dolphin` (29 slides Academia de IA) e o deck `260623-misty-lake` (29 slides Gestão e Estratégia) **não correspondem 1:1** aos 20 — eles misturam templates e criam variantes (perguntas dark, bento custom, comparador de produtos, etc).

---

## Mapeamento dos 29 slides do deck G4 Gestão e Estratégia

| Slide | Modo | Template-base | Notas |
|---|---|---|---|
| 01 capa | dark | 01 | Custom: escudo + símbolo G4 + hairline "Para quem quer mais" + barra dourada |
| 02 pergunta | light | 06 (texto focado) | 2 boxes "Por esporte" vs "Como profissional" |
| 03 palestrante | light | 02 | Bio do mentor |
| 04 pilares | light | 14 (três pilares) | 3 eixos do futuro |
| 05 time-horizon | light | 05 (gráfico) | METR chart com timeline |
| 06 will-smith | light | 03 (quote com imagem) | Vídeo antes/depois |
| 07 preferencia-humana | light | 05 (gráfico) | Bar chart 3 modelos |
| 08 custo-inteligencia | light | 17 (A vs B) | o1 vs GPT-5 com stats |
| 09 pergunta-transicao | **dark** | 04 (quote sem imagem) | Pergunta provocativa serif |
| 10 dois-mundos | light | 11 (agenda) | Lista comentada |
| 11 callback | light | 17 (A vs B) | Gestor vs executor (2 boxes) |
| 12 agenda-parte-2 | light | 11 (agenda) | Conceitos |
| 13 mollick | light | 12 (imagem + legenda) | Quote + foto |
| 14 funcionario | light | 14 (3 pilares) | IA como funcionário |
| 15 tarefas-vendedor | light | 18 (bento) | 5 tarefas em bento assimétrico |
| 16 centauro-cyborgue | light | 17 (A vs B) | 2 cards separados |
| 17 passo-a-passo | light | 19 (stepper) | 4 etapas |
| 18 quem-lidera | **dark** | 20 (quote hero) | Pergunta serif "quem deve liderar isso no negócio?" |
| 19 lideres | light | 18 (bento) | Hero navy + 3 facts (card "medo" pivô dourado) |
| 20 indicador-produtividade | light | 10 (stats 4 col) | Métricas de produtividade |
| 21 facilite-time | light | 05 (gráfico) | Harris Poll 81% vs 32% vs 29% vs 25% |
| 22 exemplo-marketing | light | 18 (bento) | Matriz 2×2 + 5 tarefas do vendedor com ação |
| 23 cta-pratica | **dark** | 20 (quote hero) | "Vamos abrir o G4 OS" |
| 24 como-fazer-durar | **dark** | 08 (divisor) | "Como fazer isso durar →" + header G4 |
| 25 sustentavel-detalhe | light | 13 (lista) | Detalhes sustentabilidade |
| 26 satya | light | 12 (imagem + legenda) | Tweet Satya + comentário |
| 27 4-classes | light | 14 (3 pilares) | 4 classes de ferramentas |
| 28 medir-antes-depois | light | 13 (lista) | Antes vs depois |
| 29 quote-final | **dark** | 20 (quote hero) | Fechamento com aspa + autor + footer |

---

## Aprendizados canônicos (vão pra decisões futuras)

- **Slide 16 (gráfico vertical) é o caso clássico de "número no lugar errado"** — quando o número deve ficar acima de cada barra, o `position:absolute; bottom:100%+N` precisa ter o `.val` **dentro do `.stem`** (altura variável), NÃO dentro do `.bar-v` (altura 100% do chart). Senão `bottom: 100%` referencia o topo do chart inteiro, e todos os números ficam alinhados no topo.
- **Slide 14 é o caso clássico de "título que invade o grid abaixo"** — sempre reservar `top:380+` antes de grids horizontais.
- **Slide 15 é o caso clássico de "max-width grande demais"** que conflita com rail à direita — calcular `(1600 - 96*2) - rail - gap` antes de chutar max-width.
- **Slide 13 é o caso clássico de "lista com padding grande demais"** que vaza — calcular `(900 - top - footer) / n_itens` antes de padding.
- **Slide 19 (stepper) é o caso clássico de `flex:1` em flex-direction:column cria vácuo invisível** — sem `justify-content: space-between` o conteúdo cola no topo.
- **Slide 6 (will-smith) é o caso clássico de "vídeo pesado no g4os-pages"** — comprimir com ffmpeg `libx264 -crf 28 -vf "scale=-2:480" -an` antes de inline-ar (33MB → 610KB).
- **Slide 6 também é o caso de "src= como string literal quebra template"** — em cards de passador publicado, use `ifr.setAttribute('srcdoc', html)` em vez de template literal com `${s.html}`.
- **Publicação única em sites.g4oscloud.com** — para o passador inlinado, cada slide precisa ter o `style.css` inline também (senão o CSS não carrega no srcdoc). 5MB é o limite por arquivo.

---

## Fluxo de uso (resumo)

**Criar slide novo**:
1. Copiar o template mais próximo de `260614-awake-grove/artifacts/[NN-template].html` (se diferente contexto) ou de um slide existente.
2. Editar copy + dados no novo arquivo.
3. **Validar visualmente**: abrir `index.html` no navegador, ir no card, dar zoom/print.
4. Adicionar entrada no array `slides` do `index.html`.
5. **Regerar o deck-inlined** com o script Python (builds all-in-one pra g4os-pages).
6. **Republicar** com `mcp__g4os-pages__republish_page`.

**Editar slide existente**:
1. Ler o slide, identificar o template-base, planejar o diff.
2. Editar copy/dados/CSS local.
3. Validar visualmente.
4. Regerar deck-inlined e republicar.

**Reaproveitar em outro deck**:
1. Copiar `style.css` + `index.html` + `assets/`.
2. Editar cada slide e o array `slides` no `index.html`.
3. Publicar.

---

## Publicação (g4os-pages)

- **Ferramenta**: `mcp__g4os-pages__publish_page` com `slug`, `title`, `html` (string única).
- **Limite**: 5MB por arquivo. Deck de 29 slides + vídeo comprimido: ~3.7MB.
- **Estratégia "deck-inlined"**: cada slide vira um `<script type="application/json" id="slide-NN">{file, html}</script>` no `<head>` do `index.html`. O JS lê via `getElementById().textContent` + `JSON.parse()`. Cada slide tem o `style.css` inline também (srcdoc não herda CSS do parent).
- **Para o `g4os-pages`**: usar `republish_page` pra atualizar (não republicar com novo slug — o `publish_page` vai incrementar slug tipo `aula-ia-ge-2`).
- **URL final**: `https://sites.g4oscloud.com/s/<slug>/` (noindex por padrão).

---

## Cross-references

- **Catálogo canônico de 20 templates** (raw HTML): `templates/`
- **Playbook narrativo** (prosa + exemplos): `playbook.md` (mesma pasta)
- **Passador de slides** (exemplo): `examples/index.html`
- **Como publicar**: `docs/PUBLISH.md`
- **Como exportar PDF**: `docs/EXPORT-PDF.md`
- **Como customizar templates**: `docs/CUSTOMIZE.md`
- **Changelog**: `docs/CHANGELOG.md`
- **Projeto**: `Aulas G4 - IA` (`project_c1402fb9-6848-4cea-9fef-489da1fbf7fe`)
- **Sessões-chave** (no G4 OS):
  - `260614-awake-grove` — design system + 20 templates canônicos
  - `260614-apt-nebula` — tokens semânticos no CSS
  - `260615-sunny-dolphin` — 1ª aula (G4 Academia de IA, 29 slides)
  - `260615-awake-creek` — técnica de export PDF em paisagem 16:9
  - `260623-misty-lake` — 2ª aula (G4 Gestão e Estratégia, 29 slides) + publicação