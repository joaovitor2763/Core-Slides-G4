# Core Slides G4 · v5 "Órbita" — Guia de uso e edição

> Referência completa para **quem (humano ou IA) vai copiar, editar e criar slides** com esta biblioteca.
> Leia as seções 1–4 antes de tocar em qualquer arquivo. O catálogo (seção 5) diz quando usar cada slide e o que editar nele.

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

## 4. Light ou dark? (decisão rápida)

- **Dark** = momentos de palco: capa, divisor, mentor/equipe, quotes, encerramento, KPIs-hero, pricing, mockup, frameworks conceituais (camadas, triângulo, polos, radar, concêntricos).
- **Light** = trabalho e leitura: gráficos de dados, tabelas, agendas, checklists, roadmaps, matrizes, bentos de conteúdo, prova social.
- Um deck real alterna: abre dark → blocos de conteúdo light → divisor dark → … → fecha dark.

## 5. Catálogo — quando usar e o que editar

Formato: **quando usar · o que editar · nota técnica**.

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
| 51 | Conceito + imagem | Ensinar um conceito em camadas: 3 blocos (kicker mono + body) com o último em destaque (régua 2px + fundo gold-dim) e ilustração vertical 3:4 à direita (placeholder → troque por imagem real, ver comentário no arquivo). |

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
| `assets/overlay-raios.png` | overlay legado da v4 (não usado na v5) |

Os tokens `--armilar-eng`/`--armilar-solid` trocam o PNG conforme o modo — você só posiciona.
