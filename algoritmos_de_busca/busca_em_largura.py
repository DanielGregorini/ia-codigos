from collections import deque
import time

grafo = {
    0: [1, 2, 5],
    1: [6],
    2: [5, 7],
    5: [1, 6, 7, 8],
    6: [7],
    8: [6]
}

grafo1 = {
    0: [1, 2],
    1: [3],
    2: [1, 3, 4],
    3: [6],
    4: [3, 5, 6],
    5: [],
    6: [],
}


def busca_em_largura(grafo, inicio, objetivo):    
    tempo_inicio = time.time()
    fila = deque([(inicio, [inicio])])
    cont = 0
    while fila:
        cont += 1
        print(cont)
        no, caminho = fila.popleft()
        if no == objetivo:
            tempo_fim = time.time()
            tempo_total = (tempo_fim - tempo_inicio) * 1000
            print(f"Tempo total gasto: {tempo_total:.2f} ms")
            return caminho
        for vizinho in grafo.get(no, []):
            if vizinho not in caminho:
                fila.append((vizinho, caminho + [vizinho]))
    return None

caminho = busca_em_largura(grafo1, 1, 6)

if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Caminho não encontrado.")