# Core Slides G4 · deck-frameworks "Órbita"

Biblioteca especializada em **frameworks visuais**: ciclos, sistemas, camadas, mapas, modelos de decisão e ferramentas estratégicas. Usa o mesmo canvas, tokens e linguagem visual de `templates-short-deck/` e `templates-expanded-deck/`.

## Como abrir

```bash
open deck-frameworks/index.html
```

O catálogo oferece dois modos:

- **Apresentar:** slide em tela cheia, com navegação por setas, Espaço, Page Up/Down, Home e End.
- **Modo apresentador:** painel com slide atual, próximo slide, notas persistidas no navegador, cronômetro e uma janela separada para o público.

## Catálogo

| # | Arquivo | Quando usar |
|---|---|---|
| 01 | `01-ciclos-interdependentes.html` | Dois loops que trocam informação por um handoff crítico. |
| 02 | `02-escolha-proposta-valor.html` | Escolher um território principal de diferenciação entre seis dimensões. |
| 03 | `03-espectro-proposta-valor.html` | Explicar proposta de valor nos níveis negócio, prospect, produto e conversão. |
| 04 | `04-alavancas-criacao-valor.html` | Organizar seis formas de gerar valor para o cliente. |
| 05 | `05-builder-proposta-valor.html` | Construir uma proposta de valor em seis partes conectadas. |
| 06 | `06-canvas-proposta-valor.html` | Mostrar o encaixe entre mapa de valor e perfil do cliente. |
| 07 | `07-mapa-valor-perfil-cliente.html` | Detalhar a relação bowtie entre oferta e necessidades. |
| 08 | `08-pentagono-cocriacao.html` | Organizar cinco movimentos ao redor de um princípio central. |
| 09 | `09-branding-identidade-marca.html` | Distinguir intenção, expressão e percepção da marca. |
| 10 | `10-processo-de-marca.html` | Explicar um processo de marca em cinco etapas sequenciais. |
| 11 | `11-marca-e-negocio.html` | Conectar estratégia de negócio e estratégia de marca. |
| 12 | `12-mercado-ao-nicho.html` | Mostrar o recorte progressivo de mercado até nicho. |
| 13 | `13-mapa-stakeholders.html` | Mapear grupos de interesse ao redor da organização. |
| 14 | `14-interseccoes-venn.html` | Explicar sobreposições e territórios compartilhados. |
| 15 | `15-elementos-estrategia-marca.html` | Organizar quatro dimensões ao redor de um núcleo estratégico. |
| 16 | `16-piramide-ressonancia.html` | Mostrar uma evolução hierárquica até ressonância. |
| 17 | `17-modelo-branding.html` | Explicar o circuito completo de gestão da marca. |
| 18 | `18-painel-execucao-marca.html` | Acompanhar estágios, progresso e prioridades de implementação. |

## Como escolher o ponto de partida

- **Existe repetição e retorno?** Comece no **01 · Ciclos interdependentes**.
- **Existe uma decisão central cercada por alternativas?** Comece no **02 · Escolha de proposta de valor**.
- **Existem níveis do geral para o específico?** Comece no **03 · Espectro de proposta de valor**.
- **Existem dimensões paralelas e independentes?** Comece no **04 · Alavancas de criação de valor**.
- **Existe uma sequência circular para construir uma ferramenta?** Comece no **05 · Builder de proposta de valor**.
- **Precisa mostrar encaixe entre oferta e cliente?** Use **06 · Canvas** ou **07 · Mapa de valor × perfil**.
- **São cinco movimentos com um princípio no centro?** Use **08 · Pentágono de co-criação**.
- **É um problema de marca?** Explore **09–11** para fundamentos e processo; **15–17** para estratégia e modelo; **18** para execução.
- **Precisa recortar mercado ou mapear atores?** Use **12 · Mercado ao nicho** ou **13 · Stakeholders**.
- **Precisa mostrar sobreposição?** Use **14 · Interseções**.
- **Nenhum deles representa a relação correta?** Crie um novo template, mas reutilize tokens, componentes e padrões de conectores desta pasta.

## Fluxo para um framework novo

1. Escreva em uma frase **qual relação a geometria precisa explicar**.
2. Liste entidades, conexões, direção e hierarquia antes de desenhar.
3. Escolha o template geometricamente mais próximo e copie o arquivo.
4. Troque copy e labels mantendo a geometria; valide o orçamento de espaço.
5. Só então altere posições, raios, ângulos ou caminhos SVG.
6. Documente os cálculos no comentário do CSS e mantenha tudo editável.
7. Abra o HTML no navegador real e revise legibilidade, sequência visual e overflow.
8. Se for reutilizável, numere o arquivo, registre-o no `index.html` e acrescente-o a este catálogo.

## Regras firmes

1. Canvas fixo **1600×900**.
2. Use tokens de `style.css`; não crie uma segunda paleta.
3. Um único protagonista gold por slide.
4. Diagramas devem ter geometria e coordenadas documentadas no comentário do CSS.
5. Conectores terminam em elementos reais; não deixe linhas flutuando.
6. Copy deve caber sem reduzir a escala tipográfica do sistema.
7. Ao adicionar um template, registre `{ file, name }` no array `slides` do `index.html`.
8. Valide o arquivo isolado e depois no catálogo.

## Estrutura de cada slide

Cada template é um HTML independente com:

- `<link rel="stylesheet" href="style.css?v=5.2">`;
- `<article class="slide">` de 1600×900;
- CSS local documentando a geometria;
- `fit()` ao final para escalar o canvas.

Para criar um novo framework, copie o template geometricamente mais próximo, preserve o skeleton e recalcule posições, raios, ângulos e conectores antes de trocar o conteúdo.
