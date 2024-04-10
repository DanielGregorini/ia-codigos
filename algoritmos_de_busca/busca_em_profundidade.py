import time

def busca_caminho_profundidade(grafo, vertice_atual, vertice_destino, visitados=set(), caminho=[]):
    #cont: int = 0
    visitados.add(vertice_atual)
    caminho.append(vertice_atual)
    if vertice_atual == vertice_destino:
        return caminho
    for vizinho in grafo.get(vertice_atual, []):
        
        #cont += 1
        #print(cont)
        if vizinho not in visitados:
            resultado = busca_caminho_profundidade(grafo, vizinho, vertice_destino, visitados, caminho)
            if resultado:
                return resultado
    caminho.pop()
    return None

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
vertice_inicial = 1
vertice_destino = 6

inicio = time.time()
caminho_encontrado = busca_caminho_profundidade(grafo1, vertice_inicial, vertice_destino)
fin = time.time()

if caminho_encontrado:
    print(f'Caminho encontrado: {caminho_encontrado}')
else:
    print('Caminho não encontrado')

tempo_total = (fin - inicio) * 1000  # Convert to milliseconds
print(f'Tempo total gasto: {tempo_total:.8f} ms')