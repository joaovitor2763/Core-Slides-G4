# Core Slides G4 — AGENTS.md (regras firmes do design system)

> **Três decks, uma linguagem.** Para a geração ATUAL — **`templates-short-deck/` (52)**, **`templates-expanded-deck/` (109)** e **`deck-frameworks/` (biblioteca especializada)**, todos na linguagem visual "Órbita" — a source of truth dos tokens, padrões de código, catálogo e QA é a `GUIA.md` de cada pasta. Este `AGENTS.md` continua sendo a referência firme para regras compartilhadas + acervo legacy.
>
> **Variantes de identidade**: `id-next/`, `id-scale/` e `id-club/` clonam as três coleções oficiais e aplicam, respectivamente, as identidades G4 Next, G4 Scale e G4 Club. A geometria e a finalidade dos templates continuam equivalentes; mudam tokens, tipografia, logos, backgrounds, motivos gráficos e alguns overrides locais. Para editar uma variante, preserve o conjunto da própria pasta (`HTML + style.css + assets`) e leia primeiro o `README.md` daquele `id-*`.
>
> **Localização dos templates**: `templates-short-deck/`, `templates-expanded-deck/`, `deck-frameworks/` e as três pastas `id-*` vão no `git clone`. `templates-legacy/` e `templates-column/` são gitignored (acervo congelado / skin opcional, local-only). Veja `README.md` → *The three official decks* e *Identity variants*.

> **Source of truth** para construção e edição de slides HTML G4 — aulas, apresentações, pitches e frameworks.
> Reúne o que foi aprendido em: `260614-awake-grove` (20 templates), `260615-sunny-dolphin` (29 slides Academia de IA), `260615-awake-creek` (PDF export) e `260623-misty-lake` (29 slides Gestão e Estratégia).

> Para prosa e exemplos, ver `playbook.md` (mesma pasta). Este arquivo é só regras.

---

## Regra de ouro
**UM slide por vez.** Criar/editar → validar visualmente → só então passar ao próximo.
Nunca editar/criar vários slides em lote. Nunca confiar em screenshot headless do Chrome (decodifica imagem tarde demais) — abrir no navegador real ou pedir print ao usuário.

---

## Biblioteca `deck-frameworks/`

`deck-frameworks/` é a biblioteca especializada para slides em que **o modelo visual é o conteúdo** — ciclos, sistemas, camadas, mapas conceituais, modelos de decisão e ferramentas estratégicas customizadas.

### Quando usar

- Use `deck-frameworks/` quando a mensagem depende de relações espaciais, loops, níveis, eixos ou conexões próprias.
- Use `templates-short-deck/` ou `templates-expanded-deck/` para gráficos, tabelas, agendas, quotes, capas e layouts editoriais comuns.
- Não transforme qualquer lista em framework: se a geometria não explica uma relação, prefira um layout de conteúdo.

### Como explorar e estender

1. Abra `deck-frameworks/index.html` e escolha o modelo geometricamente mais próximo.
2. Leia `deck-frameworks/GUIA.md` e o comentário de geometria no topo do HTML escolhido.
3. Copie o template para o projeto; não sobrescreva o original com conteúdo específico.
4. Troque copy e labels antes de alterar estrutura.
5. Se alterar estrutura, recalcule e documente raios, ângulos, coordenadas, limites e conectores.
6. Valide no navegador real, um slide por vez.
7. Só adicione ao catálogo oficial um framework reutilizável; nesse caso, registre-o em `deck-frameworks/index.html` e no `GUIA.md`.

### Regras de geometria

- Linhas e setas terminam em elementos reais; conectores não podem flutuar.
- A ordem visual deve continuar legível sem animação.
- Labels não podem depender apenas de cor; use número, nome ou posição explícita.
- O framework deve continuar editável em HTML/CSS/SVG — não rasterize o diagrama inteiro.
- Um único protagonista gold por slide; as demais partes usam neutros e hierarquia tipográfica.

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

**Safety net (v4)**: no `.mode-dark`, os tokens crus de texto/linha também flipam (`--ink`→navy-50, `--ink-2`→navy-100, `--muted`→navy-200, `--rule`→rule-dark). Slide copiado do light com `var(--ink)` não imprime mais preto sobre navy. **Exceção**: texto escuro sobre painel dourado/paper dentro de slide dark deve usar `var(--on-accent)` (gold) ou hex explícito `#0F1419` (paper) — nunca `var(--ink)`.

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

## Lista dos 48 templates (20 canônicos + 5 custom + 9 do founder-ia + 14 da expansão v4 × light/dark)

### 20 templates canônicos (com variantes light/dark em arquivos separados)

| # | Template | Tipo | Modo default | Notas |
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

**Cada template 01-20 tem versão `-dark.html`** (ex: `01-capa-dark.html`, `02-palestrante-dark.html`, etc) com `class="slide mode-dark"`. Total: **20 templates × 2 modos = 40 arquivos**.

### 5 templates custom (extraídos dos decks reais, com variantes light/dark)

| # | Template | Tipo | Notas |
|---|----------|------|-------|
| 21 | 2-boxes | Provocação | 2 cards grandes (ex: "Por esporte" vs "Como profissional") com headline + sub-texto. Baseado no slide 02 do deck Gestão. |
| 22 | Mixed grid | Comparação complexa | 4 quadrantes com tipos diferentes (cards / bento / matriz 2x2 + lista lateral). Baseado no slide 22 exemplo-marketing. |
| 23 | Custom 2-col | Headline + corpo | Headline + sub-título à esquerda, corpo + cards à direita. Baseado no slide 11 callback. |
| 24 | Pergunta CTA | Pergunta de transição | Eyebrow + h1 grande + sub-texto + seta opcional. Baseado no slide 09 pergunta-transicao. |
| 25 | Hero com logo G4 | Capa alternativa | Header com logo G4 + hairline dourada + tag "Para quem quer mais" + título hero + barra dourada. Baseado no slide 01 capa e slide 24 divisor. |

### 9 templates custom adicionais (extraídos do deck founder-ia-conteudo, 2026-07)

| # | Template | Tipo | Modo | Notas |
|---|----------|------|------|-------|
| 26 | Quote galeria split | Citação com moldura | light + dark | Split 50/50: imagem em moldura "mat de galeria" (gradiente + keyline dourada) à esquerda, citação serif grande à direita. Diferente do 03 (retrato pequeno 340×420 + citação ao lado) — aqui a imagem ocupa 50% do canvas. Baseado nos slides 02/08 (provocação/referência). |
| 27 | Mentor hero | Bio + retrato grande | light + dark | Retrato 38% à direita + nome gigante (140px) + bio em blocos separados por hairline + signoff mono. Diferente do 02-palestrante (nome 108px, bio em 1 parágrafo corrido) — tipografia maior e bio estruturada em blocos. Baseado nos slides 03/14 (mentor / few-shot learner). |
| 28 | Transição com aceleradores | Transição + lista | light + dark | Rail estreito (280px) com eyebrow + label-sub à esquerda; H1 + body + fileira de 4 itens numerados com hairline no topo à direita. Bom pra "o que vem a seguir". Baseado no slide 04 (transição). |
| 29 | Bento comparativo | Comparação em mosaico duplo | light + dark | DOIS bentos internos lado a lado (1 hero + 2 células menores cada), com group-label acima de cada um — compara "lado A" vs "lado B". Diferente do 18-bento (1 mosaico só) e do 22-mixed-grid (matriz 2×2 + painel). Baseado no slide 05 (onde a IA ajuda). |
| 30 | Grid de ferramentas | Grid 4 colunas descritivo | light + dark | 4 colunas com índice + nome grande + descrição + tag mono (empurrada ao fim com margin-top:auto) + faixa gold de takeaway no rodapé. Diferente do 10-stats (números puros) — aqui o conteúdo é descritivo, não numérico. Baseado no slide 09 (pilha de ferramentas). |
| 31 | Narrativa numérica | 3 colunas editoriais | light + dark | Cada coluna: hero-num (dado/símbolo) + headline com 1 `<em>` + parágrafo explicativo. Fecha com takeaway centralizado. Diferente do 10-stats (métrica + label curto) — aqui ensina um conceito em 3 passos. Baseado no slide 10 (métricas). |
| 32 | Bento de métricas | Mosaico 3×3 assimétrico | light + dark | 6 células de tamanhos variados numa grade 3×3, cada uma com kicker + headline + sub + 1 bignum. Diferente do 22-mixed-grid (matriz 2×2 + painel lateral). Bom pra breakdown de entregáveis (ex: 70/20/10). Baseado no slide 13 (entrega do exercício). |
| 33 | Três pilares percentuais (dark) | Manifesto / regra de alocação | dark | 3 eixos lado a lado (não empilhados) com hairline vertical entre eles, cada um com um número/percentual gigante em gold. Diferente do 14-tres-pilares (linhas horizontais empilhadas, light). Baseado no slide 14 (70/20/10). |
| 34 | Encerramento quote (dark) | Fechamento com citação | dark | Quote serif grande centralizada + atribuição mono + caixa de CTA com hairlines gold acima/abaixo + marca centralizada no topo (espelha a capa). Diferente do 15-encerramento (hero + rail de contato, light). Baseado no slide 16 (encerramento). |

### 14 templates da expansão v4 (2026-07 — gráficos, imagens, quotes, comparação, sequência)

| # | Template | Tipo | Modo | Notas |
|---|----------|------|------|-------|
| 35 | Gráfico de linha | Dados / tendência | light + dark | Único gráfico em SVG inline (polyline + dots + gridlines dashed); série base em `--fg`, último segmento/ponto + valor final em accent; coluna editorial de insight à direita. Coordenadas comentadas com a conversão valor→y. |
| 36 | Gráfico donut | Dados / composição | light + dark | Donut via `conic-gradient` (percentuais comentados), furo central com `::after` em `--bg` + número grande; segmentos neutros via `color-mix(--fg, --bg)`, 1 fatia em accent; legenda com hairline-top à direita. |
| 37 | Barras duplas | Dados / antes-depois | light + dark | Barras verticais agrupadas, 2 séries × 4 categorias; série "Antes" em `--fg-muted`, série "Com IA" em accent; legenda mono no topo; técnica do 16 (val dentro do `.stem`, alturas px comentadas). |
| 38 | Barras de progresso | Dados / adoção-share | light + dark | 4-5 barras horizontais: label mono + track `--bg-2` + fill px pré-calculado + valor %; só a linha mais importante em accent; nota "como ler" no rodapé. |
| 39 | Imagem full + overlay | Imagem hero | **dark (único)** | Foto full-bleed 1600×900 + overlay `linear-gradient(to top, rgba(0,11,21,0.92), …)` + eyebrow/título/caption ancorados na base esquerda. Comentário no HTML documenta como trocar o placeholder por foto real. Portado do padrão de overlay do deck founder-ia. |
| 40 | Imagem hero lateral | Imagem + tese | light + dark | Imagem full-bleed lateral direita 38% (topo a base, sem moldura) com `.edge-blend` de 120px (`linear-gradient(to right, var(--bg), transparent)`) fundindo com o fundo; esquerda com título display 100px + lede + bloco hairline. Portado do slide 03-mentor do deck founder-ia. |
| 41 | Galeria duo | Imagem / evidências | light + dark | Duas molduras "mat de galeria" (gradiente + keyline dourada, técnica do 26) lado a lado com legendas mono (Fig. 01/02); bom pra antes/depois visual. |
| 42 | Quote de post/tweet | Citação / evidência | light + dark | Post do LinkedIn/X reproduzido em bloco com border hairline (sem sombra): avatar circular 56px + nome/handle + texto 32px + meta mono; coluna direita de contexto editorial "por que importa". |
| 43 | Quote dupla | Citação / contraste | light + dark | Duas citações lado a lado com vrule central e aspa decorativa grande em cada lado; atribuição do lado defendido em accent. |
| 44 | Tabela comparativa | Comparação / matriz | light + dark | Grid 4 col × 5 linhas com técnica bento (gap 1px sobre `--hairline`); header mono uppercase; coluna recomendada com `border-top: 2px solid var(--accent)`; marcadores tipográficos ● ○ — com legenda. |
| 45 | Checklist fazer × evitar | Comparação / prática | light + dark | Duas colunas: "o que funciona" (+ mono) vs "o que evitar" (— mono muted); itens separados por hairlines; barra accent só no header positivo. |
| 46 | Funil | Dados / conversão | light + dark | 4 estágios em barras horizontais decrescentes (larguras px comentadas), tons via `color-mix`, estágio final em accent; coluna direita com taxa total + insight. |
| 47 | Exercício em passos | Sequência / dinâmica | light + dark | 6 passos em grid com numeral 40px + tag de tempo mono ("5 min"); passo atual com numeral accent; rodapé "6 passos · 45 min · entrega". Portado do slide 12-exercicio do deck founder-ia. |
| 48 | Número hero | Dados / takeaway | light + dark | Um número gigante (240px) assimétrico à esquerda com sufixo em accent + coluna direita com parágrafos hairline + fonte do dado. |

**Total no repo**: 48 templates → **92 arquivos** (91 `.html` + `style.css`). Têm par light/dark todos exceto os dark-únicos (08, 20, 33, 34, 39).

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
- **Os darks v3 são o caso clássico de "token cru não flipa"** — 20 variantes dark usavam `color: var(--ink)` (token cru, #0F1419) achando que flipava no `.mode-dark`. Só os tokens semânticos (`--fg`, `--bg`…) flipavam → letra preta sobre navy. Corrigido com safety net no style.css (tokens crus agora flipam também) + `var(--on-accent)` para texto sobre painel dourado.
- **`Cormorant Garamond` agora é carregada pelo `style.css`** (junto das 3 famílias). Antes, os templates 26/34/43 declaravam a serif sem carregá-la → fallback genérico feio. Não precisa mais de `<link>` extra no slide.
- **Eyebrow local ≠ `data-section`** — os dois não podem dizer a mesma coisa (redundância visível no canto do slide). `data-section` = seção do deck; eyebrow = tema do slide.
- **Template 30 é o caso clássico de "eyebrow local em cima do data-section"** — o `data-section` renderiza via `.slide::before` em `top:48px; left:var(--pad)`. Nenhum elemento local pode ocupar essa faixa; eyebrows locais começam em `top:96px`.
- **Template 31 é o caso clássico de "orçamento de accent estourado por repetição"** — 3 colunas iguais com número gold cada = 3 unidades de accent. Em layouts repetidos, só a coluna/célula líder (`.lead`) leva accent; as demais ficam em `--fg`.
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

- **Catálogo canônico de 52 templates Órbita (curto)**: `templates-short-deck/` (local — vide README) + [`templates-short-deck/GUIA.md`](templates-short-deck/GUIA.md)
- **Catálogo canônico de 109 templates Órbita (expandido)**: `templates-expanded-deck/` (local — vide README) + [`templates-expanded-deck/GUIA.md`](templates-expanded-deck/GUIA.md)
- **Biblioteca especializada de frameworks Órbita**: `deck-frameworks/` + [`deck-frameworks/GUIA.md`](deck-frameworks/GUIA.md)
- **Variantes completas de identidade**: [`id-next/README.md`](id-next/README.md), [`id-scale/README.md`](id-scale/README.md) e [`id-club/README.md`](id-club/README.md)
- **Acervo v4 (48 templates hairline, congelado)**: `templates-legacy/`
- **Catálogo navegável** (grid com filtro por categoria + toggle light/dark): `examples/catalog.html` — abrir via servidor local (`python3 -m http.server` na raiz) por causa dos iframes
- **Playbook narrativo** (prosa + exemplos): `playbook.md` (mesma pasta)
- **Passador de slides** (exemplo/base do build): `examples/index.html`
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