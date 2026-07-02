# G4 Aulas IA — Playbook (v4)

> **Como construir e evoluir slides HTML das aulas G4** (Academia de IA, Gestão e Estratégia, e futuras).
> Reúne aprendizados de **4 sessões** + 2 decks publicados de 29 slides cada.

> **Versão firme (regras, tokens, lista de templates)**: ver `AGENTS.md` na mesma pasta.
> **Auditoria visual atual**: ver `AUDITORIA.md` na mesma pasta.

---

## TL;DR

Você tá construindo **um slide HTML por vez** num canvas fixo de **1600×900**, dentro de uma **paleta navy + gold + paper** com **1 accent dourado máximo por slide**, tipografia de **3 famílias** (Space Grotesk + IBM Plex Sans + IBM Plex Mono) e um **deck** com **passador** (cards 2 colunas + modo apresentação fullscreen).

Quando o deck ficar pronto, **inline tudo num único HTML de ≤5MB** e publique em `sites.g4oscloud.com` via `mcp__g4os-pages__publish_page` com slug fixo `aula-ia-ge` (use `republish_page` pra atualizar).

---

## 1. Por que 1600×900 fixo

- Slides de apresentação profissional rodam em projetor (16:9 nativo), TV 4K, monitor 16:9 e iframe embedado. Nesses, **um canvas fixo 1600×900** se encaixa direto.
- O navegador escala via `transform: translate(-50%,-50%) scale(s)` no `.slide` — o conteúdo nunca distorce.
- **Nunca** use width/height em % ou `vw/vh` no `.slide`. Tudo é `px`.
- Se você se pegar pensando "como faço responsivo?", pare. Você está fazendo canvas fixo.

---

## 2. As 3 famílias de fonte (papéis distintos)

```
Display  →  Space Grotesk      (títulos, números hero, h1-h4)
Text     →  IBM Plex Sans      (parágrafos, citações, descrições)
Mono     →  IBM Plex Mono      (eyebrows, labels, dados)
```

**Hierarquia por italic + weight, NUNCA por troca de fonte.** Sempre a mesma família.

Exceção editorial (capa, divisor e família de quotes — 20, 26, 34, 43): Cormorant Garamond serif pra criar "peso editorial".

**Carregamento**: o `@import` do `style.css` carrega as 4 famílias (Space Grotesk + IBM Plex Sans + IBM Plex Mono + Cormorant Garamond). Nenhum `<link>` extra é necessário no slide.

---

## 3. Paleta (light e dark)

Light (default):
- `--bg` paper `#F5F4F3` · `--fg` ink `#0F1419` · `--muted` `#6B7278` · `--rule` `#D8D6CF`
- `--accent` **gold `#B9915B`** (único, máx 1× por slide)

Dark (`.mode-dark` no `<article class="slide">`):
- `--bg` navy-600 `#001A2D` · `--fg` navy-50 `#E6EEF3` · `--muted` navy-200 `#80AABF`
- `--accent` continua `#B9915B` (dourado igual)

Ative dark com `class="mode-dark"`. Os tokens semânticos reescritos automaticamente — você não precisa declarar cor nenhuma no slide.

**Safety net (v4)**: os tokens crus de texto/linha (`--ink`, `--ink-2`, `--muted`, `--rule`) também flipam no `.mode-dark`. Um slide copiado do light não imprime mais letra preta em fundo navy. A exceção é texto escuro de propósito (sobre painel dourado ou célula paper dentro de slide dark): use `var(--on-accent)` no gold e hex explícito `#0F1419` no paper.

---

## 4. A regra do accent único

**Dourado aparece no máximo 1× por slide** (excluindo a barra do `.eyebrow::before`, que é herança do design system).

Exceção: o accent pode estar em **2 unidades** SE uma for a barra do eyebrow E a outra for uma palavra só em `<em>` dentro de texto corrido (não em heading inteiro).

Exemplos:
- **OK**: `.eyebrow` com barra dourada + 1 número com `color: var(--accent)` no gráfico.
- **OK**: `.eyebrow` + palavra "**5×**" em accent no parágrafo.
- **NÃO OK**: 1 h1 inteiro em dourado + 1 número em accent (cansa).
- **NÃO OK**: 2 cards com background dourado (visual bagunçado).

---

## 5. Os 48 templates (vocabulário visual)

Eles estão em `templates/` (01-capa.html ... 48-numero-hero.html). Cada um é um arquivo único, totalmente funcional, com `<style>` local + `<article class="slide">` no padrão. Para navegar visualmente: `examples/catalog.html` (grid com filtro por categoria + toggle light/dark; abrir via `python3 -m http.server` na raiz do repo).

| # | Template | Quando usar | Quando NÃO usar |
|---|----------|-------------|------------------|
| 01 | Capa | Primeira página, abrir seção de deck | Repetir (1 por deck ou por parte) |
| 02 | Palestrante | Bio do mentor/convidado | Sem foto de pessoa |
| 03 | Quote com imagem | Citação atribuída a alguém (com retrato) | Citação genérica (use 04) |
| 04 | Quote sem imagem | Citação genérica, marca d'água grande | Quando precisa retrato (use 03) |
| 05 | Gráfico horizontal | Bar chart com 2-5 categorias | Mais de 6 categorias (use 16) |
| 06 | Texto focado | Tese forte, 2 colunas curtas | Texto longo (use 11) |
| 07 | Timeline | 3-5 eventos em ordem cronológica | Dados quantitativos (use 10) |
| 08 | Divisor de bloco | Separar seções dentro do deck (cap 1, 2, 3) | Como slide de conteúdo |
| 09 | Comparação A×B | Antes/depois, com/sem, manual/com skill | 3+ opções (use 22 ou split) |
| 10 | Stats (4 colunas) | 4 métricas paralelas | Mais de 6 ou 1 número só (use 05) |
| 11 | Agenda | 3-6 etapas de uma jornada | Texto corrido (use 06) |
| 12 | Imagem + legenda | Caso/estudo com screenshot ou foto | Sem imagem (use 13) |
| 13 | Lista numerada | 3-7 itens com hierarquia clara | Mais de 7 (quebra) |
| 14 | Três pilares | Manifesto, 3 eixos, framework | 2 ou 4 eixos (use 11 ou split) |
| 15 | Encerramento | Última página, hero + contato | Repetir |
| 16 | Gráfico vertical + nota | Volume por categoria, com insight editorial | Poucos dados (use 05) |
| 17 | A vs B | Split 50/50, accent no B | 3 opções (use 22) |
| 18 | Bento mosaic | 4-6 blocos com proporções variadas | Tudo do mesmo tamanho (use 11) |
| 19 | Stepper | 4-5 etapas sequenciais com output | Sem output visível (use 11) |
| 20 | Quote hero | Citação grande em dark mode | Em slide claro (use 04) |
| 21 | 2-boxes | Provocação binária ("por esporte" vs "profissional") | 3+ opções (use 22) |
| 22 | Mixed grid | Comparação complexa (matriz + lista + cards) | Conteúdo simples (use 18) |
| 23 | Custom 2-col | Headline à esquerda, corpo à direita | Texto muito longo |
| 24 | Pergunta CTA | Pergunta de transição entre blocos | Como conteúdo (é respiro) |
| 25 | Hero logo G4 | Capa alternativa com marca + patterns | Slides internos |
| 26 | Quote galeria split | Citação + imagem grande em moldura mat | Sem imagem forte (use 04/20) |
| 27 | Mentor hero | Bio com nome gigante + retrato 38% | Bio curta (use 02) |
| 28 | Transição aceleradores | "O que vem a seguir" + 4 itens numerados | Etapas com detalhe (use 19) |
| 29 | Bento comparativo | Dois mosaicos lado a lado (A vs B) | Comparação simples (use 09/17) |
| 30 | Grid de ferramentas | 4 colunas descritivas (stack, métodos) | Dados numéricos (use 10) |
| 31 | Narrativa numérica | 3 conceitos ensinados com um dado cada | KPIs puros (use 10) |
| 32 | Bento de métricas | Mosaico 3×3 com bignums (ex: 70/20/10) | Poucos dados (use 48) |
| 33 | Três pilares percentuais | Regra de alocação com % gigante (dark) | Pilares sem número (use 14) |
| 34 | Encerramento quote | Fechamento com citação serif + CTA (dark) | Fechamento com contato (use 15) |
| 35 | Gráfico de linha | Tendência/evolução no tempo (SVG) | Comparação pontual (use 05/16) |
| 36 | Gráfico donut | Composição/share de um todo | Mais de 5 fatias (use 38) |
| 37 | Barras duplas | 2 séries × N categorias (antes vs depois) | 1 série só (use 16) |
| 38 | Barras de progresso | % de adoção/share por item | Valores absolutos (use 05) |
| 39 | Imagem full + overlay | Foto impactante + título por cima (dark) | Sem foto de qualidade |
| 40 | Imagem hero lateral | Tese + imagem full-bleed 38% sem moldura | Imagem que precisa moldura (use 12/26) |
| 41 | Galeria duo | Duas evidências visuais lado a lado | 1 imagem só (use 12) |
| 42 | Quote de post/tweet | Post de LinkedIn/X como evidência | Citação clássica (use 03/04) |
| 43 | Quote dupla | Duas visões em contraste | 1 voz só (use 04) |
| 44 | Tabela comparativa | Matriz de critérios × opções, 1 recomendada | 2 opções (use 09/17) |
| 45 | Checklist | O que funciona vs o que evitar | Lista simples (use 13) |
| 46 | Funil | Conversão/afunilamento em estágios | Etapas sem perda (use 19) |
| 47 | Exercício em passos | Dinâmica com tempos por etapa | Sequência sem tempo (use 19) |
| 48 | Número hero | Um dado só como takeaway | Vários números (use 10/32) |

**Como reaproveitar**: copie o arquivo `.html` do template escolhido pra dentro do seu deck, renomeie (e.g. `08-divisor.html` → `08-minha-secao.html`), edite copy + dados + CSS local.

---

## 6. Anatomia de um slide

Estrutura mínima:

```html
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8" />
<title>08 · Minha seção</title>
<link rel="stylesheet" href="style.css" />
<style>
  /* CSS local — use tokens semânticos do style.css */
  .head { position: absolute; left: var(--pad); top: 132px; right: var(--pad); }
  .head h1 { font-size: 64px; line-height: 1.05; letter-spacing: -0.025em; }
  .head h1 em { font-style: italic; font-weight: 500; }
  .head .eyebrow { margin-bottom: 22px; }
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

**Invariantes**:
- `<article class="slide" data-section="...">` é o único canvas. Tudo dentro dele.
- `<div class="stage">` é o wrapper que centraliza o slide. Não mexa.
- O `<script>` de fit() no fim é obrigatório — sem ele o slide não escala. Use exatamente o snippet acima.
- `data-section="..."` é o eyebrow do canto superior esquerdo (opcional).

---

## 7. Padrões de layout (o que aprendi errando)

### 7.1 Grid que invade o título
**Erro clássico**: h1 grande + grid horizontal começando em `top: 300`. O grid "empurra" o título pra cima, ou pior, fica embaixo dele mas sem espaço.
**Fix**: reserve `top: 380+` antes de grids horizontais. **Calcule** `(900 - top - footer_bottom) / n_rows` antes de definir altura do grid.

### 7.2 Max-width que conflita com rail
**Erro**: definir `max-width: 1200` em texto que fica ao lado de um rail à direita de 280px. Texto invade rail.
**Fix**: `max-width = (1600 - 96*2) - rail_width - gap`. Para o slide 15 do Gestão, isso deu `max-width: 1080`.

### 7.3 Lista com padding grande demais
**Erro**: 5 itens × `padding: 32px` = 320px só de padding, mas o espaço disponível é 280px.
**Fix**: `(900 - top - footer) / n_itens - line_height - gap` antes de padding.

### 7.4 flex:1 em flex-direction:column cria vácuo
**Erro**: `display: flex; flex-direction: column` com `flex: 1` no conteúdo. O `flex: 1` "estica" o conteúdo até o final, criando vácuo invisível entre o conteúdo e o final.
**Fix**: usar `justify-content: space-between` no parent OU `margin-top: auto` no último filho.

### 7.5 Gráfico vertical com número no lugar errado
**Erro**: `.val { position: absolute; bottom: calc(100% + 14px) }` dentro de `.bar-v` (que tem `height: 100%` do chart). O `bottom: 100%` é relativo ao `.bar-v` que ocupa o chart inteiro, então todos os números ficam no topo do chart.
**Fix**: `<div class="val">` **dentro do `<div class="stem">`** (altura variável, `position: relative`). Aí o `bottom: 100%` referencia o topo do stem (= topo da barra).

### 7.6 Vídeo pesado no g4os-pages
**Erro**: vídeo de 33MB estoura o limite de 5MB do `g4os-pages`.
**Fix**: comprimir com ffmpeg antes de inlinear:
```bash
ffmpeg -y -i original.mp4 -vf "scale=-2:480" -c:v libx264 -preset slow -crf 28 -an -movflags +faststart out.mp4
# 33MB → ~600KB
```

### 7.7 srcdoc com string literal quebra template
**Erro**: `<iframe srcdoc="${s.html}" ...>` com template literal do JS. Se `s.html` contém aspas duplas, o atributo `srcdoc` quebra e o slide não renderiza.
**Fix**: usar DOM manipulation no JS:
```js
const ifr = document.createElement('iframe');
ifr.setAttribute('srcdoc', s.html);  // setAttribute lida com escape corretamente
```

### 7.8 CSS não carrega em iframe via srcdoc
**Erro**: o parent (index.html) tem o `style.css` inline, mas o iframe via `srcdoc` cria um documento novo que não herda o CSS do parent. Slide renderiza sem estilo.
**Fix**: **inline o `style.css` em cada slide também**, não só no parent. Deck-inlined = `<style>...</style>` no index + dentro de cada slide.

### 7.9 Eyebrow local em cima do data-section
**Erro**: o `data-section` do `<article>` renderiza via `.slide::before` em `top: 48px; left: var(--pad)`. Um eyebrow/kicker local posicionado no mesmo `top: 48px` imprime um texto por cima do outro (aconteceu no template 30).
**Fix**: a faixa `top: 0–80px` do canto superior esquerdo é reservada pro `data-section`. Eyebrows locais começam em `top: 96px` (ou zere o `data-section=""`).

### 7.10 Orçamento de accent estourado por repetição
**Erro**: em layouts de colunas/células repetidas, dar `color: var(--accent)` ao elemento-hero de CADA coluna multiplica o dourado (3 colunas = 3 accents; aconteceu no template 31).
**Fix**: a classe de accent vai numa modificadora (`.lead`, `.current`, `.destaque`) aplicada a UMA coluna/célula; as demais ficam em `--fg`.

---

## 7B. Tratamentos de imagem (portados do deck founder-ia-conteudo)

Quatro formas canônicas de colocar imagem num slide, da mais moldurada à mais crua:

1. **Moldura "mat de galeria"** (templates 26, 41) — `padding` de 20-22px com `linear-gradient` de mat + keyline dourada fina (`box-shadow: 0 0 0 1px rgba(185,145,91,0.5)`) no clip interno. Única exceção permitida a border-radius/sombra. Versão dark usa alfas navy (ver `26-quote-galeria-split-dark.html`).
2. **Hero lateral full-bleed** (template 40) — imagem sangrando topo-a-base em 38% da largura, sem moldura, com `.edge-blend` (`linear-gradient(to right, var(--bg), transparent)` de ~120px) fundindo a borda esquerda da foto com o fundo. Ajuste o enquadramento com `object-position` (comentado no arquivo).
3. **Full-bleed com overlay** (template 39) — foto cobre os 1600×900 inteiros + overlay `linear-gradient(to top, rgba(0,11,21,0.92), rgba(0,11,21,0.15))` + texto ancorado na base esquerda. Sempre dark.
4. **Frame com legenda** (template 12) — screenshot/foto documental com sidebar de leitura.

**Overlay decorativo de raios**: `assets/patterns/overlay-raios.png` (portado do deck founder-ia) — posicionar `right: 0; bottom: 0; width/height: 900px; background-size: contain; opacity: 0.7; pointer-events: none` em capas/divisores/encerramentos dark. Mesma família dos `pattern-shield/symbol.png` usados no template 25.

**Placeholder padrão**: os templates de imagem não usam foto real — usam `div` escura com hachura `repeating-linear-gradient(45deg, ...)` + label mono. Cada template documenta em comentário HTML como trocar pela foto final.

---

## 8. Fluxo de criação de slide (1 por vez)

```bash
# 1. Copiar template mais próximo (catálogo visual: examples/catalog.html)
cp templates/05-grafico.html meu-deck/08-meu-grafico.html

# 2. Editar o slide
# - Copiar do template-base
# - Trocar data-section, h1, dados do gráfico
# - Adicionar entrada no array `slides` do index.html (n, file, name)

# 3. Validar visualmente
# - Abrir o deck local no browser (index.html do deck, ou o slide direto)
# - Ir no card do slide novo, dar zoom/print
# - Mandar print pro usuário validar

# 4. Publicar (regera deck-inlined + republica)
python3 build-deck-inlined.py
mcp__g4os-pages__republish_page(slug="aula-ia-ge", html=...)
```

**Regra**: **NUNCA** edite mais de 1 slide sem validar o anterior**. Especialmente em lote (5-10 slides), porque erros de copy/dados/posição se acumulam.

---

## 9. O passador (index.html)

O `index.html` é o **passador de slides**:
- Grid 2 colunas com thumbnails
- Botão "▶ Apresentar do 1º" → modo fullscreen
- Setas / Espaço / Enter → próximo
- ← / Backspace → anterior
- Esc → sair do modo apresentação
- Click no card → abre o slide

**Estrutura**:
- Header com título do deck
- Grid de cards (`.card`)
- Botão fixo "Apresentar do 1º"
- HUD no modo apresentação (prev / counter / next / close)
- Iframe no modo apresentação (frame 1600x900, escalado pra caber no viewport)

**Reaproveitamento**: copie o `index.html` inteiro, mude o array `slides` (n, file, name) e o título.

**Para o deck-inlined**: o index.html é gerado pelo script Python. Cada slide vira um `<script type="application/json" id="slide-NN">{file, html}</script>`. O JS lê via `getElementById().textContent` + `JSON.parse()`. Cards montados via DOM (não template literal) pra evitar escape de aspas. Modo apresentação também via `setAttribute('srcdoc', slides[idx].html)`.

---

## 10. Publicação (g4os-pages)

**Tool**: `mcp__g4os-pages__publish_page(slug, title, html)` ou `republish_page(slug, html)`.

**Limite**: 5MB por arquivo. Deck de 29 slides + vídeo comprimido: ~3.7MB.

**Estratégia**:
1. Build do `deck-inlined.html` único (todos os slides inlinados como `<script type="application/json">` no head)
2. Inline o `style.css` em cada slide também (srcdoc não herda CSS do parent)
3. Inline imagens como data URI (`src="data:image/png;base64,..."`)
4. Inline vídeo comprimido (se houver) como data URI (`src="data:video/mp4;base64,..."`)
5. `mcp__g4os-pages__republish_page(slug="aula-ia-ge", html=<conteúdo>)`

**URL final**: `https://sites.g4oscloud.com/s/aula-ia-ge/` (noindex por padrão).

**NÃO use** `publish_page` pra atualizar — vai incrementar slug (`aula-ia-ge-2`). Use `republish_page` com o mesmo slug.

---

## 11. Sub-agentes (quando usar)

**Redesign de slide**: `mcp__session__subagent_run` com `connectionSlug: managed-g4-aigateway` e `model: anthropic.claude-opus-4-7` (ou `anthropic.claude-opus-4-8`).

Brief do sub-agente deve ter:
- **Caminho absoluto** do arquivo
- **Texto que NÃO pode ser alterado** (dados, citações, nomes)
- **Lista do que está errado** (o usuário reportou)
- **Restrições de design** (accent count, modo dark, etc)

**NÃO use** sub-agente pra 1 slide simples — fazer manualmente é mais rápido. Use sub-agente pra:
- Redesenhar layout inteiro de 1 slide (bento, comparador, etc)
- Auditar 5+ slides em batch (classificar ✅/❌)
- Criar variantes de 1 template (e.g. "faça 3 versões do template 16 com paletas diferentes")

**Modelos**:
- `anthropic.claude-opus-4-7` — design + revisão visual (recomendado)
- `anthropic.claude-opus-4-8` — design mais novo, mesma função
- `claude-sonnet-4-6` — auditoria mais barata
- `claude-haiku-4-5-20251001-v1:0` — automações simples (NÃO pra design)

---

## 12. Decisões de produto (por que assim)

- **29 slides** por deck (não 15, não 50) — tempo de aula presencial ~45min × ~1.5min/slide = 60-70min com folga. Cabe em 1 aula + 1 demo ao vivo.
- **Passador com cards 2 colunas** (não slideshow automático) — permite navegação livre, anotações, "pula pro slide 12 que eu quero discutir agora".
- **Publicação self-contained via g4os-pages** (não Google Slides, não PDF linkado) — HTML permite vídeo inline, animações, interatividade, e o link pode ser compartilhado com alunos.
- **Vídeo comprimido pra 480px** (não full HD) — limite de 5MB do g4os-pages, e no projetor 480p num slide 1600x900 fica indistinguível de HD.
- **Cores navy + gold** (não Inter, não vermelho) — alinhado com o G4 brand portal, usado em todos os materiais da empresa.
- **Cormorant Garamond só em capa + divisor + perguntas dark** (não em todo slide) — serif editorial pra criar "peso de seção" sem virar design frilly.

---

## 13. Casos especiais

### Capa dark com logo G4 + símbolos
Slide 1 do deck Gestão e Estratégia: fundo navy + logo G4 branca no canto superior esquerdo + hairline dourada + tag "Para quem quer mais" no canto superior direito + título serif "G4 Gestão / *e Estratégia*." em dourado + subtítulo curto em serif + barra dourada na base + 2 overlays de imagem (escudo em low opacity, símbolo G4 full-screen em low opacity).

**Decisão editorial**: a capa é o ÚNICO slide que pode "gastar mais atenção visual" — é a primeira impressão. Todos os outros slides são "conteúdo".

### Divisor dark
Slide 24: fundo navy + número gigante "03" semi-transparente como marca d'água (removido) + título serif "Como fazer isso *durar* →" + hairline + subtítulo curto. Sem eyebrow (não compete com o título).

### Perguntas dark
Slides 9, 18: fundo navy + título serif gigante + sub-mono + kicker. Usado pra criar "pausa reflexiva" entre seções light.

### Compressão de assets
Antes de inlinear: comprimir tudo. PNGs > 500KB → sips -Z 1200 ou otimizar via tinypng. JPGs > 500KB → sips -Z 1600 -s format jpeg --setProperty quality 0.8. MP4s → ffmpeg CRF 28 com 480px de altura.

---

## 14. Onde isso está documentado

- **`AGENTS.md`** (mesma pasta) — regras firmes, tokens, lista dos 48 templates, mapeamento dos 29 slides
- **Catálogo canônico de 48 templates** — `templates/` (navegável em `examples/catalog.html`)
- **Projeto** — `Aulas G4 - IA` (`project_c1402fb9-6848-4cea-9fef-489da1fbf7fe`)
- **Sessões-chave**:
  - `260614-awake-grove` — design system + 20 templates
  - `260614-apt-nebula` — tokens semânticos no CSS
  - `260615-sunny-dolphin` — 1ª aula (G4 Academia de IA, 29 slides)
  - `260615-awake-creek` — técnica de export PDF em paisagem 16:9
  - `260623-misty-lake` — 2ª aula (G4 Gestão e Estratégia, 29 slides) + publicação no g4os-pages

---

## 15. TL;DR pra próxima sessão

Se você tá chegando nessa sessão sem contexto:

1. **Ler `AGENTS.md`** (regras firmes) + **`playbook.md`** (este arquivo, prosa).
2. **Olhar o catálogo de 48 templates** em `templates/` (navegável em `examples/catalog.html`).
3. **Procurar o template mais próximo** no catálogo pra novo slide.
4. **1 slide por vez**: copiar → editar → validar visualmente → próximo.
5. **Publicar** com `mcp__g4os-pages__republish_page(slug="...", html=<deck-inlined>)`.

**Atalhos úteis**:
- Sub-agente Opus 4.7: `mcp__session__subagent_run(prompt, connectionSlug="managed-g4-aigateway", model="anthropic.claude-opus-4-7")`
- Build deck-inlined: `build-deck-inlined.py` (raiz do repo)
- Comprimir vídeo: `ffmpeg -y -i in.mp4 -vf "scale=-2:480" -c:v libx264 -preset slow -crf 28 -an -movflags +faststart out.mp4`
- Comprimir PNG: `sips -Z 1600 in.png --out out.png` (mantém proporção, max 1600px)
- Comprimir JPG: `sips -s format jpeg --setProperty quality 0.8 in.jpg --out out.jpg`