# Customizar templates

> Como criar variantes dos 20 templates sem quebrar a consistência visual do deck.

## TL;DR

**1 slide por vez.** Copia o template mais próximo, edita copy + dados + CSS local, valida visualmente, próximo.

## Escolher a identidade antes de customizar

A raiz contém a identidade padrão **Órbita**. Para decks de unidades específicas, use uma das variantes completas:

| Unidade | Pasta | Guia |
|---|---|---|
| G4 Next | `id-next/` | [`id-next/README.md`](../id-next/README.md) |
| G4 Scale | `id-scale/` | [`id-scale/README.md`](../id-scale/README.md) |
| G4 Club | `id-club/` | [`id-club/README.md`](../id-club/README.md) |

Depois de escolher a identidade, permaneça dentro dela: copie o HTML da coleção desejada e mantenha o `style.css` e os `assets/` da mesma pasta. Embora as variantes clonem os layouts oficiais, elas também contêm overrides por slide; trocar apenas a folha de estilo ou misturar assets entre identidades pode produzir contraste, logo e background incorretos.

Exemplo:

```bash
# Deck curto com identidade G4 Scale
cp id-scale/templates-short-deck/06-grafico-barras.html meu-slide.html
cp id-scale/templates-short-deck/style.css style.css
cp -R id-scale/templates-short-deck/assets assets
```

## Padrões de customização

### Mudar copy e dados (90% dos casos)

```html
<!-- Antes -->
<h1>Título original <em>com ênfase</em>.</h1>
<p class="lede">Texto original.</p>

<!-- Depois -->
<h1>Meu novo título <em>com ênfase</em>.</h1>
<p class="lede">Meu novo texto.</p>
```

Só mexe no texto. O CSS e a estrutura ficam.

### Adicionar 1 accent (dourado)

```css
/* Antes */
.num { color: var(--ink); }

/* Depois */
.num { color: var(--accent); }
```

Limite: **1 accent por slide** (excluindo `.eyebrow::before`).

### Trocar de light pra dark

```html
<article class="slide mode-dark" data-section="...">
```

Tokens semânticos reescritos automaticamente. **Não declare cor nenhuma** — use `var(--bg)`, `var(--fg)`, etc.

### Adicionar uma imagem (assets/)

Coloca a imagem em `assets/images/` e referencia:

```html
<img src="assets/images/minha-foto.jpg" alt="..." style="position:absolute; left:96px; top:200px; width:400px;" />
```

Pra `g4os-pages` (inline), converte pra data URI:
```bash
python3 -c "
import base64
with open('assets/images/minha-foto.jpg', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()
print(f'src=\"data:image/jpeg;base64,{b64}\"')
" > image-data-uri.txt
```

### Criar layout 2 colunas dentro de um slide existente

```html
<article class="slide" data-section="...">
  <div class="head">
    <div class="eyebrow">Eyebrow</div>
    <h1>Título</h1>
  </div>

  <div style="position:absolute; left:96px; right:96px; top:380px; bottom:80px; display:grid; grid-template-columns:1fr 1fr; gap:60px;">
    <div>
      <h3>Coluna esquerda</h3>
      <p>Conteúdo da esquerda.</p>
    </div>
    <div>
      <h3>Coluna direita</h3>
      <p>Conteúdo da direita.</p>
    </div>
  </div>
</article>
```

Sempre calcule o espaço disponível: `(1600 - 96*2) = 1408` de largura, `(900 - top - bottom) = altura`. Reserve `top:380+` antes de grids horizontais.

## Padrões de bug (não fazer)

### 1. Grid que invade o título
```css
/* Bug */
.head { top: 300px; }
.grid { top: 320px; }  /* muito perto do título */
```
**Fix**: reserve `top:380+` antes de grids horizontais.

### 2. Max-width que conflita com rail
```css
/* Bug */
.txt { max-width: 1200px; }  /* rail à direita tem 280px */
```
**Fix**: `max-width = (1600 - 96*2) - rail_width - gap = 1408 - 280 - 60 = 1068`.

### 3. Lista com padding grande demais
```css
/* Bug */
.li { padding: 32px 0; }  /* 5 itens × 64 = 320px num espaço de 280px */
```
**Fix**: `(900 - top - footer) / n_itens - line_height = padding_max`.

### 4. flex:1 em flex-direction:column cria vácuo
```css
/* Bug */
.step { display: flex; flex-direction: column; }
.txt { flex: 1; }  /* estica e cria vácuo entre txt e .out */
```
**Fix**: usar `justify-content: space-between` no `.step` OU `margin-top: auto` no `.out`.

### 5. Gráfico vertical com número no lugar errado
```html
<!-- Bug: .val dentro de .bar-v (altura 100% do chart) -->
<div class="bar-v">
  <div class="val">47</div>  <!-- bottom: 100% = topo do chart -->
  <div class="stem" style="height: 47%;"></div>
</div>

<!-- Fix: .val dentro de .stem (altura variável) -->
<div class="bar-v">
  <div class="stem" style="height: 47%;">
    <div class="val">47</div>  <!-- bottom: 100% = topo da barra -->
  </div>
</div>
```

### 6. Vídeo pesado (>5MB) no g4os-pages
```bash
# Comprimir antes
ffmpeg -y -i in.mp4 -vf "scale=-2:480" -c:v libx264 -preset slow -crf 28 -an -movflags +faststart out.mp4
```

### 7. srcdoc com aspas duplas quebra
```js
// Bug: template literal com s.html que tem aspas
template = `<iframe srcdoc="${s.html}">`;
// Fix: setAttribute lida com escape
ifr.setAttribute('srcdoc', s.html);
```

### 8. CSS não carrega em iframe srcdoc
```html
<!-- O parent tem style.css inline, mas o iframe via srcdoc cria documento novo -->
<!-- Fix: inline o style.css em cada slide também -->
```

## Quando usar sub-agente Opus 4.7

**Use pra**:
- Redesenhar layout inteiro de 1 slide
- Criar 3-5 variantes de 1 template
- Auditar 5+ slides em batch

**Não use pra**:
- Editar copy de 1 slide (mais rápido manual)
- Adicionar 1 accent
- Trocar 1 imagem

Brief do sub-agente:
```python
mcp__session__subagent_run(
  prompt="Caminho: /path/do/slide.html. ... Objetivo: ... Restrições: accent max 1x, canvas 1600x900, font-family Space Grotesk. Texto que NÃO pode ser alterado: ...",
  name="Designer slide 15",
  role="Designer de slides bento box",
  connectionSlug="managed-g4-aigateway",
  model="anthropic.claude-opus-4-7"
)
```

## Quando publicar e quando iterar local

| Situação | Ação |
|---|---|
| Editou copy, dados, accent | Local (file:// no navegador) |
| Redesenhou layout de 1 slide | Local + sub-agente valida |
| Auditou 5+ slides em batch | Local + AUDITORIA.md |
| Deck completo, vai apresentar | **Publicar** (g4os-pages) |

## TL;DR pra próxima sessão

1. Olhar `AGENTS.md` (regras firmes) + `playbook.md` (prosa)
2. Escolher template mais próximo de `templates-short-deck/` (52) ou `templates-expanded-deck/` (109) — abra o `index.html` da pasta pra navegar com filtro de categoria
3. Copiar → editar → validar visualmente → próximo
4. Publicar via g4os-pages (PUBLISH.md)
