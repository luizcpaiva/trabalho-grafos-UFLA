import re
from itertools import combinations
import numpy as np


class GrafoProcessor:
    def __init__(self, arquivo_path):
        self.arquivo_path = arquivo_path
        self.info = {}
        self.nos = {}
        self.arestas_obrig = []
        self.arestas_opcionais = []
        self.arcos_obrig = []
        self.arcos_opcionais = []
        self.total_nos = 0

    def processar_arquivo(self):
        self._extrair_metadados()
        self._processar_conteudo()
        self._organizar_dados()
        return self.info, self.total_nos

    def _extrair_metadados(self):
        padroes = {
            'nome': r'Nome:\s+(\S+)',
            'valor_otimo': r'Valor ótimo:\s+(-?\d+)',
            'veiculos': r'Veículos:\s+(-?\d+)',
            'capacidade': r'Capacidade:\s+(\d+)',
            'deposito': r'Depósito:\s+(\d+)',
            'nos': r'Nós:\s+(\d+)',
            'arestas': r'Arestas:\s+(\d+)',
            'arcos': r'Arcos:\s+(\d+)',
            'nos_obrig': r'Nós obrigatórios:\s+(\d+)',
            'arestas_obrig': r'Arestas obrigatórias:\s+(\d+)',
            'arcos_obrig': r'Arcos obrigatórios:\s+(\d+)'
        }

        with open(self.arquivo_path, 'r') as f:
            for linha in f:
                for chave, padrao in padroes.items():
                    match = re.search(padrao, linha)
                    if match:
                        valor = match.group(1)
                        self.info[chave] = int(valor) if valor.isdigit() else valor

        self.total_nos = self.info.get('nos', 0)

    def _processar_conteudo(self):
        secao_atual = None
        
        with open(self.arquivo_path, 'r') as f:
            for linha in f:
                linha = linha.strip()
                
                if linha.startswith('ReN.'):
                    secao_atual = 'nos'
                elif linha.startswith('ReE.'):
                    secao_atual = 'arestas_obrig'
                elif linha.startswith('ReA.'):
                    secao_atual = 'arcos_obrig'
                elif linha.startswith('EDGE'):
                    secao_atual = 'arestas_opcionais'
                elif linha.startswith('ARC'):
                    secao_atual = 'arcos_opcionais'
                elif not linha:
                    continue
                else:
                    self._processar_linha(linha, secao_atual)

    def _processar_linha(self, linha, secao):
        partes = linha.split()
        
        if secao == 'nos' and len(partes) == 3:
            id_no = int(partes[0][1:])
            self.nos[id_no] = {
                'demanda': int(partes[1]),
                'custo': int(partes[2])
            }
            
        elif secao == 'arestas_obrig' and len(partes) == 6:
            self.arestas_obrig.append((
                int(partes[1]), int(partes[2]),
                int(partes[3]), int(partes[4]),
                int(partes[5])
            ))
            
        elif secao == 'arestas_opcionais' and len(partes) == 4:
            self.arestas_opcionais.append((
                int(partes[1]), int(partes[2]),
                int(partes[3])
            ))
            
        elif secao == 'arcos_obrig' and len(partes) == 6:
            self.arcos_obrig.append((
                int(partes[1]), int(partes[2]),
                int(partes[3]), int(partes[4]),
                int(partes[5])
            ))
            
        elif secao == 'arcos_opcionais' and len(partes) == 4:
            self.arcos_opcionais.append((
                int(partes[1]), int(partes[2]),
                int(partes[3])
            ))

    def _organizar_dados(self):
        self.info.update({
            'nos': self.nos,
            'arestas_obrig': self.arestas_obrig,
            'arestas_opcionais': self.arestas_opcionais,
            'arcos_obrig': self.arcos_obrig,
            'arcos_opcionais': self.arcos_opcionais
        })


class AnalisadorGrafo:
    @staticmethod
    def calcular_distancias(grafo, n_nos):
        INF = float('inf')
        dist = [[INF] * n_nos for _ in range(n_nos)]
        prox = [[-1] * n_nos for _ in range(n_nos)]
        
        for i in range(n_nos):
            dist[i][i] = 0

        for aresta in grafo['arestas_obrig'] + grafo['arestas_opcionais']:
            origem, destino, custo = aresta[:3]
            origem_idx = origem - 1
            destino_idx = destino - 1
            dist[origem_idx][destino_idx] = custo
            dist[destino_idx][origem_idx] = custo
            prox[origem_idx][destino_idx] = destino_idx
            prox[destino_idx][origem_idx] = origem_idx

        for k in range(n_nos):
            for i in range(n_nos):
                for j in range(n_nos):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        prox[i][j] = prox[i][k]

        return dist, prox

    @staticmethod
    def calcular_centralidade(dados, n_nos):
        dist, prox = AnalisadorGrafo.calcular_distancias(dados, n_nos)
        betweenness = {i: 0 for i in range(1, n_nos + 1)}
        
        for u, v in combinations(range(n_nos), 2):
            if dist[u][v] == float('inf'):
                continue
                
            caminho = []
            atual = u
            while atual != v:
                caminho.append(atual + 1)
                atual = prox[atual][v]
            caminho.append(v + 1)
            
            for no in caminho[1:-1]:
                betweenness[no] += 1
                
        return betweenness

    @staticmethod
    def calcular_metricas(matriz_dist):
        diametro = 0
        soma_distancias = 0
        contagem = 0
        
        for i in range(len(matriz_dist)):
            for j in range(len(matriz_dist)):
                if i != j and matriz_dist[i][j] != float('inf'):
                    diametro = max(diametro, matriz_dist[i][j])
                    soma_distancias += matriz_dist[i][j]
                    contagem += 1
                    
        caminho_medio = soma_distancias / contagem if contagem else float('inf')
        return diametro, caminho_medio

    @staticmethod
    def gerar_relatorio(dados, n_nos):
        relatorio = {}
        
        # Cálculos básicos
        relatorio["Vértices totais"] = n_nos
        relatorio["Arestas"] = dados.get('arestas', 0)
        relatorio["Arcos"] = dados.get('arcos', 0)
        relatorio["Vértices obrigatórios"] = dados.get('nos_obrig', 0)
        relatorio["Arestas obrigatórias"] = len(dados['arestas_obrig'])
        relatorio["Arcos obrigatórios"] = len(dados['arcos_obrig'])
        
        # Cálculo de graus
        graus = {i: 0 for i in range(1, n_nos + 1)}
        for aresta in dados['arestas_obrig'] + dados['arestas_opcionais']:
            graus[aresta[0]] += 1
            graus[aresta[1]] += 1
            
        relatorio["Grau mínimo"] = min(graus.values()) if graus else 0
        relatorio["Grau máximo"] = max(graus.values()) if graus else 0
        
        # Outras métricas
        relatorio["Direcionado"] = bool(dados.get('arcos', 0))
        
        n = n_nos
        m = relatorio["Arestas"]
        relatorio["Densidade"] = (2 * m) / (n * (n - 1)) if n > 1 else 0
        
        distancias, _ = AnalisadorGrafo.calcular_distancias(dados, n_nos)
        relatorio["Centralidade"] = AnalisadorGrafo.calcular_centralidade(dados, n_nos)
        diametro, caminho_medio = AnalisadorGrafo.calcular_metricas(distancias)
        relatorio["Diâmetro"] = diametro
        relatorio["Caminho médio"] = caminho_medio
        
        return relatorio


def analisar_instancia(caminho_arquivo):
    processor = GrafoProcessor(caminho_arquivo)
    dados_grafo, total_nos = processor.processar_arquivo()
    return AnalisadorGrafo.gerar_relatorio(dados_grafo, total_nos)