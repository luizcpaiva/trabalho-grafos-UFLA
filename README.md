# Análise e Visualização de Problemas Logísticos em Grafos

Este projeto foi desenvolvido para a disciplina **Grafos e suas Aplicações (GCC262)**, pelos alunos **Sandy Karolina Maciel** e **Luiz Carlos de Paiva Silva**. O trabalho integra conceitos teóricos e práticos da modelagem de problemas logísticos utilizando grafos, com o objetivo de otimizar o fluxo de bens e serviços e melhorar a eficiência operacional.

---

## Sumário

1. [Visão Geral do Projeto](#visão-geral-do-projeto)
2. [Objetivos e Problema Abordado](#objetivos-e-problema-abordado)
3. [Funcionalidades e Metodologia](#funcionalidades-e-metodologia)
   - [Pré-Processamento e Leitura dos Dados](#pré-processamento-e-leitura-dos-dados)
   - [Cálculo de Métricas e Estatísticas](#cálculo-de-métricas-e-estatísticas)
   - [Algoritmos Empregados](#algoritmos-empregados)
   - [Visualização dos Dados e Grafos](#visualização-dos-dados-e-grafos)
   - [Etapa 2: Solução Inicial (Algoritmo Construtivo)](#etapa-2-solução-inicial-algoritmo-construtivo)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Pré-Requisitos e Instalação](#pré-requisitos-e-instalação)
6. [Como Utilizar o Software](#como-utilizar-o-software)
7. [Contribuições e Considerações Finais](#contribuições-e-considerações-finais)

---

## Visão Geral do Projeto

Este projeto explora a modelagem e análise de problemas logísticos utilizando grafos. A implementação contempla a leitura de instâncias de dados, o processamento desses dados para extrair métricas e estatísticas do grafo, bem como a visualização gráfica da rede. A abordagem adotada permite identificar gargalos, otimizar rotas, analisar a eficiência de serviços logísticos e auxiliar na tomada de decisões estratégicas.

---

## Objetivos e Problema Abordado

Em problemas logísticos, a capacidade de gerenciar e otimizar o fluxo de transporte de bens é crucial para aumentar a eficiência e reduzir custos. O problema base deste projeto é definido em um grafo ou multigrafo, onde:

- **Vértices (Nós):** Representam pontos de entrega, interseções ou locais de serviço.
- **Arestas e Arcos:** Representam vias de acesso, onde:
  - **Arestas** tratam de conexões bidirecionais.
  - **Arcos** representam vias de mão única (direcionadas).

Cada conexão possui atributos como custo de viagem, demanda associada e custo de serviço. Um subconjunto dessas conexões é classificado como obrigatório (serviços que devem ser atendidos), e o objetivo final é encontrar um conjunto de rotas para veículos com custo mínimo, respeitando as restrições de capacidade e garantindo que cada demanda seja atendida.

---

## Funcionalidades e Metodologia

### Pré-Processamento e Leitura dos Dados

- **Leitura de Instâncias:**
  A função `carregar_instancia` (localizada em `grafos.py`) é responsável por ler os arquivos de instância. O arquivo contém os detalhes dos vértices, arestas (obrigatórias e opcionais) e arcos, além de parâmetros como número de veículos, capacidade dos veículos e informações específicas sobre o depósito.

- **Modelagem dos Dados:**
  Os dados são organizados em estruturas como dicionários e listas, proporcionando uma representação clara dos atributos de cada vértice e conexão. Essa organização facilita o acesso e a manipulação dos dados para análises subsequentes.

### Cálculo de Métricas e Estatísticas

O software realiza um conjunto abrangente de cálculos sobre o grafo, incluindo:

- **Número de Elementos do Grafo:**
  - Total de vértices, arestas e arcos.
  - Elementos obrigatórios (nós, arestas e arcos).

- **Densidade do Grafo:**
  Mede a relação entre o número de conexões existentes e o número máximo de conexões possíveis, considerando se o grafo é direcionado ou não.

- **Grau dos Vértices:**
  - Grau mínimo e máximo dos vértices.
  - Distribuição do grau para cada vértice (útil para identificar pontos de concentração ou gargalos na rede).

- **Componentes Conexos:**
  Utilizando técnicas de busca em largura (BFS), o software identifica subgrafos conectados, o que é fundamental para analisar a integridade e a coesão da rede.

- **Matriz de Caminhos Mínimos e Predecessores:**
  Implementação do algoritmo de **Floyd-Warshall** para determinar a matriz de distâncias entre todos os pares de vértices e armazenar os predecessores correspondentes. Isso permite:
  - Identificação dos caminhos mais curtos.
  - Cálculo do caminho médio.
  - Determinação do diâmetro do grafo (a maior distância encontrada entre quaisquer dois vértices).

- **Intermediação (Betweenness Centrality):**
  Mede a frequência com que cada nó aparece nos caminhos mais curtos entre os demais vértices. Essa métrica é crucial para identificar nós críticos que podem atuar como pontos de gargalo na rede.

### Algoritmos Empregados

- **Floyd-Warshall:**
  Utilizado para o cálculo de todas as distâncias mínimas e a matriz de predecessores no grafo. Essa abordagem permite extrair diversas métricas essenciais (caminho médio, diâmetro).

- **Busca em Largura (BFS):**
  Empregada na identificação dos componentes conexos, garantindo que cada subgrafo isolado seja corretamente identificado.

- **Algoritmo de Caminhos Mínimos com DFS:**
  Uma versão simplificada é utilizada para encontrar, em alguns casos, os caminhos mínimos específicos para o cálculo da intermediação.

### Visualização dos Dados e Grafos

O notebook `main.ipynb` integra as funcionalidades de leitura e análise com a visualização gráfica, incluindo:

- **Plotagem do Grafo Completo:**
  Exibição do grafo diferenciando:
  - **Arestas Obrigatórias:** Linhas sólidas (por exemplo, azul).
  - **Arestas Opcionais:** Linhas tracejadas (por exemplo, verde).
  - **Arcos:** Linhas pontilhadas (por exemplo, vermelho), indicando direcionalidade.

- **Visualização dos Componentes Conexos:**
  Cada componente é mostrado com uma cor distinta, facilitando a identificação de subredes dentro do grafo.

- **Exibição de Estatísticas:**
  O resumo gerado (incluindo número de elementos, densidade, grau, intermediação, caminho médio e diâmetro) é exibido no console para rápida análise.

---

### Etapa 2: Solução Inicial (Algoritmo Construtivo)

A Fase 2 do projeto focou no desenvolvimento de um **algoritmo construtivo** para o problema de roteamento estudado na Fase 1. Um algoritmo construtivo inicia com uma solução "vazia" e, iterativamente, adiciona elementos a ela até que uma solução completa e válida seja construída, satisfazendo todas as restrições do problema.

Os principais requisitos para a solução gerada nesta etapa são:

* **Capacidade do Veículo:** Nenhuma rota pode ultrapassar a capacidade máxima definida para os veículos.
* **Cobertura de Serviços:** Cada serviço obrigatório (nó, aresta ou arco) deve ser atendido por **exatamente uma rota**.
* **Contagem Única de Demanda/Custo:** Se uma rota passar mais de uma vez por um vértice, aresta ou arco requerido, a demanda e o custo de serviço associados a esse elemento devem ser contados **apenas uma vez** para a rota.

Além disso, todas as instâncias fornecidas foram testadas, e os resultados são salvos no formato padrão `sol-nome_instancia.dat` em uma pasta designada (`solucoes/`).

#### Algoritmo Empregado: Path-Scanning (Heurística Construtiva)

Para atender aos requisitos da Fase 2, foi implementada uma heurística conhecida como **Path-Scanning**. Esta heurística é uma das mais comuns para problemas de roteamento de veículos com demanda em arestas (CARP - *Capacitated Arc Routing Problem*) devido à sua simplicidade e eficácia na geração de soluções iniciais.

O Path-Scanning opera da seguinte forma:

1.  **Inicialização:** Começa-se com um veículo no depósito e uma rota vazia. Todos os serviços obrigatórios (nós, arestas e arcos) são marcados como "pendentes".
2.  **Seleção do Próximo Serviço:** A partir do nó atual do veículo, o algoritmo busca o serviço obrigatório pendente que pode ser alcançado com o menor custo de viagem (utilizando as distâncias mínimas calculadas pelo Floyd-Warshall) e que não excede a capacidade remanescente do veículo.
3.  **Extensão da Rota:**
    * O caminho mais curto do nó atual até o início do serviço selecionado é adicionado à rota.
    * O serviço em si é então percorrido, adicionando seu custo e demanda à rota atual.
    * A aresta/arco/nó do serviço é marcada como "atendida" e removida da lista de serviços pendentes.
    * O nó final do serviço torna-se o novo nó atual do veículo.
4.  **Encerramento da Rota:** Se não houver mais serviços pendentes que possam ser atendidos pelo veículo atual (seja por capacidade ou conectividade), o veículo retorna ao depósito, completando a rota.
5.  **Novo Veículo:** Um novo veículo é despachado do depósito, e o processo se repete até que todos os serviços obrigatórios tenham sido atendidos.

Esta heurística é um **algoritmo construtivo** porque adiciona gradualmente serviços à rota até que todos os requisitos sejam cumpridos, sem a necessidade de reavaliar ou otimizar rotas existentes (o que seria feito em fases subsequentes ou com meta-heurísticas).

#### Código da Solução Construtiva (`etapa2.py`)

O arquivo `etapa2.py` contém a lógica principal para a solução construtiva:

* **Classe `GrafoCARPAdaptado`:** Esta classe atua como uma **camada adaptadora** entre a estrutura de dados do grafo (`grafo_data`) carregada por `grafos.py` e o algoritmo de Path-Scanning. Ela normaliza o acesso a informações como capacidade do veículo, depósito e listas de serviços obrigatórios (nós, arestas, arcos) para que o `path_scanning` possa operá-los de maneira unificada. Além disso, ela encapsula as chamadas para `floyd_warshall` e `encontrar_caminhos_minimos`, garantindo que as distâncias e os caminhos mais curtos estejam sempre disponíveis.
* **Função `path_scanning(grafo_adaptado)`:** Esta é a implementação da heurística Path-Scanning.
    * Ela primeiro organiza todos os serviços obrigatórios (nós, arestas, arcos) em uma lista `servicos_pendentes` e cria um mapeamento (`servico_info`) para suas demandas, custos e extremos, além de atribuir um `mapeamento_id` para uma ordem consistente de seleção.
    * Dentro do *loop* principal que gera cada rota, o algoritmo busca iterativamente o próximo serviço mais próximo que pode ser atendido pelo veículo atual, respeitando a capacidade.
    * Caminhos mínimos são calculados (e adicionados ao custo da rota) para mover o veículo do nó atual até o serviço e, se for uma aresta/arco, percorrer o serviço até seu outro extremo.
    * Após atender um serviço, ele é removido de `servicos_pendentes`.
    * Quando a rota não pode mais adicionar serviços, o veículo retorna ao depósito.
* **Função `criar_id_servicos(grafo_data)`:** Auxiliar para criar IDs únicos e consistentes para cada tipo de serviço obrigatório (nó, aresta, arco). Isso é útil para referenciar os serviços de forma padronizada.
* **Função `salvar_resultado_arquivo(...)`:** Responsável por formatar e salvar a solução gerada pelo Path-Scanning em um arquivo `.dat`, seguindo o padrão de saída especificado pela disciplina (custo total, número de rotas, tempos de execução e detalhes de cada rota, incluindo visitas a depósitos e serviços específicos).

#### Notebook de Execução (`etapa2.ipynb`)

O notebook `etapa2.ipynb` é o *script* executável para a Fase 2:

* Ele carrega as funções essenciais de `grafos.py` e as novas funções e classes de `etapa2.py`.
* Similar ao `main.ipynb`, ele define as pastas de entrada (`instancias/`) e saída (`solucoes/`).
* Ele **itera sobre todos os arquivos `.dat`** presentes na pasta `instancias/`, processando cada um individualmente.
* Para cada instância, ele:
    * Carrega os dados do grafo.
    * Cria uma instância de `GrafoCARPAdaptado`.
    * Mede o tempo de execução do `path_scanning`.
    * Salva o resultado formatado no arquivo de saída correspondente (`sol-nome_instancia.dat`).
* Inclui **tratamento de erros** (`try-except`) para garantir que o processo continue mesmo que ocorram problemas ao carregar ou processar uma instância específica.

Com esta estrutura, o projeto não só realiza a análise e visualização (Fase 1) mas também fornece uma solução construtiva funcional para o problema CARP (Fase 2), gerando resultados para todas as instâncias de teste.

---

## Estrutura do Projeto

A organização dos arquivos é a seguinte:

├── grafos.py # Contém funções para leitura de instâncias, processamento de dados e cálculos de métricas.
├── main.ipynb # Notebook Jupyter que integra a leitura dos dados, os cálculos e a visualização dos grafos.
├── etapa2.py # Contém a classe adaptadora e a implementação da heurística Path-Scanning para a Fase 2.
├── etapa2.ipynb # Notebook Jupyter para execução em massa das instâncias e geração das soluções da Fase 2.
├── instancias/ # Diretório com arquivos de instância (ex.: "teste.dat") contendo os dados de entrada.
├── solucoes/ # Diretório para armazenar os arquivos de solução gerados (ex.: "sol-teste.dat").
└── README.md # Este arquivo de documentação.

Cada componente do projeto foi estruturado para facilitar a manutenção, a expansão e a compreensão do sistema.

---

## Pré-Requisitos e Instalação

### Requisitos

- **Python 3.x**
- **Bibliotecas:**
  - **NumPy:** Para manipulação de arrays e operações matemáticas.
  - **Matplotlib:** Para a criação de gráficos e visualizações.
  - **Bibliotecas Embutidas do Python:** `re`, `itertools`, `collections` (incluindo `deque`).

### Instalação das Dependências

Certifique-se de que o Python 3.x está instalado no seu sistema. Para instalar as bibliotecas externas, abra o terminal e execute:

pip install numpy matplotlib

Recomendação: Utilize ambientes virtuais (como virtualenv, venv ou conda) para isolar e gerenciar as dependências do projeto.



## Como Utilizar o Software

### 1. Preparar os Dados

- Coloque seus arquivos de instância (por exemplo, `teste.dat`) na pasta `instancias/`.

- Cada arquivo deve seguir o formato especificado, com as seguintes seções:

  - **Informações gerais**:
    - Nome da instância
    - Valor ótimo
    - Número de veículos
    - Capacidade dos veículos
    - Nó depósito
    - Número total de nós, arestas e arcos

  - **Seções de dados**:
    - `ReN.` — Vértices obrigatórios
    - `ReE.` — Arestas obrigatórias
    - `EDGE` — Arestas opcionais
    - `ReA.` — Arcos obrigatórios
    - `ARC` — Arcos opcionais

---

### 2. Executar o Notebook para Análise e Visualização (Fase 1)

- Abra o arquivo `main.ipynb` em um ambiente Jupyter, como:

  - [Jupyter Notebook](https://jupyter.org/)
  - [JupyterLab](https://jupyterlab.readthedocs.io/)
  - Google Colab (com adaptações)

- Execute as células do notebook na ordem apresentada. A sequência principal de operações inclui:

  1. **Leitura do arquivo de instância** com a função `carregar_instancia` do arquivo `grafos.py`
  2. **Geração de um resumo completo** do grafo, com cálculo de métricas e estatísticas
  3. **Visualização gráfica do grafo completo** e dos **componentes conexos**
  4. **Exibição de uma amostra da matriz de distâncias** (caminhos mínimos)

  - Quando for executado, irá abrir um campo de texto para você inserir o nome do arquivo que deseja realizar (ex: `instancias/mgval_0.50_10B.dat`) 

---

### 3. Executar o Notebook para Geração de Soluções (Fase 2)

- Abra o arquivo `etapa2.ipynb` em um ambiente Jupyter (Jupyter Notebook, JupyterLab).

- Execute as células do notebook. Este notebook irá automaticamente processar todos os arquivos `.dat` presentes na pasta `instancias/` e salvará as soluções geradas pelo algoritmo Path-Scanning na pasta `solucoes/` no formato `sol-nome_da_instancia.dat`.

- Observe a saída no console para acompanhar o progresso e identificar quaisquer erros no processamento de instâncias específicas.

---

### 4. Interpretação dos Resultados

- Após a execução, será exibido no console um resumo semelhante ao exemplo abaixo:

=== RESUMO DO GRAFO ===
1. Número de vértices: 50
2. Número de arestas: 33
3. Número de arcos: 101
4. Vértices obrigatórios: 44
5. Arestas obrigatórias: 16
6. Arcos obrigatórios: 50
7. É direcionado? Sim
8. Densidade: 0.0412
9. Grau mínimo: 1
10. Grau máximo: 5
11. Número de componentes conexos: 1
12. Caminho médio: 14.00
13. Diâmetro: 37


- Também serão exibidos:
  - Um **gráfico visual do grafo original** (arestas e arcos, obrigatórios e opcionais)
  - Um gráfico com **componentes conexos em cores distintas**
  - Resultados intermediários e **métricas calculadas no console**

- Interpretação dos Resultados do Arquivo `sol-mgval_0.50_10B.dat`

- Custo Total da Solução (1ª Linha): 785
Este é o custo total acumulado de todas as rotas combinadas na solução. Representa a soma dos custos de todas as viagens dos veículos para atender a todos os serviços obrigatórios.

- Número de Rotas (2ª Linha): 4
Indica a quantidade de rotas (ou veículos) utilizados para atender a todos os serviços obrigatórios. Neste exemplo, 4 veículos foram necessários.

- Tempo Total de Execução (3ª Linha): 90219700
Este valor representa o tempo total, em nanossegundos, que levou para o script completar todo o processamento para esta instância, incluindo o carregamento do grafo, a execução do algoritmo e a gravação do arquivo de saída.

- Tempo do Algoritmo Path-Scanning (4ª Linha): 90068100
Este é o tempo de execução, em nanossegundos, especificamente do algoritmo Path-Scanning para encontrar a solução. É o tempo gasto na lógica heurística principal, sem contar o tempo de I/O (leitura/escrita de arquivos).

- Detalhes de Cada Rota (Linhas Seguintes): O formato é `0 1 <ID_ROTA> <DEMANDA_TOTAL_ROTA> <CUSTO_TOTAL_ROTA> <NUM_VISITAS_TOTAL> (<DETALHES_VISITA_1>) (<DETALHES_VISITA_2>) ... (<DETALHES_VISITA_N>)`

## Contribuições e Considerações Finais

Este projeto é fruto do esforço e dedicação dos alunos **Sandy Karolina Maciel** e **Luiz Carlos de Paiva Silva**, desenvolvido no âmbito da disciplina **Grafos e suas Aplicações (GCC262)**, do curso de Sistemas de Informação da **UFLA**.

O trabalho integra teoria e prática na resolução de problemas logísticos, servindo não apenas como entrega acadêmica, mas também como base para futuras pesquisas e aplicações práticas em áreas como:

- Otimização de rotas
- Gestão de redes de transporte
- Análise de conectividade em grafos direcionados e não direcionados

---

## Pontos de Destaque

- ✅ **Integração Teoria-Prática**  
  Aplicação de algoritmos clássicos (como **Floyd-Warshall**) e técnicas de busca para resolver problemas reais baseados em instâncias logísticas complexas.

- 🧠 **Visualização Intuitiva**  
  Geração de gráficos e componentes visuais que facilitam a identificação de **componentes conexos**, análise de **graus**, **densidade**, **diâmetro**, entre outros indicadores estruturais da rede.

- 🔧 **Expansibilidade**  
  O código foi estruturado de forma **modular** (com funções reutilizáveis e separação de responsabilidades), permitindo:
  - Facilidade de manutenção
  - Integrações futuras com novas funcionalidades
  - Adaptação a diferentes tipos de entrada ou representações de grafos


