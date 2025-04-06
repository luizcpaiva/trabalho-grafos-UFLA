import re
import itertools
import numpy as np
from collections import defaultdict, deque

def carregar_instancia(caminho):
    with open(caminho, 'r') as f:
        linhas = f.readlines()

    grafo = {}
    vertices = {}
    obrigatorias = []
    opcionais = []
    arcos_req = []
    arcos_opc = []

    padroes = {
        'nome': r'Name:\s+(\S+)',
        'valor_otimo': r'Optimal value:\s+(-?\d+)',
        'veiculos': r'#Vehicles:\s+(-?\d+)',
        'capacidade': r'Capacity:\s+(\d+)',
        'deposito': r'Depot Node:\s+(\d+)',
        'num_vertices': r'#Nodes:\s+(\d+)',
        'num_arestas': r'#Edges:\s+(\d+)',
        'num_arcos': r'#Arcs:\s+(\d+)',
        'vertices_req': r'#Required N:\s+(\d+)',
        'arestas_req': r'#Required E:\s+(\d+)',
        'arcos_req': r'#Required A:\s+(\d+)',
    }

    for linha in linhas:
        for chave, regex in padroes.items():
            match = re.search(regex, linha)
            if match:
                valor = match.group(1)
                grafo[chave] = int(valor) if valor.isdigit() or valor.startswith('-') else valor

    n = grafo.get('num_vertices', 0)

    lendo = {
        'vertices': False,
        'arestas_req': False,
        'arestas_opc': False,
        'arcos_req': False,
        'arcos_opc': False,
    }

    for linha in linhas:
        linha = linha.strip()

        if linha.startswith('ReN.'):
            lendo = {chave: False for chave in lendo}
            lendo['vertices'] = True
            continue
        elif linha.startswith('ReE.'):
            lendo = {chave: False for chave in lendo}
            lendo['arestas_req'] = True
            continue
        elif linha.startswith('EDGE'):
            lendo = {chave: False for chave in lendo}
            lendo['arestas_opc'] = True
            continue
        elif linha.startswith('ReA.'):
            lendo = {chave: False for chave in lendo}
            lendo['arcos_req'] = True
            continue
        elif linha.startswith('ARC'):
            lendo = {chave: False for chave in lendo}
            lendo['arcos_opc'] = True
            continue

        dados = linha.split()

        if lendo['vertices'] and len(dados) == 3:
            id_v = int(dados[0][1:])
            vertices[id_v] = {
                'demanda': int(dados[1]),
                'custo_servico': int(dados[2])
            }

        elif lendo['arestas_req'] and len(dados) == 6:
            origem, destino = int(dados[1]), int(dados[2])
            custo, dem, serv = map(int, dados[3:])
            obrigatorias.append((origem, destino, custo, dem, serv))

        elif lendo['arestas_opc'] and len(dados) == 4:
            origem, destino, custo = int(dados[1]), int(dados[2]), int(dados[3])
            opcionais.append((origem, destino, custo))

        elif lendo['arcos_req'] and len(dados) == 6:
            origem, destino = int(dados[1]), int(dados[2])
            custo, dem, serv = map(int, dados[3:])
            arcos_req.append((origem, destino, custo, dem, serv))

        elif lendo['arcos_opc'] and len(dados) == 4:
            origem, destino, custo = int(dados[1]), int(dados[2]), int(dados[3])
            arcos_opc.append((origem, destino, custo))

    grafo['vertices'] = vertices
    grafo['arestas_req'] = obrigatorias
    grafo['arestas_opc'] = opcionais
    grafo['arcos_req'] = arcos_req
    grafo['arcos_opc'] = arcos_opc

    return grafo, n

def floyd_warshall(grafo, n_vertices):
    INF = float('inf')
    dist = [[INF] * n_vertices for _ in range(n_vertices)]
    pred = [[-1] * n_vertices for _ in range(n_vertices)]
    
    for i in range(n_vertices):
        dist[i][i] = 0
    
    # Preencher com arestas existentes
    for u, v, custo, *_ in grafo['arestas_req'] + grafo['arestas_opc']:
        dist[u-1][v-1] = custo
        dist[v-1][u-1] = custo
        pred[u-1][v-1] = u-1
        pred[v-1][u-1] = v-1
    
    for u, v, custo, *_ in grafo['arcos_req'] + grafo['arcos_opc']:
        dist[u-1][v-1] = custo
        pred[u-1][v-1] = u-1
    
    # Algoritmo principal
    for k in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    
    return dist, pred

def componentes_conexos(grafo, n_vertices):
    # Construir lista de adjacência
    adj = defaultdict(list)
    for u, v, *_ in grafo['arestas_req'] + grafo['arestas_opc']:
        adj[u].append(v)
        adj[v].append(u)
    for u, v, *_ in grafo['arcos_req'] + grafo['arcos_opc']:
        adj[u].append(v)
    
    visitados = set()
    componentes = []
    
    for v in range(1, n_vertices + 1):
        if v not in visitados:
            # BFS para encontrar componente conexo
            fila = deque([v])
            componente = set()
            while fila:
                node = fila.popleft()
                if node not in visitados:
                    visitados.add(node)
                    componente.add(node)
                    for vizinho in adj.get(node, []):
                        if vizinho not in visitados:
                            fila.append(vizinho)
            if componente:
                componentes.append(componente)
    
    return componentes

def calcular_intermediacao(grafo, n_vertices):
    dist, _ = floyd_warshall(grafo, n_vertices)
    intermediacao = {v: 0 for v in range(1, n_vertices + 1)}
    INF = float('inf')
    
    for s in range(n_vertices):
        for t in range(n_vertices):
            if s == t or dist[s][t] == INF:
                continue
            # Encontrar todos os caminhos mínimos entre s e t
            caminhos = encontrar_caminhos_minimos(grafo, s+1, t+1, dist)
            for caminho in caminhos:
                for node in caminho[1:-1]:  # Excluir origem e destino
                    intermediacao[node] += 1
    
    # Normalizar
    total_pares = n_vertices * (n_vertices - 1)
    if total_pares > 0:
        for v in intermediacao:
            intermediacao[v] /= total_pares
    
    return intermediacao

def encontrar_caminhos_minimos(grafo, origem, destino, dist):
    # Implementação simplificada para encontrar um caminho mínimo
    # Em uma implementação real, precisaríamos de um algoritmo mais completo
    caminhos = []
    n_vertices = len(dist)
    INF = float('inf')
    
    if dist[origem-1][destino-1] == INF:
        return caminhos
    
    # Usando DFS para encontrar um caminho mínimo
    pilha = [(origem, [origem])]
    while pilha:
        node, caminho = pilha.pop()
        if node == destino:
            caminhos.append(caminho)
            continue
        for v in range(1, n_vertices + 1):
            if v != node and dist[node-1][v-1] + dist[v-1][destino-1] == dist[node-1][destino-1]:
                if v not in caminho:
                    pilha.append((v, caminho + [v]))
    
    return caminhos

def gerar_resumo(grafo, n_vertices):
    resumo = {
        'vertices': n_vertices,
        'arestas_total': grafo.get('num_arestas', 0),
        'arcos_total': grafo.get('num_arcos', 0),
        'vertices_req': grafo.get('vertices_req', 0),
        'arestas_req': len(grafo['arestas_req']),
        'arcos_req': len(grafo['arcos_req']),
    }

    graus = {i: 0 for i in range(1, n_vertices + 1)}

    # Contabilizar graus
    for u, v, *_ in grafo['arestas_req'] + grafo['arestas_opc']:
        graus[u] += 1
        graus[v] += 1
    for u, v, *_ in grafo['arcos_req'] + grafo['arcos_opc']:
        graus[u] += 1  # Só conta a saída para arcos direcionados

    # Determinar se é direcionado
    direcionado = (grafo.get('num_arcos', 0) > 0)
    resumo['direcionado'] = direcionado

    # Densidade
    arestas_dir = grafo.get('num_arcos', 0) if direcionado else grafo.get('num_arestas', 0)
    if direcionado:
        densidade = arestas_dir / (n_vertices * (n_vertices - 1)) if n_vertices > 1 else 0
    else:
        densidade = (2 * arestas_dir) / (n_vertices * (n_vertices - 1)) if n_vertices > 1 else 0

    resumo['densidade'] = densidade

    # Grau mínimo e máximo
    graus_lista = list(graus.values())
    resumo['grau_minimo'] = min(graus_lista)
    resumo['grau_maximo'] = max(graus_lista)
    resumo['graus'] = graus

    # Componentes conexos
    componentes = componentes_conexos(grafo, n_vertices)
    resumo['num_componentes'] = len(componentes)
    resumo['componentes'] = componentes

    # Matriz de distâncias e predecessores
    distancias, predecessores = floyd_warshall(grafo, n_vertices)
    resumo['distancias'] = distancias
    resumo['predecessores'] = predecessores

    # Intermediação
    resumo['intermediacao'] = calcular_intermediacao(grafo, n_vertices)

    # Caminho médio e diâmetro
    soma_distancias = 0
    pares_validos = 0
    diametro = 0
    INF = float('inf')
    
    for i in range(n_vertices):
        for j in range(n_vertices):
            if i != j and distancias[i][j] < INF:
                soma_distancias += distancias[i][j]
                pares_validos += 1
                if distancias[i][j] > diametro:
                    diametro = distancias[i][j]
    
    resumo['caminho_medio'] = soma_distancias / pares_validos if pares_validos > 0 else INF
    resumo['diametro'] = diametro if pares_validos > 0 else INF

    return resumo