import sys
import time

# Função para busca em profundidade
def busca_profundidade(grafo, vertice, visitados=set()):
    visitados.add(vertice)
    for vizinho in grafo.get(vertice, []):
        if vizinho not in visitados:
            busca_profundidade(grafo, vizinho, visitados)

# Grafo de exemplo
grafo = {
    0: [1],
    1: [2, 3, 4],
    2: [5, 6],
    3: [7, 8],
    4: [9, 10],
    5: [11],
    7: [12, 13],
    8: [14],
    10: [15, 16, 17],
    11: [18, 19, 20],
    17: [21, 22]
}

# Obtendo o uso de memória antes da execução
antes_memoria = sys.getsizeof(grafo)

# Executando a busca em profundidade
inicio_tempo = time.time()
busca_profundidade(grafo, 0)
fim_tempo = time.time()

# Obtendo o uso de memória após a execução
depois_memoria = sys.getsizeof(grafo)

# Calculando o uso de memória total
uso_memoria = depois_memoria - antes_memoria

# Calculando o tempo total de execução
tempo_total = fim_tempo - inicio_tempo

# Imprimindo os resultados
print("Uso de memória total:", uso_memoria, "bytes")
print("Tempo total de execução:", tempo_total, "segundos")