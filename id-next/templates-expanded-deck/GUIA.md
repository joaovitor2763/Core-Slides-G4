# Core Slides G4 · expanded-deck "Órbita" — Guia de uso e edição

> Referência completa para **quem (humano ou IA) vai copiar, editar e criar slides** com esta biblioteca.
> Leia as seções 1–4 antes de tocar em qualquer arquivo. O catálogo (seção 5) diz quando usar cada slide e o que editar nele.
> O `expanded-deck` (109 templates) é uma extensão do `short-deck` (52 templates) — mesmo design system, mesmo canvas, mais opções. O `index.html` desta pasta agrupa por categoria (filtros no topo).
> **Copy = Lorem Ipsum por design**: o texto dos templates é placeholder calibrado ao layout — os COMPRIMENTOS fazem parte do design. Números, %, moedas, datas e labels de eixo são dados de exemplo amarrados à geometria dos gráficos (escalas comentadas). Ao usar: troque o lorem por conteúdo de comprimento parecido; se mudar um número de gráfico, recalcule o px pela escala comentada. Nos slides 101–109, comentários HTML (`<!-- ex.: … -->`) dizem o que vai em cada região.

---

## 1. Mecânica do canvas (igual em TODOS os slides)

- Canvas fixo **1600×900** (16:9). Nada de `vw/vh/%` no conteúdo — tudo em `px` absolutos.
- Estrutura obrigatória de cada arquivo:

```html
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>NN · Nome</title>
<link rel="stylesheet" href="style.css?v=5.2" />   <!-- manter o ?v= (cache-buster) -->
<style>/* CSS local do slide — sempre consumindo var(--…) */</style>
</head>
<body>
<div class="stage">
  <article class="slide" data-section="Metadado">   <!-- + classe mode-dark se dark -->
    <!-- conteúdo posicionado com position:absolute e px -->
  </article>
</div>
<script>
  const slide = document.querySelector('.slide');
  function fit(){
    const s = Math.min(innerWidth / 1600, innerHeight / 900);
    slide.style.transform = `translate(-50%, -50%) scale(${s})`;
  }
  addEventListener('resize', fit); fit();
</script>
</body>
</html>
```

- `data-section` é **só metadado** (busca/organização). NÃO renderiza nada. O único kicker visível é o `.eyebrow`.
- Padding externo: `var(--pad)` = 96px. Conteúdo vive entre x 96–1504 e y ~96–804 (sangrias decorativas são exceção intencional).
- **Valide somas de px antes de salvar**: larguras de colunas + gaps devem fechar em 1408 (=1600−192); nada de conteúdo além de y=804.
- Ao criar slide novo: registre no array `slides` do `index.html` (`{file, name}`).

## 2. Design system (style.css)

### Tokens
Modo light é o default; `class="slide mode-dark"` re-escopa tudo. **Nunca** use hex de texto direto — sempre tokens:

| Token | Light | Dark | Uso |
|---|---|---|---|
| `--bg` | paper #F5F4F3 | navy #001525 | fundo do slide |
| `--surface` | #FFF | rgba(255,255,255,.045) | cards |
| `--surface-2` | #EFEDE9 | rgba(255,255,255,.08) | chips, tracks |
| `--text-1/2/3` | navy escuro → slate | ice → slate claro | título / corpo / muted |
| `--text-ghost` | rgba .13 | rgba .10 | linha-eco fantasma |
| `--border`, `--border-2` | rgba navy .09/.16 | rgba branco .09/.16 | bordas, baselines |
| `--gold` | #B9915B | #C9A05C | acento único |
| `--gold-dim/-border` | rgba gold | rgba gold | chips/fundos dourados |
| `--green/--red` (+`-dim`) | escuros | claros | deltas positivos/negativos |
| `--on-gold` | #FFF | #1A1300 | texto sobre gold |

### Tipografia (4 papéis — nunca misturar)
- `--serif` **Playfair Display** → títulos (`.h-serif`), quotes, ghost. Itálico gold no `<em>` = palavra-chave.
- `--num` **Space Grotesk** → TODO número (`.num`), nomes de card, labels fortes. Número NUNCA em serif.
- `--sans` **IBM Plex Sans** → corpo (`.lede` 21px, `.body` 17px, `.small` 14px).
- `--mono` **IBM Plex Mono** → `.eyebrow`, `.mono-label`, dados de eixo, kickers.

### Componentes prontos
- `.surface` (radius 22 + borda + sombra) · `.surface--flat` (sombra leve) · `.surface--gold` (destaque; use em **1** card por slide).
- `.chip` pill mono · `.chip--gold` · `.chip--green` · `.chip--red` · `.chip .dot` (bolinha).
- `.cta` — botão pill gold. Secundário: pill outline manual (`border:1px solid var(--border-2); border-radius:999px`).
- `.eyebrow` — kicker mono com traço gold. Um por slide, acima do título.
- `.ghost` — texto serif gigante quase invisível (números de capítulo, eco de título).
- `.grain` — ruído de filme (só em slides dark de respiro).
- `.armilar--engraving` — gravura da esfera armilar (ver §3.1).

### Regras invioláveis
1. **Ouro com parcimônia**: 1 protagonista gold por slide (em do título OU número-hero OU card gold). Chips de apoio ok.
2. **PROIBIDO** `.glow`/halos radiais difusos, emoji, ícone de biblioteca externa, hover nos slides.
3. Ícones: inline SVG stroke 1.8px 24×24 dentro de disco 48px (ver 43-cards-icones.html).
4. Título nunca centralizado, exceto divisores/encerramento. Assimetria sempre.
5. Slides dark: tokens fazem tudo — não escreva cor de texto hardcoded (exceção: texto escuro sobre painel gold/paper = `var(--on-gold)` ou hex `#0F1419` comentado).

## 3. Padrões de código (copie destes arquivos)

### 3.1 Gravura armilar no canto inferior direito
Assinatura visual dos slides de respiro. A arte do PNG ocupa o canto direito/inferior do arquivo — por isso as bordas do PNG devem coincidir com as bordas do canvas (right/bottom levemente negativos). **Nunca** deixe uma borda do PNG no meio do slide (corte duro visível).

```css
.armilar--corner{width:780px;height:439px;right:-30px;bottom:-30px;opacity:.26}
/* dark: opacity .20–.28 · light: .45–.55 (o tom slate é mais claro no paper) */
```
```html
<div class="armilar armilar--engraving armilar--corner" aria-hidden="true"></div>
```
Onde usar: capa, divisores, mentor, encerramento, quotes de respiro. Onde NÃO usar: slides densos (gráficos, tabelas, grids) — esses ficam limpos.

### 3.2 Gráfico de barras (06, 41)
- Card `.surface` envolve o chart. Baseline firme: `::after` 2px `var(--border-2)`.
- Categorias ABAIXO da baseline com altura fixa (`height:12px;line-height:12px` + margin-top:18 → baseline em `bottom:30px`).
- Alturas **pré-calculadas em px com comentário da escala**: `/* 100% = 250px · 81% = 203px */`.
- Barra destaque: `linear-gradient(180deg,var(--gold-300),var(--gold-500))`, radius só no topo, **sem sombra** (vaza sob a baseline).
- Gridline de referência: `::before` com `repeating-linear-gradient` dashed + tick mono.

### 3.3 Linha SVG (07, 42)
- `path` com curvas `C` (controles a ±102px dos pontos — nunca polyline dura).
- Conversão comentada: `/* y = 280 − valor·3,25 */`. Área sob a linha: `linearGradient` gold→transparente.
- Série secundária: stroke `var(--text-3)` 2px `stroke-dasharray="6 8"`.
- Valor final `.num` ao lado do último ponto; halo no dot final.

### 3.4 Pizza/donut (08, 17) e anel (23)
- `conic-gradient` com **percentuais comentados**; furo = círculo interno com `background:var(--bg)` (ou cor do surface).
- Tons neutros: `rgba(0,31,53,.16/.11/.07)` (light). 1 fatia gold.
- Anel segmentado (23): conic de 4 segmentos + furo; rotação via `from Xdeg`.

### 3.5 Conectores de diagrama (23, 33, 34, 36, 38)
Padrão obrigatório — linhas nunca "flutuam":
```svg
<line x1=… y1=… x2=… y2=… />          <!-- stroke var(--text-3), width 1.2, opacity .55 -->
<circle class="dot-co"  cx=… cy=… r="3"/>   <!-- ponta no texto -->
<circle class="dot-ring" cx=… cy=… r="5"/>  <!-- ponta no diagrama, na borda EXATA -->
```
Coordenadas calculadas e comentadas (cos/sin para círculos: `centro + R·(sin θ, −cos θ)`).

### 3.6 Placeholders de imagem
Nenhum slide usa foto externa. Para trocar por foto real, cada arquivo tem comentário `<!-- para usar foto real: … -->`:
- Retrato (03, 29): substituir o div de iniciais por `<img src="…" style="width:100%;height:100%;object-fit:cover">` dentro do frame.
- Foto full (13): idem, no `.canvas` (remover a hachura `::before`).
- Mockup (25): trocar a `.ui` fake por `<img>` de screenshot dentro da `.screen`.

### 3.7 Cronograma (37), tabela (40), matriz (20)
- 37: colunas por dia com faixas horárias tracejadas atrás (z-index 0) e cards na frente.
- 40: `<table>` real; zebra `rgba(0,31,53,.025)`; TOTAL com `border-top:2px`; coluna-chave com números gold.
- 20: quadrantes `.surface--flat` + eixos com seta CSS + labels mono rotacionados (`writing-mode`/`transform`).

### 3.8 Split misto — painel navy dentro de slide light (27, 57, 58, 60, 62)
O `<article>` fica **light**; o painel navy é um `<div class="… mode-dark">` interno com `background:var(--navy-700)` manual — a classe re-escopa todos os tokens dentro dele. Nunca inverta (article dark com painel paper interno tende a vazar token). Pill/costura na divisa: ver 27-split.

### 3.9 Barras posicionadas em régua (81 ponte, 82 metas, 100 gantt)
Toda barra flutuante/posicionada tem `left/width/bottom` **pré-calculados em px com a régua comentada** (`/* 1 semana = 103px */`, `/* 1M = 22px */`). Waterfall: positivo = `var(--green-dim)` + border green, negativo = `var(--red-dim)` + border red, colunas cheias de abertura/fechamento em navy/gold; conectores tracejados ligam os acumulados.

### 3.10 Heatmap (99)
Células com `background:rgba(0,31,53,α)` e α por faixa de intensidade comentado (.04/.08/.14/.22/.32). Valor legível: células escuras (α ≥ .22) usam `#F5F4F3` (comentado); célula líder em gradiente gold com `var(--on-gold)`.

## 4. Light ou dark? (decisão rápida)

- **Dark** = momentos de palco: capa, divisor, mentor/equipe, quotes, encerramento, KPIs-hero, pricing, mockup, frameworks conceituais (camadas, triângulo, polos, radar, concêntricos).
- **Light** = trabalho e leitura: gráficos de dados, tabelas, agendas, checklists, roadmaps, matrizes, bentos de conteúdo, prova social.
- Um deck real alterna: abre dark → blocos de conteúdo light → divisor dark → … → fecha dark.

## 5. Catálogo — quando usar e o que editar

### 5.0 Qual template usar? (desambiguação rápida)

Vários templates parecem primos. A régua para escolher:

| Você quer mostrar… | Use | Não confunda com |
|---|---|---|
| Uma frase de efeito, só | **30** quote mínima | 66 (tem estrutura de debate), 47 (lista) |
| As perguntas que a aula responde | **47** perguntas | 66 (debate), 71 (quiz com resposta) |
| Um debate com a turma dividida | **66** dois lados | 32 (fazer×evitar é prática, não opinião) |
| Checagem de aprendizado com gabarito | **71** quiz | 47 (não tem resposta) |
| Composição de um todo (fatias) | **08** donut (simples) ou **17** pizza (legenda rica) | 44 (mix MUDANDO no tempo) |
| Conversão etapa a etapa | **15** funil | 89 (TAM/SAM/SOM é nesting, não conversão) |
| Tamanho de mercado | **89** barras aninhadas ou **35** círculos | 15 (funil implica perda) |
| Priorização (fazer primeiro) | **20** matriz 2×2 | 86 (riscos), 92 (posicionamento vs concorrentes) |
| Riscos por probabilidade × impacto | **86** mapa de riscos | 20, 92 |
| Nós vs concorrentes em 2 eixos | **92** posicionamento | 20, 86 |
| Marcos no tempo (o que aconteceu) | **21** timeline · **76** versão para case | 46 (fases futuras), 100 (semanas com donos) |
| Plano futuro por fases | **46** roadmap | 100 (gantt = barras por semana), 37 (horas × dias) |
| Cronograma de execução com donos | **100** gantt | 46, 37 |
| Agenda de um evento de 1–2 dias | **37** cronograma · **53** programa dois dias | 05 (agenda de aula) |
| Um ano de programa/contrato | **62** plano anual | 46, 100 |
| Antes × depois em números | **10** (2 cards) · **75** (grid de 6 métricas) | 27 (split narrativo), 41 (barras) |
| Um conceito para ensinar | **64** (com prova numérica) · **51** (com ilustração) · **39** (manifesto) | 30 |
| Quem é a pessoa | **03** mentor (1) · **49** equipe (4) · **61** galeria (3 retratos) | 57 (módulo + mentores juntos) |
| Depoimentos | **50** prova social (clientes) · **55** vozes (como descrevem o produto) · **29/04/60** (1 quote forte) | — |
| KPIs / métricas | **09** stats (4) · **45** grid dark (painel) · **79** resumo executivo (KPIs + leitura) | 75 (antes→depois) |
| Processo linear com movimento | **104** seta (etapas dentro de uma seta) | 12 (grade de passos), 21 (marcos no tempo) |
| Framework de N pilares | **105** pentágono (conceito + transversal) · **24** camadas · **38** triângulo | 18 (radar é DADO, 2 séries) |
| Duas séries no mesmo gráfico | **109** combo (barras + linha) | 41 (2 séries de barras), 42 (2 linhas) |
| Funil | **15** vertical (conversão) · **108** horizontal (jornada de valor + base transversal) | 89 |
| Portfólio de ofertas | **106** por maturidade · **107** por área × horizonte | 48 (pricing) |
| Quem conduz | **03** (1) · **103** (2 espelhados) · **49** (4) · **61** (3 retratos) | — |
| Para quem é (ICP) | **102** público-alvo | 63 (objetivos de aula) |
| Agenda de fases de programa | **101** (sub-cards por fase) | 05 (aula), 37 (horas×dias), 53 (2 dias) |

### 5.1 Como editar sem quebrar (receita)

1. **Nunca edite o template no lugar** — copie (`cp NN-nome.html meu-slide.html`) e edite a cópia; os 100 arquivos desta pasta são a biblioteca de referência.
2. **Leia o comentário de topo do arquivo antes de mexer** — ele é o mapa: toda conta de px (colunas, gaps, escalas de gráfico, coordenadas de conector) está lá. Se mudar um tamanho, **recalcule e atualize o comentário**.
3. **Troque só copy e dados primeiro.** Estrutura (classes, tokens, skeleton do §1) fica intacta. Nunca escreva hex de texto: use `var(--…)` (§2).
4. Em gráficos: os valores visuais são **px pré-calculados** — mudar o número no texto sem recalcular a barra/altura gera slide mentiroso. Siga a escala comentada (§3.2–3.4, §3.9).
5. Em diagramas: mover um elemento exige recalcular os conectores (dots ancorados na borda EXATA — §3.5).
6. Respeite o orçamento de gold (§2, regra 1): se o seu conteúdo pede outro destaque, MOVA o gold, não adicione um segundo.
7. **Renderize e olhe** (checklist §6, item 9) antes de dar por pronto. Se criou arquivo novo, registre no array `slides` do `index.html` com a categoria certa.

Formato do catálogo abaixo: **quando usar · o que editar · nota técnica**.

| # | Slide | Uso · edição · notas |
|---|---|---|
| 01 | Capa | Abertura. Edite: eyebrow, título (em gold na expressão-chave), sub, chips de meta, data. Logo via `assets/g4-logo-branca.svg`. |
| 02 | Divisor dark | Troca de capítulo. Edite: chip "Parte N", título, ghost `02` (número do capítulo, 330px, sangra à direita de propósito). |
| 03 | Mentor | Quem conduz. Edite: nome (sobrenome em `<em>` gold), cargo mono, bio 2 frases, 3 chips, iniciais do retrato. |
| 04 | Quote editorial | Fala + dado que a valida. Edite: quote serif, avatar-iniciais, card lateral (número `.num` + caption + chip). |
| 05 | Agenda | Roteiro da aula. Edite: 4 itens (nome, sub, chip duração); o item atual leva `.surface--gold` + chip--gold "agora". |
| 06 | Gráfico de barras | 1 série, 2–5 categorias. Edite valores/alturas seguindo o comentário de escala (§3.2). Recalcule sempre. |
| 07 | Gráfico de linha | Tendência 1 série. Edite pontos do path pela fórmula comentada (§3.3). |
| 08 | Donut | Composição (3–5 fatias). Edite conic-gradient (% comentados) + legenda em mini-cards. |
| 09 | Stats | 4 métricas. Edite números/labels/chips de tendência; a protagonista fica no `.surface--gold`. Título com linha-eco `.ghost`. |
| 10 | Antes × depois | Contraste 2 cards. Edite número apagado (antes) vs gold (depois) + 3 bullets "+". |
| 11 | Bento | Mosaico hero + 3 células. Edite bignum gold, claim serif e células de apoio. |
| 12 | Método em passos | 4 passos com output. Edite numerais serif, nomes, descrições e chips "→ entrega". Passo atual = gold. |
| 13 | Imagem hero | Foto de caso. Edite título/lede/chips; troque placeholder por foto (§3.6). Rotação -1.2deg é intencional. |
| 14 | Tabela de decisão | Critérios × opções, uma recomendada (coluna gold-dim + chip). Marcadores ✓/○/—. |
| 15 | Funil | 4 estágios decrescentes. Larguras px comentadas; último estágio gold; card lateral com taxa total. |
| 16 | Encerramento | Fechamento com CTA. Edite quote, atribuição, texto do `.cta` e contatos do rodapé. |
| 17 | Pizza | Composição com legenda rica (valor + share). Mesmo esquema do 08. |
| 18 | Radar | Capacidades hoje × meta (5 eixos, SVG). Edite os polygons pelas coordenadas comentadas; série meta = gold. |
| 19 | Barras de progresso | % por item em tracks pill. Fills px comentados; líder em gold. |
| 20 | Matriz 2×2 | Priorização em eixos. Edite labels dos eixos, 4 quadrantes; o recomendado = gold + chip "comece aqui". |
| 21 | Timeline | Marcos no tempo. Cards alternam acima/abaixo do trilho; marco atual = dot gold com halo. |
| 22 | Fluxo ramificado | Pipeline/árvore de processo. Edite pills e as curvas bézier comentadas; raiz = gold. |
| 23 | Ciclo | Loop de 4 etapas (anel conic + callouts). Conectores no padrão §3.5; etapa crítica = segmento + callout gold. |
| 24 | Framework camadas | Stack/pirâmide 4 níveis. Larguras crescentes (480→1080); base = gradiente gold. |
| 25 | Mockup laptop | Produto/tela. Troque a UI fake por screenshot (§3.6). |
| 26 | Bento claro | Mosaico light com célula hero + 3 apoios. |
| 27 | Split | Antes/depois literal: metade navy (div interno com `mode-dark`) + metade paper + pill "→" na divisa. |
| 28 | Venn | 3 condições que se cruzam. Círculos com fills translúcidos; interseção = dot gold + label. |
| 29 | Quote com foto | Depoimento forte. Retrato placeholder + quote serif 54px + chip de resultado. |
| 30 | Quote mínima | Frase de efeito só. O slide mais vazio do deck — não adicione nada. |
| 31 | Divisor claro | Espelho light do 02. Ghost do capítulo + gravura no canto. |
| 32 | Checklist | Fazer × evitar (dots verdes "+" vs vermelhos "—"). |
| 33 | Polos | 2 sistemas comparados (círculo neutro vs gold) com spokes radiais + seta tracejada. Spokes: coordenadas comentadas. |
| 34 | Ciclo de setas | Loop com movimento (4 arcos SVG com pontas de seta). Ângulos/arcos comentados. |
| 35 | Círculos concêntricos | TAM/SAM/SOM ou qualquer aninhamento. 3 círculos tangentes na base; alvo interno = gold. |
| 36 | Árvore | Hierarquia/BSC: raiz pill + trave + 5 filhos (glyphs tipográficos, NUNCA emoji); filho-chave = gold. |
| 37 | Cronograma | Agenda multi-dia (colunas + faixas horárias). Blocos gold-dim = momentos especiais. |
| 38 | Triângulo | Trade-off de 3 forças. Vértices dot gold + callouts; labels de aresta rotacionados; centro serif itálico. |
| 39 | Manifesto | Texto puro serif 46px com 2 `<em>` gold + 3 notas numeradas. Sem cards. |
| 40 | Tabela de dados | Números por área com TOTAL. §3.7. |
| 41 | Barras comparativas | 2 séries × 4 categorias (antes neutro / depois gold). Escala comentada. |
| 42 | Linhas competindo | 2 trajetórias divergindo; chave vertical marca o gap ("+46 pts"). |
| 43 | Cards com ícones | 3 alavancas com texto denso + ícones SVG stroke; card central gold. |
| 44 | Empilhadas 100% | Mix mudando por período; segmento gold cresce. Larguras somam 1000px/linha (comentado). |
| 45 | Grid de KPIs | Painel 2×2 dark; KPI protagonista gold; chips de delta. |
| 46 | Roadmap | 3 fases com marcos; fase atual gold + chip "agora"; setas → entre colunas. |
| 47 | Perguntas | Q1–Q4 serif itálico + resposta-síntese; a pergunta em foco tem bloco gold-dim. |
| 48 | Planos | Pricing 3 tiers; o do meio gold, elevado, com `.cta` cheio; laterais com pill outline. |
| 49 | Equipe | 4 mentores (avatar iniciais; fundador com avatar gold) + chip de credencial. |
| 50 | Prova social | 3 depoimentos com resultado medido em chip--green; central gold. |
| 51 | Conceito + imagem | Ensinar um conceito em camadas: 3 blocos (kicker mono + body), o último em painel gold-dim de borda uniforme, e ilustração vertical 3:4 à direita (placeholder → troque por imagem real, ver comentário no arquivo). |
| 52 | Exercício prático | Atividade em passos: grade 3×2 de cards (Passo NN gold + tempo mono + título + descrição) e painel-resumo no topo direito (tempo total `.num` + entregável). Melhor que lista vertical: preenche o canvas e o tempo fica colado no passo. |

### Expansão — Referências G4 (53–62)

| # | Slide | Uso · edição · notas |
|---|---|---|
| 53 | Programa dois dias | Encontro/imersão de 2 dias. Edite: chips de pilares (1º ativo gold), círculos Dia 1/Dia 2 (Dia 1 = gradiente gold), labels-satélite dos spokes, mini-cards de agenda nas laterais. Spokes com trig comentada (§3.5). |
| 54 | Hub de entregas | Tudo que o programa/produto entrega ao redor de um hub. Edite: nome/sub do disco central, as 8 pills + descrições (a âncora do programa = pill--gold), abraçando o anel com spokes CURTOS — as posições seguem a curvatura (trig comentada); se mover um item, recalcule pill + dot + âncora juntos. |
| 55 | Vozes de usuários | Como o público descreve o produto. Edite: título, retrato placeholder (§3.6), 4 claims entre aspas + explicações itálicas, ícones SVG dos discos (1º disco = gold). |
| 56 | Grid de casos de uso | Vitrine de casos por aplicação/área. Edite: rótulos rotacionados das bandas, 8 pares card-ícone + resultado concreto. UM card gold no slide inteiro. |
| 57 | Módulo de aula | Abertura de módulo de curso. Edite: chips de módulos (ativo = navy invertido), chip--gold "Módulo N", título itálico, 4 aprendizados, painel dark com 4 mentores (avatar iniciais). Split misto §3.8. |
| 58 | Custo da inação | Custo de não agir (pitch). Edite: pergunta serif da faixa navy, os 3 painéis (paper/gold/navy) com ícone + custo em `<b>`. O painel gold é o protagonista. |
| 59 | Convergência A×B | Dois mundos convergindo (founder × mentor, problema × solução). Edite: bloco-lede, 4 pills neutras (esq.), 4 pills gold-dim (dir.), rótulos das travas da moldura, palavra serif abaixo. Cotovelos SVG com dots comentados. |
| 60 | Perfil + quote | Por que X + autoridade que valida. Edite: título, 3 argumentos (2º com barra gold), retrato central (§3.6), quote serif + atribuição no painel navy. |
| 61 | Galeria de retratos | Time/mentores com categorias. Edite: título (em gold), 3 chips de categoria, nomes/cargos, placeholders de retrato (§3.6). |
| 62 | Plano anual | Programa/contrato ao longo de 12 meses. Edite: células M01–M12, as DUAS pistas (dots mensais + losangos trimestrais — as coordenadas dos centros estão comentadas), o retângulo gold do período especial + chip-callout, e os 3 cards-pilares da faixa paper. Split misto §3.8. |

### Expansão — Aulas & Educação (63–71)

| # | Slide | Uso · edição · notas |
|---|---|---|
| 63 | Objetivos de aprendizagem | Abertura de aula. Edite: 4 competências (claim + como pratica), card 01 = gold "aplicável amanhã", chip de duração no rail. |
| 64 | Conceito no número | Ensinar UM conceito e prová-lo com um exemplo trabalhado. Edite: termo (em gold), definição, a fala "como explicar para o time", e o card do exemplo — barras antes→depois com escala comentada (/* R$ 1M = 40px */), painel gold-dim do resultado e leitura final. Os números precisam fechar entre si. |
| 65 | Canvas de exercício | Worksheet projetável. Edite: 6 campos (kicker numerado + pergunta + dica), campo 01 = borda gold tracejada "comece aqui", chip de tempo. Bordas DASHED = affordance de preenchimento. |
| 66 | Debate · dois lados | Debate estruturado: a turma se divide em dois lados. Edite: pergunta (sem em gold — o VS gold é o protagonista), os 2 cards de argumentos (kicker + 3 itens '+'), a linha "ganha quando" ancorada na base de cada card, e os chips de mecânica. Não confundir com 47 (lista de perguntas) nem 30 (frase de efeito). |
| 67 | Recap · síntese | Fechamento de aula. Edite: 5 frases-síntese + porquês; linha 3 = gold-dim "a mais importante". |
| 68 | Biblioteca · leituras | Aprofundamento pós-aula: ESTANTE com 4 capas de livro sobre a prateleira. Edite: título/autor/meta de cada capa, as cores das capas (a recomendada = gradiente gold, texto `--on-gold`), chips de tipo sob a prateleira e os 3 passos de "como usar". A lombada é o `::before` — não remova. |
| 69 | Dinâmica de turma | Logística de dinâmica. Edite: painel-resumo (tempo total + entrega), 3 colunas de fase com tempos por item; "execução" = gold. |
| 70 | Escada de maturidade | Diagnóstico por níveis. Edite: 5 níveis (nome + descritor), qual leva o chip "você está aqui" (= gold). Alturas escalonadas comentadas; baseline contínua. |
| 71 | Quiz · checagem | Pergunta com resposta revelada. Edite: pergunta, 4 alternativas, qual é a correta (= gold + chip "resposta"), fonte no rodapé. |

### Expansão — Case Study (72–78)

| # | Slide | Uso · edição · notas |
|---|---|---|
| 72 | Abertura de case | Capa do caso. Edite: eyebrow do setor, nome da empresa (em gold), lede-resumo, 4 chips de contexto e a FAIXA DE STATS da base (hairline + 3 números espalhados na largura). Armilar + grain ficam. |
| 73 | Contexto do case | Situação → complicação → pergunta. Edite: os 3 blocos (numeral ghost + régua + kicker + texto); o 3º (a pergunta, serif itálico) leva a régua gold. Slide de conteúdo — sem armilar. |
| 74 | Desafio → intervenção | O nó × 3 frentes. Edite: card do nó (chip--red + sintomas), 3 frentes (kicker + ação + ferramenta); frente decisiva = gold. |
| 75 | Resultados do case | Grid 3×2 antes→depois. Edite: 6 métricas coerentes entre si (antes small + depois num + delta chip--green); a principal = gold. |
| 76 | Linha do case | Como aconteceu no tempo. Edite: posições/meses dos dots, cards alternados das fases, resultado no último dot (gold + halo). |
| 77 | Aprendizados do case | 3 lições editoriais. Edite: as 3 frases serif itálicas + "na prática"; só a 2ª leva `<em>` gold. |
| 78 | Evidência · documento | Prova documental. Edite: nome do arquivo, a linha destacada gold-dim (o dado), 3 callouts; troque o corpo fake por screenshot real (comentário no arquivo). |

### Expansão — Financeiro (79–86)

| # | Slide | Uso · edição · notas |
|---|---|---|
| 79 | Resumo executivo | Fechamento do mês em 1 página. Edite: 4 KPIs + chips de tendência (margem = gold), colunas "sustentou"/"atenção" (dots green/red). |
| 80 | DRE resumida | Tabela real vs plano. Edite: valores (a ARITMÉTICA precisa fechar — receita→EBITDA), chips de Δ; linha EBITDA = gold-dim. |
| 81 | Ponte · waterfall | De onde veio o crescimento. Edite: colunas (abertura navy, efeitos green/red, fechamento gold) — recalcule alturas/bottoms pela escala comentada; a soma precisa fechar. |
| 82 | Metas × realizado | Bullet bars YTD. Edite: 5 métricas (fill px na régua /* 100% = 700px */), marcador da meta fixo; a que mais superou = fill gold. Métrica invertida anotada. |
| 83 | Curva de caixa | Burn → breakeven → geração. Edite: path pela conversão comentada, posição do breakeven (dot gold), 3 números da direita. Área red-dim antes / gold depois. |
| 84 | Orçamento por área | Alocação anual. Edite: 5 segmentos da barra 100% (px somando 1408), valores por coluna (somam o total), chips vs ano anterior; área-destaque = segmento gold. |
| 85 | Cenários | 3 futuros. Edite: receita/margem/premissas/probabilidade por cenário; o BASE (meio, elevado) = gold "cenário-guia". |
| 86 | Mapa de riscos | Probabilidade × impacto. Edite: posições dos 6 discos (coordenadas comentadas), lista com mitigação; o risco na zona crítica = disco gold + item gold-dim. |

### Expansão — Pitch & Vendas (87–94; ver também 58)

| # | Slide | Uso · edição · notas |
|---|---|---|
| 87 | O problema · dores | 3 dores com custo. Edite: claims + sintomas + custo em `--red`; síntese na base com único `<em>` gold. SEM gold nos cards. |
| 88 | A solução | O que é → o que faz → o que muda. Edite: os 3 cards conectados; o 3º (resultado com número) = gold. |
| 89 | Mercado · TAM SAM SOM | Tamanho de mercado em barras aninhadas. Edite: valores e larguras (proporção ilustrativa comentada), definições mono; SOM = gold. |
| 90 | Modelo de receita | Motores de receita + unit economics. Edite: pills de oferta (a principal = gold-dim), % de mix e tickets, 4 mini-cards (CAC/LTV/payback coerentes). |
| 91 | Tração | Curva de crescimento com milestones. Edite: path pela conversão comentada, 3 milestones, número hero gold + chips NRR/churn. |
| 92 | Posicionamento | Scatter competitivo. Edite: eixos, 6 concorrentes (monogramas + labels), posição do disco G4 (gold, quadrante superior-direito). |
| 93 | A oferta | Âncora de valor × investimento. Edite: 6 itens com valores de referência (somam a âncora), preço no card gold + CTA + chip de escassez. |
| 94 | Próximos passos | Fechamento comercial com datas. Edite: 3 passos (nomes + datas concretas), contato no rodapé; passo 1 = gold "agora". |

### Expansão — Produto (95–100; ver também 25)

| # | Slide | Uso · edição · notas |
|---|---|---|
| 95 | Mockup celular | App mobile. Edite: bolhas do chat fake (ou troque por screenshot, comentário no arquivo), 3 features (disco da 2ª = gold), chip de status. Base do celular sangra o canvas de propósito. |
| 96 | Grade de features | 6 funcionalidades com ícones SVG próprios. Edite: nomes + descrições + ícones; célula 1 = gold. |
| 97 | Jornada do usuário | 5 etapas + curva de valor. Edite: labels das etapas, o que o produto faz em cada uma, posição do "momento aha" (dot gold + callout). |
| 98 | Arquitetura | Entrada → motor → saída. Edite: pills de entrada/saída, nome e módulos do core (border gold); setas alinhadas aos centros (coordenadas comentadas). |
| 99 | Heatmap de adoção | Áreas × meses. Edite: alphas das células pela legenda (§3.10), célula líder gold, card de insight. |
| 100 | Plano de trabalho · gantt | 4 frentes × 12 semanas. Edite: barras pela régua comentada (/* 1 semana = 103px */), fase atual = gold + chip "agora", linha "hoje", donos no rodapé. |

### Expansão — Referências G4 · rodada 2 (101–109)

| # | Slide | Uso · edição · notas |
|---|---|---|
| 101 | Fases do programa | Agenda de programa/consultoria em 3 fases. Edite: barra de cada fase, subtítulo e os DOIS sub-cards (compromisso + lista de informações/atividades); a fase-núcleo (meio) = `.surface--gold`. |
| 102 | Público-alvo | "Para quem é" (ICP) no pitch. Edite: título-pergunta, 2 parágrafos, os 4 tiles dark (ícone + label; tile 1 = faixa gold cheia) e a nota de alerta do rodapé. |
| 103 | Dois mentores | Dupla de mentores/palestrantes em metades espelhadas (dark/light). Edite: retratos (§3.6), nomes (só o sobrenome do mentor 1 em gold), chips de especialidade, linha de "logos" mono e as bios. Split misto §3.8. |
| 104 | Processo em seta | Ciclo/processo linear com movimento. Edite: os 6 labels sob os discos e qual disco é o atual (= gold). A seta é UM path SVG (corpo+cabeça) em gold-dim — não é o protagonista. |
| 105 | Pentágono de pilares | 5 pilares + 1 transversal (centro). Edite: pills + parágrafos dos 6 callouts; o dot central gold é o pilar que permeia os demais. Vértices por trig comentada; conectores com dots exatos (§3.5). |
| 106 | Jornada × programas | Portfólio mapeado por maturidade. Edite: bullets por estágio, pills do eixo, e as 4 barras de programa (ranges de coluna px comentados; a âncora = gold). Curva de fundo é decorativa. |
| 107 | Matriz de programas | Áreas × horizonte (estratégico/tático/operacional) com badge de programa por linha. Edite: labels, células (entrega por interseção) e badges (linha 1 = gold). Substitui a função do "sunburst" com legibilidade Órbita. |
| 108 | Funil horizontal | Jornada de valor em 3 estágios afunilando + base transversal. Edite: labels dos trapézios, pills de programa e a seta de base (texto escuro `#0F1419` sobre seta clara — comentado). Split misto §3.8; protagonista = em do título. |
| 109 | Gráfico combo | Duas séries de natureza diferente (barras + linha pontilhada). Edite: valores/alturas pela escala comentada, valores da linha pela conversão, última barra = gold; 4 tiles de KPI à direita. |

## 6. Checklist de QA (rode antes de entregar qualquer slide)

1. Somas de px fecham (colunas+gaps=1408; nada abaixo de y=804, salvo sangria intencional).
2. Um único protagonista gold. Nenhum `.glow`. Nenhum emoji.
3. Números em Space Grotesk; corpo em Plex Sans; labels em mono; serif só em título/quote/ghost.
4. Gráfico: barras coladas na baseline; labels abaixo dela; escala comentada bate com os valores.
5. Conectores com dot nas duas pontas, ancorados em coordenadas exatas.
6. Gravura armilar: só nos slides de respiro, canto inferior direito, bordas do PNG fora do canvas.
7. Dark: nenhum texto com hex escuro hardcoded (use tokens; sobre gold use `--on-gold`).
8. `<link ... href="style.css?v=5.2">` presente; slide registrado no `index.html`.
9. **Valide renderizando**: abra o arquivo no Chrome (ou headless `--screenshot`) e olhe a imagem — não confie só no código.

## 7. Assets

| Arquivo | Uso |
|---|---|
| `assets/g4-logo-branca.svg` | logo em slides dark (`.logo`, ~34px) |
| `assets/g4-logo-navy.svg` | logo em slides light |
| `assets/armilar-engraving-ice.png` | gravura para slides **dark** (via `.armilar--engraving`, token automático) |
| `assets/armilar-engraving-slate.png` | gravura para slides **light** (token automático) |
| `assets/armilar-solid-*.png` | marca sólida — uso pontual; evite crops que gerem "quarto de esfera" |
| `assets/overlay-raios.png` | overlay legado (v4 hairline, não usado no Órbita) |

Os tokens `--armilar-eng`/`--armilar-solid` trocam o PNG conforme o modo — você só posiciona.
