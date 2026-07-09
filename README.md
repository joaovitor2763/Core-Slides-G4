# Core Slides G4

> **Two decks, one language.** Build G4 slides by picking the deck that matches your project size — not by version number. All official templates share the **"Órbita"** visual language (Playfair serif + Space Grotesk display, navy + gold + paper, sphere armilar overlay, surfaces with radius + soft shadow, chips/pills for meta).

## The two official decks

| Deck | Slides | Use it for |
|---|---|---|
| **[`templates-short-deck/`](templates-short-deck/README.md)** | **52** | Lean projects — aulas, workshops, talks, internal decks. The minimum viable G4. **Start here.** |
| **[`templates-expanded-deck/`](templates-expanded-deck/README.md)** | **109** | Everything: case study (8 etapas), relatório financeiro (DRE, fluxo de caixa, orçamento, cenários, mapa de riscos), pitch de vendas, apresentação de produto. Same language as short-deck, more layouts. |

> **Decisão prática:** se você não sabe qual escolher, vá de `short-deck` (52). Ele cobre 90% dos projetos. Se faltar layout (ex: você precisa de um slide de fluxo de caixa), promova o deck para `expanded-deck` e copie o template extra que falta.

---

## Quick start

```bash
# 1. Clone o repo
git clone https://github.com/joaovitor2763/Core-Slides-G4.git
cd Core-Slides-G4

# 2. Abra o passador do deck escolhido no browser
open templates-short-deck/index.html
# (ou: open templates-expanded-deck/index.html)

# 3. Copie o template mais próximo do seu slide
cp templates-short-deck/06-grafico-barras.html meu-slide.html

# 4. Edite copy + dados + CSS local
#    (use tokens do templates-short-deck/style.css — ou do expanded-deck)

# 5. Valide visualmente
open meu-slide.html

# 6. Publique (opcional)
#   - PDF: docs/EXPORT-PDF.md (Chrome headless, 1 slide por vez)
#   - Web: docs/PUBLISH.md (g4os-pages, deck-inlined ≤5MB)
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

Detalhes completos por template (anatomia, quando NÃO usar, customização): [`templates-short-deck/GUIA.md`](templates-short-deck/GUIA.md) ou [`templates-expanded-deck/GUIA.md`](templates-expanded-deck/GUIA.md).

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

## Estrutura do repo

```
Core-Slides-G4/
├── README.md                    ← este arquivo
├── AGENTS.md                    ← regras firmes (canvas, paleta, tipografia, restrições)
├── playbook.md                  ← prosa + exemplos + fluxo de uso + padrões de bug
├── LICENSE                      ← MIT
│
├── build-deck-inlined.py        ← builda um deck HTML único (≤5MB) pra publicar
│
├── templates-short-deck/        ← 52 slides Órbita (deck curto)
├── templates-expanded-deck/     ← 109 slides Órbita (deck expandido)
│
├── examples/
│   ├── index.html               ← passador de slides (base do build, 2 colunas)
│   └── catalog.html             ← catálogo navegável
│
├── assets/                      ← logos, padrões, imagens exemplo
│   ├── logos/                   ← g4-logo-branca.svg
│   ├── patterns/                ← pattern-shield, pattern-symbol
│   └── images/                  ← imagens exemplo
│
└── docs/
    ├── EXPORT-PDF.md            ← Chrome headless, 1 slide por vez
    ├── PUBLISH.md               ← g4os-pages, deck-inlined, ≤5MB
    ├── CUSTOMIZE.md             ← como criar variantes dos templates
    └── CHANGELOG.md             ← histórico de iterações
```

---

## Onde está o quê

- **Regras firmes** (canvas, paleta, tipografia, restrições) → [`AGENTS.md`](AGENTS.md)
- **Prosa, exemplos, fluxo, padrões de bug** → [`playbook.md`](playbook.md)
- **Catálogo do deck curto (52)** + GUIA detalhada → [`templates-short-deck/`](templates-short-deck/) (especialmente [`templates-short-deck/GUIA.md`](templates-short-deck/GUIA.md))
- **Catálogo do deck expandido (109)** + GUIA detalhada → [`templates-expanded-deck/`](templates-expanded-deck/) (especialmente [`templates-expanded-deck/GUIA.md`](templates-expanded-deck/GUIA.md))
- **Como exportar PDF** → [`docs/EXPORT-PDF.md`](docs/EXPORT-PDF.md)
- **Como publicar no g4os-pages** → [`docs/PUBLISH.md`](docs/PUBLISH.md)
- **Como customizar templates** → [`docs/CUSTOMIZE.md`](docs/CUSTOMIZE.md)
- **Changelog** → [`docs/CHANGELOG.md`](docs/CHANGELOG.md)

---

## Proveniência

Sessões-chave que produziram este repo:

| Sessão | Contribuição |
|---|---|
| `260614-awake-grove` | Design system v1 + 15 templates canônicos |
| `260615-sunny-dolphin` | 1ª aula (G4 Academia de IA) — 29 slides |
| `260615-awake-creek` | Técnica de export PDF (Chrome headless 1 slide por vez) |
| `260623-misty-lake` | 2ª aula (G4 Gestão e Estratégia) + 5 templates novos + publicação g4os-pages |
| `deck founder-ia-conteudo` | Templates 26-34 + padrões de imagem (moldura mat, hero lateral, overlay) |
| `expansão v4 (2026-07)` | Templates 35-48 + darks 27-32 + catálogo navegável |
| `geração Órbita (2026-07-07)` | Nova linguagem visual editorial-orgânica. 52 templates no `templates-short-deck/`. |
| `expansão Órbita (2026-07-07)` | +57 templates organizados em 10 categorias no `templates-expanded-deck/` (109 total). |
| `rebrand de folders (2026-07-09)` | `templates-v5/ → templates-short-deck/`, `templates-v6/ → templates-expanded-deck/`. README reescrito como "Two decks, one language". |

**Projeto**: `Aulas G4 - IA` (id: `project_c1402fb9-6848-4cea-9fef-489da1fbf7fe`)

---

## Licença

MIT — use, modifique, distribua. Mantenha os créditos.
