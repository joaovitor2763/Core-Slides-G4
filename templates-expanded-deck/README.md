# Core Slides G4 · expanded-deck (109 templates)

O **deck expandido** da G4: 109 templates, mesma linguagem visual "Órbita" (editorial-orgânica, inspirada na landing do G4 OS e na rox.com), cobrindo aulas, case study, relatório financeiro, pitch de vendas e apresentações de produto.

Inclui **tudo** o que o [`short-deck`](../templates-short-deck/README.md) (52 slides) já entrega, **mais 57 templates extras** para projetos que precisam de layouts mais densos e específicos (case study de 8 etapas, fluxo de caixa, DRE, mapa de riscos, mockups de produto, arquitetura, etc.).

> **Histórico de naming:** esta pasta se chamava `templates-v6/`. Renomeada em 2026-07-09 para que o nome descreva o **propósito** (deck expandido) em vez da versão. Os slides são os mesmos.

> **Copy = Lorem Ipsum de propósito.** Os templates vêm com texto placeholder calibrado ao layout (os comprimentos importam) e números de exemplo que batem com a geometria dos gráficos. Comentários HTML nos slides novos indicam o conteúdo esperado em cada região. Troque o lorem pelo seu conteúdo mantendo comprimentos parecidos.

A linguagem:

- **Serif display** (Playfair Display) com itálico dourado na palavra-chave
- **Superfícies suaves**: radius 22px, borda sutil, sombra em camadas — conteúdo denso vive dentro de cards, não solto
- **Chips/pills** para meta, legendas e deltas (verde/vermelho para tendências)
- **Esfera armilar da marca** (`.armilar` sólida / `.armilar--engraving` gravura) como overlay decorativo — PNGs pré-tingidos por modo em `assets/` (ice para navy, slate para paper); grain de filme (`.grain`), linha-eco fantasma (`.ghost`)
- **Números** em Space Grotesk, corpo em IBM Plex Sans, labels em IBM Plex Mono
- Paleta da marca mantida: paper `#F5F4F3` · navy `#001F35–#001525` · gold `#B9915B` (dark usa `#C9A05C`)

**Guia completo de uso/edição (para humanos e IAs): [GUIA.md](GUIA.md)** — tokens, padrões de código, catálogo slide a slide e checklist de QA.

## Uso

```bash
open index.html        # galeria com filtro por categoria + modo apresentação (setas/espaço/Esc)
cp 06-grafico-barras.html meu-slide.html   # copie o mais próximo e edite
```

Funciona direto via `file://` — slides e index no mesmo diretório.

## Os 109 templates

Categorias do index: **Estrutura** · **Pessoas & Quotes** · **Dados & Gráficos** · **Diagramas & Frameworks** · **Conteúdo & Layouts** · **Aulas & Educação** · **Case Study** · **Financeiro** · **Pitch & Vendas** · **Produto**.

### Base do short-deck (01–52)

Os 52 templates do [`templates-short-deck/`](../templates-short-deck/README.md) — capa, divisor, mentor, gráficos, bento, funil, mentores, etc. Use o link do `short-deck` para o catálogo completo e detalhado dessa base.

| # | Slide | Modo |
|---|-------|------|
| 01 | Capa (rings + grain + serif hero) | dark |
| 02 | Divisor de capítulo (ghost gigante) | dark |
| 03 | Mentor (nome serif 110px + retrato) | dark |
| 04 | Quote editorial + dado que valida | light |
| 05 | Agenda (item atual em gold) | light |
| 06 | Gráfico de barras (surface + barra gradient) | light |
| 07 | Gráfico de linha (SVG curvo + área) | light |
| 08 | Donut + legenda em mini-cards | light |
| 09 | Stats 4× com eco ghost e chips de tendência | light |
| 10 | Antes × depois (card gold elevado) | light |
| 11 | Bento (hero 3,4× + células vidro) | dark |
| 12 | Método em 4 passos (números serif) | light |
| 13 | Imagem hero rotacionada com chip flutuante | dark |
| 14 | Tabela de decisão (coluna recomendada) | light |
| 15 | Funil (pills decrescentes + card taxa) | dark |
| 16 | Encerramento (quote + CTA pill) | dark |
| 17 | Pizza / composição (conic + legenda rica) | light |
| 18 | Radar 5 eixos, 2 séries (SVG) | dark |
| 19 | Barras de progresso (tracks pill) | light |
| 20 | Matriz 2×2 com eixos-seta | light |
| 21 | Timeline horizontal alternada | light |
| 22 | Fluxo ramificado (pills + curvas SVG) | light |
| 23 | Ciclo / anel com callouts | light |
| 24 | Framework de camadas (pirâmide) | dark |
| 25 | Mockup laptop CSS (tela demo G4 OS) | dark |
| 26 | Bento claro 4 células | light |
| 27 | Split antes × depois (navy/paper) | misto |
| 28 | Framework Venn 3 círculos | light |
| 29 | Quote com foto/retrato | dark |
| 30 | Quote mínima 84px | dark |
| 31 | Divisor claro (ghost + gravura armilar) | light |
| 32 | Checklist fazer × evitar | light |
| 33 | Polos comparativos (2 esferas + spokes) | dark |
| 34 | Ciclo de setas | dark |
| 35 | Círculos concêntricos TAM/SAM/SOM | dark |
| 36 | Árvore / hierarquia (BSC) | dark |
| 37 | Cronograma multi-dia | dark |
| 38 | Triângulo estratégico | dark |
| 39 | Manifesto tipográfico | light |
| 40 | Tabela de dados densa | light |
| 41 | Barras comparativas (2 séries) | light |
| 42 | Linhas competindo + gap | light |
| 43 | Cards com ícones SVG | light |
| 44 | Empilhadas 100% | light |
| 45 | Grid de KPIs 2×2 | dark |
| 46 | Roadmap por fases | light |
| 47 | Perguntas da aula | dark |
| 48 | Planos / pricing | dark |
| 49 | Equipe / mentores | dark |
| 50 | Prova social (3 quotes) | light |
| 51 | Conceito + imagem (blocos + ilustração 3:4) | light |
| 52 | Exercício prático (grade de passos + tempo total) | light |

### Expansão (53–109)

Os 57 templates que tornam este o **deck expandido** — 100/101–109 são os layouts novos organizados em 10 categorias. Use o índice abaixo para achar o slide certo pelo tipo de conteúdo, e o `index.html` desta pasta para navegar com filtro de categoria.

**Referências G4 (53–62)** — layouts extraídos de decks reais do G4 (Scale, Mentoring, OS):

| # | Slide | Modo |
|---|-------|------|
| 53 | Programa dois dias (pilares + 2 círculos + agendas laterais) | dark |
| 54 | Hub de entregas (disco central + 8 itens radiais) | dark |
| 55 | Vozes de usuários (retrato + trilho de 4 quotes com ícones) | dark |
| 56 | Grid de casos de uso (2 bandas × 4 col + rótulo lateral) | dark |
| 57 | Módulo de aula (tabs + aprendizados + painel de mentores) | misto |
| 58 | Custo da inação (pergunta + 3 painéis full-bleed) | misto |
| 59 | Convergência A×B (2 lados → moldura central) | dark |
| 60 | Perfil + quote (argumentos + retrato + citação dark) | misto |
| 61 | Galeria de retratos (3 verticais + chips de categoria) | dark |
| 62 | Plano anual (12 meses · sessões + boards + reta final gold) | misto |

**Aulas & Educação (63–71):**

| # | Slide | Modo |
|---|-------|------|
| 63 | Objetivos de aprendizagem (2×2 competências) | light |
| 64 | Conceito no número (definição + exemplo trabalhado) | light |
| 65 | Canvas de exercício (6 campos tracejados) | light |
| 66 | Debate · dois lados (VS + mecânica de sala) | dark |
| 67 | Recap · 5 coisas para lembrar | light |
| 68 | Biblioteca · leituras (estante com 4 capas + como usar) | light |
| 69 | Dinâmica de turma (3 fases + tempo total) | light |
| 70 | Escada de maturidade (5 níveis ascendentes) | light |
| 71 | Quiz · checagem com resposta revelada | dark |

**Case Study (72–78):**

| # | Slide | Modo |
|---|-------|------|
| 72 | Abertura de case (empresa + chips + faixa de stats) | dark |
| 73 | Contexto (situação → complicação → pergunta) | light |
| 74 | Desafio → intervenção (nó + 3 frentes) | light |
| 75 | Resultados (grid antes→depois com deltas) | light |
| 76 | Linha do case (fases M0–M9 + resultado) | light |
| 77 | Aprendizados (3 lições serif) | dark |
| 78 | Evidência · documento anotado | light |

**Financeiro (79–86):**

| # | Slide | Modo |
|---|-------|------|
| 79 | Resumo executivo (KPIs + sustentou/atenção) | light |
| 80 | DRE resumida (tabela real vs plano) | light |
| 81 | Ponte · waterfall EBITDA | light |
| 82 | Metas × realizado (bullet bars) | light |
| 83 | Curva de caixa (breakeven no zero) | light |
| 84 | Orçamento por área (barra 100% + colunas) | light |
| 85 | Cenários (conservador · base · ambicioso) | light |
| 86 | Mapa de riscos (probabilidade × impacto) | dark |

**Pitch & Vendas (87–94, + 58):**

| # | Slide | Modo |
|---|-------|------|
| 87 | O problema · 3 dores com custo | dark |
| 88 | A solução em 3 camadas | light |
| 89 | Mercado · TAM SAM SOM em barras | light |
| 90 | Modelo de receita + unit economics | light |
| 91 | Tração (curva MRR + milestones) | dark |
| 92 | Posicionamento competitivo (scatter) | light |
| 93 | A oferta (âncora de valor + card investimento) | dark |
| 94 | Próximos passos (3 passos com datas) | dark |

**Produto (95–100, + 25):**

| # | Slide | Modo |
|---|-------|------|
| 95 | Mockup celular (chat do produto) | dark |
| 96 | Grade de features 3×2 com ícones | light |
| 97 | Jornada do usuário (curva de valor) | light |
| 98 | Arquitetura (entrada → motor → saída) | dark |
| 99 | Heatmap de adoção (áreas × meses) | light |
| 100 | Plano de trabalho · gantt (4 frentes × 12 semanas) | light |

**Referências G4 · rodada 2 (101–109):**

| # | Slide | Modo |
|---|-------|------|
| 101 | Fases do programa (3 colunas com sub-cards aninhados) | dark |
| 102 | Público-alvo (tiles dark com ícones + nota de alerta) | light |
| 103 | Dois mentores (metades espelhadas dark/light) | misto |
| 104 | Processo em seta (6 etapas numa seta gigante) | dark |
| 105 | Pentágono de pilares (5 vértices + pilar central) | light |
| 106 | Jornada × programas (estágios + barras de programa) | dark |
| 107 | Matriz de programas (áreas × horizonte + badges) | light |
| 108 | Funil horizontal (3 trapézios + seta de base) | misto |
| 109 | Gráfico combo (barras + linha de 2ª série + KPIs) | dark |

**Nota do topo**: o `data-section` é só metadado — NÃO renderiza nada. O único kicker visível é o `.eyebrow`.

Regras herdadas da lib: canvas fixo 1600×900 com `fit()`, dourado com parcimônia (1 protagonista por slide), sem emoji, placeholder de foto documentado em comentário no arquivo.
