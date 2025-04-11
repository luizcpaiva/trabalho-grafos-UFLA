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

## Estrutura do Projeto

A organização dos arquivos é a seguinte:

├── grafos.py # Contém funções para leitura de instâncias, processamento de dados e cálculos de métricas. 
├── main.ipynb # Notebook Jupyter que integra a leitura dos dados, os cálculos e a visualização dos grafos. 
├── instancias/ # Diretório com arquivos de instância (ex.: "teste.dat") contendo os dados de entrada. 
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

### 2. Executar o Notebook

- Abra o arquivo `main.ipynb` em um ambiente Jupyter, como:

  - [Jupyter Notebook](https://jupyter.org/)
  - [JupyterLab](https://jupyterlab.readthedocs.io/)
  - Google Colab (com adaptações)

- Execute as células do notebook na ordem apresentada. A sequência principal de operações inclui:

  1. **Leitura do arquivo de instância** com a função `carregar_instancia` do arquivo `grafos.py`
  2. **Geração de um resumo completo** do grafo, com cálculo de métricas e estatísticas
  3. **Visualização gráfica do grafo completo** e dos **componentes conexos**
  4. **Exibição de uma amostra da matriz de distâncias** (caminhos mínimos)

---

### 3. Interpretação dos Resultados

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


