# Grafo representando as cidades da Romênia, suas conexões e distâncias entre elas
romenia = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Fagaras': {'Sibiu': 99, 'Bucarest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucarest': 101, 'Craiova': 138},
    'Craiova': {'Rimnicu Vilcea': 146, 'Pitesti': 138, 'Drobeta': 120},
    'Bucarest': {'Fagaras': 211, 'Pitesti': 101}
}

def busca_profundidade_limitada(grafo, inicio, objetivo, limite):
    visitados = set()

    def busca_profundidade_limitada_recursiva(vertice, profundidade):
        if vertice == objetivo:
            return [vertice]
        if profundidade == limite:
            return None
        if vertice not in visitados:
            visitados.add(vertice)
            for vizinho, distancia in grafo.get(vertice, {}).items():
                caminho = busca_profundidade_limitada_recursiva(vizinho, profundidade + 1)
                if caminho is not None:
                    return [(vertice, distancia)] + caminho
        return None

    return busca_profundidade_limitada_recursiva(inicio, 0)

def aprofundamento_iterativo(grafo, inicio, objetivo, limite_maximo):
    for limite in range(1, limite_maximo + 1):
        resultado = busca_profundidade_limitada(grafo, inicio, objetivo, limite)
        if resultado is not None:
            return resultado
    return None

def calcula_soma_distancias(caminho):
    soma = 0
    for i in range(len(caminho) - 1):
        _, distancia = caminho[i]
        soma += distancia
    return soma

# Executar o algoritmo de aprofundamento iterativo com diferentes limites
for limite in [2, 4, 7]:
    print(f"Busca com limite de profundidade {limite}:")
    caminho = aprofundamento_iterativo(romenia, 'Arad', 'Bucarest', limite)
  
    if caminho is not None:
        print("Caminho encontrado:", caminho)
        soma_distancias = calcula_soma_distancias(caminho)
        print("Soma total das distâncias:", soma_distancias)
    else:
        print("Não foi possível encontrar um caminho com o limite especificado.")
    print()

print("----------------------------------------")

for limite in [2, 4, 7]:
    print(f"Busca com aprofundamento iterativo {limite}:")
   
    caminho1 = aprofundamento_iterativo(romenia, 'Arad', 'Bucarest', limite)
    
    if caminho1 is not None:
        print("Caminho encontrado:", caminho)
        soma_distancias = calcula_soma_distancias(caminho)
        print("Soma total das distâncias:", soma_distancias)
    else:
        print("Não foi possível encontrar um caminho com o limite especificado.")
    print()
 
