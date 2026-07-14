# Core Slides G4 · short-deck (52 slides)

O **deck curto** da G4: 52 templates, linguagem visual "Órbita" (editorial-orgânica, inspirada na landing do G4 OS e na rox.com). É o ponto de partida para qualquer projeto — aulas, workshops, talks, decks institucionais enxutos. Se o seu projeto precisa de algo mais (case study, financeiro, pitch de vendas, produto), pule para [`templates-expanded-deck/`](../templates-expanded-deck/README.md).

> **Histórico de naming:** esta pasta se chamava `templates-v5/`. Renomeada em 2026-07-09 para que o nome descreva o **propósito** (deck curto) em vez da versão. Os slides são os mesmos.

## Linguagem "Órbita"

- **Serif display** (Playfair Display) com itálico dourado na palavra-chave
- **Superfícies suaves**: radius 22px, borda sutil, sombra em camadas — conteúdo denso vive dentro de cards, não solto
- **Chips/pills** para meta, legendas e deltas (verde/vermelho para tendências)
- **Esfera armilar da marca** (`.armilar` sólida / `.armilar--engraving` gravura) como overlay decorativo — PNGs pré-tingidos por modo em `assets/` (ice para navy, slate para paper); halo dourado (`.glow`), grain de filme (`.grain`), linha-eco fantasma (`.ghost`)
- **Números** em Space Grotesk, corpo em IBM Plex Sans, labels em IBM Plex Mono
- Paleta da marca mantida: paper `#F5F4F3` · navy `#001F35–#001525` · gold `#B9915B` (dark usa `#C9A05C`)

**Guia completo de uso/edição (para humanos e IAs): [GUIA.md](GUIA.md)** — tokens, padrões de código, catálogo slide a slide e checklist de QA.

## Uso

```bash
open index.html        # passador: grid de cards + modo apresentação (setas/espaço/Esc)
cp 06-grafico-barras.html meu-slide.html   # copie o mais próximo e edite
```

Funciona direto via `file://` — slides e index no mesmo diretório.

## Os 52 slides

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

**Nota do topo**: o `data-section` é só metadado — NÃO renderiza nada. O único kicker visível é o `.eyebrow` do título.

Regras herdadas da lib: canvas fixo 1600×900 com `fit()`, `data-section` como kicker automático, dourado com parcimônia (1 protagonista por slide), sem emoji, placeholder de foto documentado em comentário no arquivo.

## Próximo passo

Se você precisa de layouts para **case study**, **relatório financeiro**, **pitch de vendas** ou **apresentação de produto**, vá para [`templates-expanded-deck/`](../templates-expanded-deck/README.md) — tem os mesmos 52 + 57 templates extras (109 no total), mesma linguagem "Órbita", só mais opções.

A lib v4 (48 templates, estilo hairline) segue intacta em [`templates-legacy/`](../templates-legacy/).
