# Core Slides G4

> **Three decks, one language.** Build G4 slides by picking the library that matches the job — not by version number. All official templates share the **"Órbita"** visual language (Playfair serif + Space Grotesk display, navy + gold + paper, sphere armilar overlay, surfaces with radius + soft shadow, chips/pills for meta).

## The three official decks

| Deck | Slides | Use it for |
|---|---|---|
| **[`templates-short-deck/`](templates-short-deck/README.md)** | **52** | Lean projects — aulas, workshops, talks, internal decks. The minimum viable G4. **Start here.** |
| **[`templates-expanded-deck/`](templates-expanded-deck/README.md)** | **109** | Everything: case study, financeiro, pitch de vendas e produto. Same language as short-deck, more layouts. |
| **[`deck-frameworks/`](deck-frameworks/GUIA.md)** | **18** | Frameworks visuais — ciclos, sistemas, mapas de decisão, branding e ferramentas estratégicas. |

> **Decisão prática:** comece em `short-deck`. Use `expanded-deck` quando faltar um layout operacional específico; use `deck-frameworks` quando o centro do slide for um modelo ou ferramenta visual.

## Identity variants

The three official collections also have complete **visual identity variants**. Each `id-*` folder mirrors `templates-short-deck`, `templates-expanded-deck` and `deck-frameworks`: the slide structure and content model remain compatible, while typography, palette, logos, backgrounds and decorative assets follow the selected brand.

| Identity | Folder | Visual direction | Start here |
|---|---|---|---|
| **G4 Next** | [`id-next/`](id-next/README.md) | Deep petroleum, wine accent and Next armillary assets | [`id-next/templates-short-deck/index.html`](id-next/templates-short-deck/index.html) |
| **G4 Scale** | [`id-scale/`](id-scale/README.md) | Petroleum blue, punctual ruby and vertical fringe motifs | [`id-scale/templates-short-deck/index.html`](id-scale/templates-short-deck/index.html) |
| **G4 Club** | [`id-club/`](id-club/README.md) | Near-black navy, brand gold and CLUB letterpress backgrounds | [`id-club/templates-short-deck/index.html`](id-club/templates-short-deck/index.html) |

Use the root collections for the default **Órbita** identity. Use an `id-*` collection when the deck belongs to that business unit; copy templates only from within the same identity so its `style.css`, HTML overrides and `assets/` stay aligned. Do not treat these folders as extra layout libraries: they are branded clones of the same three canonical collections.

---

## Quick start

```bash
# 1. Clone o repo
git clone https://github.com/joaovitor2763/Core-Slides-G4.git
cd Core-Slides-G4

# 2. Abra o passador do deck escolhido no browser
open templates-short-deck/index.html
# (ou: open templates-expanded-deck/index.html)
# (frameworks: open deck-frameworks/index.html)

# 3. Copie o template mais próximo do seu slide
cp templates-short-deck/06-grafico-barras.html meu-slide.html

# 4. Edite copy + dados + CSS local
#    (use tokens do templates-short-deck/style.css — ou do expanded-deck)

# 5. Valide visualmente
open meu-slide.html

# 6. Publique (opcional)
#   - PDF: docs/EXPORT-PDF.md (Chrome headless, 1 slide por vez)
```

---

## How to use a template

Cada template é um arquivo `.html` único e auto-contido. A estrutura é sempre a mesma:

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>NN · Nome</title>
  <link rel="stylesheet" href="style.css" />
  <style>/* CSS local — use tokens semânticos do style.css */</style>
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

**Regras de ouro:**

- **Canvas fixo 1600×900** (16:9). Nada de `vw/vh/%` no conteúdo — tudo em `px` absolutos.
- O `<script>fit()</script>` no fim é **obrigatório** — sem ele o slide não escala.
- `data-section="..."` é só metadado, **não renderiza nada**. O único kicker visível é o `.eyebrow` do título.
- **Use tokens do `style.css`** (`var(--bg)`, `var(--gold)`, `var(--text-1)` etc.), nunca hex de texto direto.
- **1 accent por slide** (gold com parcimônia). Sem emoji. Sem `vw/vh`.

Detalhes completos por template (anatomia, quando NÃO usar, customização): [`templates-short-deck/GUIA.md`](templates-short-deck/GUIA.md), [`templates-expanded-deck/GUIA.md`](templates-expanded-deck/GUIA.md) ou [`deck-frameworks/GUIA.md`](deck-frameworks/GUIA.md).

---

## Picking the right template

### `templates-short-deck/` (52 slides)

| # | Slide | Modo | Use |
|---|---|---|---|
| 01 | Capa | dark | Primeira página, abrir seção |
| 02 | Divisor de capítulo | dark | Separar partes do deck |
| 03 | Mentor (nome serif + retrato) | dark | Bio do mentor/palestrante |
| 04 | Quote editorial + dado | light | Citação atribuída com dado que valida |
| 05 | Agenda (item atual em gold) | light | 3-6 etapas de uma jornada |
| 06 | Gráfico de barras | light | Bar chart com 2-5 categorias |
| 07 | Gráfico de linha | light | Tendência/evolução no tempo |
| 08 | Donut + legenda | light | Composição/share de um todo |
| 09 | Stats 4× com chips | light | 4 métricas paralelas com delta |
| 10 | Antes × depois | light | Comparação simples com card gold |
| 11 | Bento (hero + células) | dark | Mosaico 3,4× com células vidro |
| 12 | Método em 4 passos | light | Numerados com serif |
| 13 | Imagem hero rotacionada | dark | Foto + chip flutuante |
| 14 | Tabela de decisão | light | Critérios × opções, recomendado em gold |
| 15 | Funil (pills + taxa) | dark | Conversão decrescente |
| 16 | Encerramento (quote + CTA) | dark | Última página |
| 17 | Pizza / composição | light | Conic + legenda rica |
| 18 | Radar 5 eixos | dark | 2 séries em gráfico de radar |
| 19 | Barras de progresso | light | % de adoção/share por item |
| 20 | Matriz 2×2 com eixos | light | Posicionamento com setas |
| 21 | Timeline alternada | light | 3-5 eventos horizontais |
| 22 | Fluxo ramificado | light | Pills + curvas SVG |
| 23 | Ciclo / anel | light | Processo cíclico com callouts |
| 24 | Framework de camadas | dark | Pirâmide/pirâmide invertida |
| 25 | Mockup laptop CSS | dark | Tela demo G4 OS |
| 26 | Bento claro 4 células | light | Mosaico 4 com hairlines |
| 27 | Split antes × depois | misto | Navy/paper lado a lado |
| 28 | Framework Venn 3 círculos | light | Sobreposição de 3 conjuntos |
| 29 | Quote com foto/retrato | dark | Citação + retrato |
| 30 | Quote mínima 84px | dark | Citação grande centralizada |
| 31 | Divisor claro | light | Ghost + gravura armilar |
| 32 | Checklist fazer × evitar | light | +/− em colunas |
| 33 | Polos comparativos | dark | 2 esferas com spokes |
| 34 | Ciclo de setas | dark | Loop visual com setas |
| 35 | Círculos concêntricos | dark | TAM/SAM/SOM |
| 36 | Árvore / hierarquia | dark | BSC / organograma |
| 37 | Cronograma multi-dia | dark | Agenda de 2-5 dias |
| 38 | Triângulo estratégico | dark | 3 vértices |
| 39 | Manifesto tipográfico | light | Frase grande + assinatura |
| 40 | Tabela de dados densa | light | Tabela com números |
| 41 | Barras comparativas | light | 2 séries × N categorias |
| 42 | Linhas competindo + gap | light | Comparação temporal com gap |
| 43 | Cards com ícones SVG | light | Grid de features |
| 44 | Empilhadas 100% | light | Composição percentual |
| 45 | Grid de KPIs 2×2 | dark | 4 KPIs grandes |
| 46 | Roadmap por fases | light | Linha do tempo de entregas |
| 47 | Perguntas da aula | dark | Discussão/perguntas |
| 48 | Planos / pricing | dark | Tabela de preços |
| 49 | Equipe / mentores | dark | Grid de pessoas |
| 50 | Prova social (3 quotes) | light | Depoimentos em colunas |
| 51 | Conceito + imagem | light | Bloco + ilustração 3:4 |
| 52 | Exercício prático | light | Grade de passos + tempo |

Catálogo completo + GUIA detalhada: [`templates-short-deck/README.md`](templates-short-deck/README.md).

### `templates-expanded-deck/` (109 slides)

Tudo do `short-deck` (01-52) **+ 57 templates extras**, organizados em 10 categorias:

- **Aulas & Educação** (63-71): módulo de aula, programa 2 dias, hub radial, vozes de usuários, escala de níveis, quiz
- **Case Study** (72-78): abertura, contexto, solução, resultados, linha do tempo, aprendizados, evidência
- **Financeiro** (79-86): resumo executivo, DRE, ponte, metas vs real, fluxo de caixa, orçamento, cenários, mapa de riscos
- **Pitch & Vendas** (87-94): problema, solução, mercado, modelo de receita, tração, posicionamento, oferta, próximos passos
- **Produto** (95-100): mockup celular, features, jornada, arquitetura, heatmap, gantt, fases programa
- **Referências G4** (101-109): público-alvo, duplo mentor, seta processo, pentágono pilares, jornada programas, matriz programas, funil horizontal, gráfico combo, recap, biblioteca, dinâmica turma, perfil+quote, galeria retratos, plano anual, objetivos, conceito+definição, canvas exercício, pergunta debate, gantt

Catálogo completo + GUIA detalhada: [`templates-expanded-deck/README.md`](templates-expanded-deck/README.md).

### `deck-frameworks/` — frameworks customizados

Use esta biblioteca quando o **framework é o conteúdo principal do slide**: ciclos, sistemas, camadas, mapas conceituais, modelos de decisão e ferramentas estratégicas que exigem geometria própria. Para gráficos, tabelas, agendas, quotes ou layouts editoriais comuns, continue usando `short-deck` ou `expanded-deck`.

**Como explorar:**

```bash
open deck-frameworks/index.html
```

O catálogo mostra todos os frameworks e oferece **Apresentar** e **Modo apresentador**. Abra o [`deck-frameworks/GUIA.md`](deck-frameworks/GUIA.md) para entender a anatomia, a intenção e o melhor ponto de partida de cada modelo.

| # | Framework | Use quando precisar mostrar… |
|---|---|---|
| 01 | Ciclos interdependentes | Dois loops que trocam informação por um handoff crítico. |
| 02 | Escolha de proposta de valor | Uma decisão central entre seis territórios de diferenciação. |
| 03 | Espectro de proposta de valor | Camadas entre negócio, prospect, produto e conversão. |
| 04 | Alavancas de criação de valor | Seis formas complementares de gerar valor. |
| 05 | Builder de proposta de valor | Uma ferramenta circular construída em seis partes. |
| 06 | Canvas de proposta de valor | Encaixe entre mapa de valor e perfil do cliente. |
| 07 | Mapa de valor × perfil do cliente | Relação bowtie entre oferta e necessidades do cliente. |
| 08 | Pentágono de co-criação | Cinco movimentos conectados por um princípio central. |
| 09 | Branding, identidade, marca | Passagem da intenção para expressão e percepção. |
| 10 | Processo de desenvolvimento da marca | Cinco etapas sequenciais com duas camadas de leitura. |
| 11 | Marca e negócio | Relação entre estratégia de negócio e estratégia de marca. |
| 12 | Do mercado ao nicho | Recorte progressivo de mercado, segmento e nicho. |
| 13 | Mapa de stakeholders | Grupos de interesse orbitando a organização. |
| 14 | Interseções (Venn) | Sobreposições e territórios compartilhados. |
| 15 | Elementos da estratégia de marca | Quatro dimensões organizadas ao redor de um núcleo. |
| 16 | Pirâmide de ressonância | Evolução hierárquica até relacionamento e ressonância. |
| 17 | Modelo de gestão de marca | Circuito entre identidade, expressão, percepção e gestão. |
| 18 | Painel de execução da marca | Estágios, progresso e prioridades de implementação. |

**Como criar um framework customizado:**

1. Comece pelo template geometricamente mais próximo em `deck-frameworks/`.
2. Copie o arquivo; nunca altere o template-base para um projeto específico.
3. Preserve `style.css`, tokens Órbita, canvas 1600×900 e o orçamento de um protagonista gold.
4. Recalcule raios, ângulos, coordenadas e conectores — e documente a geometria no comentário do CSS.
5. Valide no navegador **um slide por vez**; verificação automática não substitui QA visual.
6. Se o novo modelo for reutilizável, registre-o no array `slides` de `deck-frameworks/index.html` e documente-o no `GUIA.md`.

---

## "Órbita" visual language

- **Display:** Space Grotesk para h1–h4 + números.
- **Serif:** Playfair Display em capa, dark dividers e quote-hero — itálico dourado na palavra-chave.
- **Body:** IBM Plex Sans. Mono (eyebrows, labels, dados): IBM Plex Mono.
- **Paleta:** paper `#F5F4F3` · navy `#001525` (light e dark) · gold `#B9915B` (light) / `#C9A05C` (dark).
- **1 accent por slide.** Cards com radius 22 + soft shadow; hairlines para hierarquia em tabelas densas.
- **Sphere armilar** (`.armilar` / `.armilar--engraving`) como overlay decorativo, com PNGs pré-tingidos por modo em `templates-*/assets/`. Outras decorações: `.grain` (filme), `.ghost` (linha-eco), `.glow` (halo dourado).

Detalhes completos: [`templates-short-deck/GUIA.md`](templates-short-deck/GUIA.md) e [`templates-expanded-deck/GUIA.md`](templates-expanded-deck/GUIA.md).

---

## Estrutura recomendada para um deck/projeto de slides

**A pasta do seu deck deve seguir a mesma estrutura das pastas de templates** (`templates-short-deck/` ou `templates-expanded-deck/`):

```
meu-deck/                        ← pasta raiz do seu deck
├── index.html                   ← passador de slides (navegação + modo apresentação)
├── style.css                    ← design system compartilhado (tokens + classes)
├── slides/                      ← todos os slides do deck, um .html por slide
│   ├── 01-capa.html
│   ├── 02-agenda.html
│   ├── 03-quote.html
│   ├── 04-conceito.html
│   ├── 05-grafico-barras.html
│   ├── ...
│   └── NN-encerramento.html
├── assets/                      ← imagens, logos, padrões, fontes do deck
│   ├── logos/                   ← ex: g4-logo-branca.svg
│   ├── images/                  ← ex: mentor-retrato.jpg, produto-mockup.png
│   ├── patterns/                ← ex: armilar-solid-ice.png
│   └── data/                    ← ex: vendas-2026-q2.json (se houver dados)
└── build/                       ← (opcional) output do build-deck-inlined.py
    └── meu-deck-inlined.html
```

**Regras de estrutura:**

1. **`index.html` no root** — é o passador. Lê `slides/` e renderiza. Abra `file://.../meu-deck/index.html` no browser pra navegar com setas/Espaço/Esc.
2. **`style.css` no root** — único CSS compartilhado, contém os tokens (`--bg`, `--gold`, etc.) e classes semânticas (`.head`, `.eyebrow`, `.body`, `.num`, `.kpi`). Cada slide faz `<link rel="stylesheet" href="../style.css" />`.
3. **`slides/` é uma subpasta** — todos os slides são arquivos `.html` independentes. Nomes com prefixo numérico (`01-`, `02-`, ...) pra ordenar.
4. **`assets/` no root** — imagens, logos, padrões e dados. Paths nos slides: `../assets/images/...`.
5. **Cada slide é auto-contido** — `<style>/* CSS local */</style>` no head, `<article class="slide" data-section="...">` no body, `<script>fit()</script>` no fim. Copy de `templates-short-deck/NN-nome.html` pra `slides/NN-nome.html`, ajuste os paths de `style.css` e `assets/` (`style.css` → `../style.css`, `assets/foo.png` → `../assets/foo.png`).

**Como montar o deck:**

```bash
# 1. Crie a pasta com a estrutura acima
mkdir -p meu-deck/slides meu-deck/assets/{images,logos,patterns,data}
cp templates-short-deck/index.html  meu-deck/index.html
cp templates-short-deck/style.css   meu-deck/style.css

# 2. Copie os templates que você vai usar
cp templates-short-deck/01-capa.html         meu-deck/slides/01-capa.html
cp templates-short-deck/05-agenda.html       meu-deck/slides/02-agenda.html
cp templates-short-deck/06-grafico-barras.html meu-deck/slides/03-grafico.html
# ... etc

# 3. Em CADA slide copiado, ajuste os paths
#    <link rel="stylesheet" href="style.css" />          → ../style.css
#    <img src="assets/foo.png" />                         → ../assets/foo.png
# (1 find/sed resolve pra todos: sed -i '' 's|href="style.css"|href="../style.css"|g; s|src="assets/|src="../assets/|g' meu-deck/slides/*.html)

# 4. Edite copy + dados em cada slide (1 slide por vez, validar visualmente)

# 5. Publique (opcional)
python3 build-deck-inlined.py --slides meu-deck/slides --assets meu-deck/assets \
  --index templates-short-deck/index.html --out meu-deck/build/inlined.html \
  --title "Meu Deck"
```

**Vantagens dessa estrutura:**

- Cada slide é independente → editar, versionar e revisar 1 por vez.
- `style.css` único → 1 lugar pra mexer em tokens.
- `assets/` centralizado → 1 lugar pra mexer em imagens.
- `index.html` auto-contido → abre no browser sem servidor.
- Funciona idêntico nas pastas `templates-short-deck/` e `templates-expanded-deck/`.

---

## Onde está o quê

- **Regras firmes** (canvas, paleta, tipografia, restrições) → [`AGENTS.md`](AGENTS.md)
- **Prosa, exemplos, fluxo, padrões de bug** → [`playbook.md`](playbook.md)
- **Catálogo do deck curto (52)** + GUIA detalhada → [`templates-short-deck/`](templates-short-deck/) (especialmente [`templates-short-deck/GUIA.md`](templates-short-deck/GUIA.md))
- **Catálogo do deck expandido (109)** + GUIA detalhada → [`templates-expanded-deck/`](templates-expanded-deck/) (especialmente [`templates-expanded-deck/GUIA.md`](templates-expanded-deck/GUIA.md))
- **Como exportar PDF** → [`docs/EXPORT-PDF.md`](docs/EXPORT-PDF.md)
- **Como customizar templates** → [`docs/CUSTOMIZE.md`](docs/CUSTOMIZE.md)
- **Identidade G4 Next** → [`id-next/README.md`](id-next/README.md)
- **Identidade G4 Scale** → [`id-scale/README.md`](id-scale/README.md)
- **Identidade G4 Club** → [`id-club/README.md`](id-club/README.md)

---

## Licença

MIT — use, modifique, distribua. Mantenha os créditos.
