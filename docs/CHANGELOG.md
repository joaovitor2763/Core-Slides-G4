# Changelog — Core Slides G4

## Identity variants — 2026-07-14

**Três skins completas sobre as coleções oficiais Órbita.** Cada pasta replica `templates-short-deck`, `templates-expanded-deck` e `deck-frameworks`, preservando os tipos de slide e adaptando o sistema visual à unidade de negócio.

- **`id-next/` — G4 Next**: Libre Baskerville + Manrope, petróleo profundo, vinho como accent, logos e armilares Next, além de backgrounds orgânicos próprios.
- **`id-scale/` — G4 Scale**: Libre Baskerville + Manrope, azul petróleo como accent protagonista, rubi pontual nos títulos claros, logos Scale e família de frisos verticais.
- **`id-club/` — G4 Club**: Libre Baskerville + Manrope, navy quase-preto, gold da marca, logo Club e backgrounds letterpress "CLUB".
- Cada identidade inclui README próprio, catálogos navegáveis, folhas de estilo e assets locais. Templates de identidades diferentes não devem compartilhar `style.css` ou `assets/`.

## v5.0 "Órbita" — 2026-07-02

**Nova geração da biblioteca em `templates-v5/` (50 slides + index.html próprio).** A v4 permanece intacta em `templates/` como acervo.

- **Nova linguagem visual** (inspirada na landing do G4 OS e na rox.com): serif Playfair Display com itálico dourado, superfícies com radius 22px + sombra em camadas, chips/pills, ghost text, grain e **gravura da esfera armilar** como assinatura do canto inferior direito (PNGs pré-tingidos por modo em `templates-v5/assets/`).
- **50 slides**: capa, divisores, mentor/equipe, quotes (4 tipos), agenda, cronograma multi-dia, 9 tipos de gráfico (barras, linha, donut, pizza, radar, progresso, comparativas, linhas competindo, empilhadas 100%), KPIs, stats, bentos, split, matriz 2×2, timeline, fluxo ramificado, ciclos, frameworks (camadas, Venn, triângulo, polos, concêntricos, árvore/BSC), mockup de laptop, tabelas (decisão + dados), checklist, roadmap, manifesto, perguntas, pricing, prova social e encerramento.
- **`templates-v5/GUIA.md`** — guia completo para humanos e IAs: tokens, padrões de código (escalas de gráfico comentadas, conectores com dots, spec da gravura), catálogo slide a slide e checklist de QA.
- Decisões de linguagem: `data-section` virou metadado puro (não renderiza), halos radiais (`.glow`) proibidos, cache-buster `style.css?v=` nos links.

## v4.0 — 2026-07-02

**Expansão da biblioteca: 20 → 48 templates.**

- **Templates 26-34** (portados do deck `founder-ia-conteudo`): quote galeria split, mentor hero, transição aceleradores, bento comparativo, grid de ferramentas, narrativa numérica, bento de métricas, três pilares percentuais (dark), encerramento quote (dark)
- **Templates 35-48** (expansão v4):
  - Gráficos: 35 linha (SVG inline), 36 donut (`conic-gradient`), 37 barras duplas, 38 progresso, 46 funil
  - Imagens: 39 full-bleed + overlay (dark), 40 hero lateral 38% com edge-blend, 41 galeria duo (moldura mat)
  - Quotes: 42 post/tweet, 43 quote dupla
  - Comparação/prática: 44 tabela comparativa, 45 checklist fazer × evitar, 47 exercício em passos com tempos, 48 número hero
- **Variantes dark completadas** para 27-32 (todos os templates agora têm par light/dark, exceto os dark-únicos 08, 20, 33, 34, 39)
- **`examples/catalog.html`** — catálogo navegável dos 48 templates com filtro por categoria e toggle light/dark
- **`assets/patterns/overlay-raios.png`** — overlay decorativo de raios portado do deck founder-ia (capas/divisores/encerramentos dark)
- **Playbook** §5 atualizado (tabela dos 48), §7.9/7.10 (faixa reservada do data-section; orçamento de accent em colunas repetidas), §7B (tratamentos de imagem)
- **Fixes**: template 30 (eyebrow local sobrepunha o `data-section`), template 31 (3 números gold → só a coluna `.lead`; vácuo vertical reduzido)

## v4.1 — 2026-07-02 (auditoria pós-expansão)

- **FIX crítico de contraste dark**: 20 variantes dark da v3 usavam `color: var(--ink)` (token cru, não flipava) → letra preta em fundo navy. Corrigido no design system: `.mode-dark` agora flipa também os tokens crus (`--ink`, `--ink-2`, `--muted`, `--rule`). Texto escuro intencional sobre painel gold/paper usa `var(--on-accent)` ou hex explícito (22-dark ajustado).
- **FIX serif fantasma**: `Cormorant Garamond` era usada (26/34) sem ser carregada → fallback genérico. Agora vem no `@import` do `style.css`.
- **FIX redundância**: 4 templates (15, 22, 26, 27) tinham `data-section` idêntico ao eyebrow local (texto duplicado no slide). Regra nova: data-section = seção do deck; eyebrow = tema do slide.
- **43-quote-dupla**: quotes em Cormorant serif 44px (caráter editorial da família de quotes) no lugar de sans 30px.
- **31-narrativa-numerica**: placeholders fracos ("+1σ", "↗", "Headline do primeiro sinal") substituídos por narrativa real (9h → 62% → 2,4×).
- **37-barras-duplas**: barras alargadas (88 → 128px).

## v3.0 — 2026-06-26

**Primeira release pública.**

- **20 templates canônicos** validados (01-20) em `templates/`
- **`style.css` compartilhado** com paleta navy + gold, 3 famílias de fonte (Space Grotesk + IBM Plex Sans + IBM Plex Mono)
- **`AGENTS.md`** consolidado com regras firmes (canvas 1600×900, accent único, modo dark, etc)
- **`playbook.md`** com prosa + exemplos + padrões de bug
- **`examples/index.html`** — passador de slides funcional
- **`assets/`** — logos, patterns e imagens exemplo
- **`docs/EXPORT-PDF.md`** — técnica de export PDF via Chrome headless
- **`docs/PUBLISH.md`** — publicação no g4os-pages
- **`docs/CUSTOMIZE.md`** — padrões de customização + bugs comuns
- **Licença MIT**

### Proveniência

| Sessão | Contribuição |
|---|---|
| `260614-awake-grove` | Design system v1 + 15 templates |
| `260614-apt-nebula` | Tokens semânticos no CSS |
| `260615-sunny-dolphin` | 1ª aula (G4 Academia de IA, 29 slides) |
| `260615-awake-creek` | Técnica de export PDF (Chrome headless 1 slide por vez) |
| `260623-misty-lake` | 2ª aula (G4 Gestão e Estratégia) + 5 templates novos (16-20) + publicação g4os-pages |

### Aprendizados canônicos consolidados (do `playbook.md`)

- Slide 16: número da barra precisa estar **dentro do `.stem`** (não do `.bar-v`)
- Slide 14: reservar `top:380+` antes de grids horizontais
- Slide 15: `max-width = (1600 - 96*2) - rail - gap` antes de chutar
- Slide 13: padding da lista = `(900 - top - footer) / n_itens`
- Slide 19: `flex: 1` em flex-direction:column cria vácuo invisível — usar `space-between` no parent
- Slide 6 (vídeo): comprimir MP4 com ffmpeg `crf 28 scale=-2:480` (33MB → 600KB)
- Passador publicado: cada slide precisa ter `style.css` inline também (srcdoc não herda)
- Passador publicado: `ifr.setAttribute('srcdoc', s.html)` em vez de template literal (evita quebra de aspas)

### Mudanças v2 → v3

- **Removido `data-page` do design system** (contagem de slides não é fixa, slides são reaproveitados)
- **Navy-600** virou bg dark (substituindo navy-700 que era muito profundo)
- **Gold accent** voltou pro dourado queimado `#B9915B` (após teste de "royal gold" que ficou pálido demais)
- **`Cormorant Garamond` serif** adicionado pra capa + divisor + perguntas dark (editorial weight)
- **5 templates novos** (16-20): grafico-vertical, a-vs-b, bento, stepper, quote-hero
