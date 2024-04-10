import heapq
from collections import deque

# Classe para representar um nó no grafo
class Node:
    def __init__(self, name, heuristic_cost=0):
        self.name = name
        self.neighbors = {}
        self.heuristic_cost = heuristic_cost
        self.actual_cost = float('inf')
        self.parent = None

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost

    def __lt__(self, other):
        # Você pode definir a comparação com base no custo atual mais a heurística
        return (self.actual_cost + self.heuristic_cost) < (other.actual_cost + other.heuristic_cost)


# Função de busca A*
def busca_a_estrela(start, goal):
    open_set = []  # Conjunto de nós a serem avaliados
    closed_set = set()  # Conjunto de nós já avaliados

    start.actual_cost = 0

    heapq.heappush(open_set, (start.heuristic_cost, start))

    while open_set:
        _, current_node = heapq.heappop(open_set)

        if current_node == goal:
            # Se o nó atual é o objetivo, reconstruímos o caminho
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node)

        for neighbor, cost in current_node.neighbors.items():
            if neighbor in closed_set:
                continue

            tentative_actual_cost = current_node.actual_cost + cost

            if tentative_actual_cost < neighbor.actual_cost:
                neighbor.parent = current_node
                neighbor.actual_cost = tentative_actual_cost
                heapq.heappush(open_set, (tentative_actual_cost + neighbor.heuristic_cost, neighbor))
    return None

# Busca em largura
def busca_em_largura(start, goal):
    queue = deque([start])
    visited = set()

    while queue:
        current_node = queue.popleft()
        if current_node == goal:
            # Se o nó atual é o objetivo, reconstruímos o caminho
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        visited.add(current_node)

        for neighbor, _ in current_node.neighbors.items():
            if neighbor not in visited and neighbor not in queue:
                neighbor.parent = current_node
                queue.append(neighbor)
    return None

# Busca em profundidade
def busca_em_profundidade(start, goal):
    stack = [start]
    visited = set()

    while stack:
        current_node = stack.pop()
        if current_node == goal:
            # Se o nó atual é o objetivo, reconstruímos o caminho
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        visited.add(current_node)

        for neighbor, _ in current_node.neighbors.items():
            if neighbor not in visited and neighbor not in stack:
                neighbor.parent = current_node
                stack.append(neighbor)
    return None

# Busca de custo uniforme
def busca_custo_uniforme(start, goal):
    queue = [(0, start)]  # Fila de prioridade (custo, nó)
    visited = set()

    while queue:
        _, current_node = heapq.heappop(queue)
        if current_node == goal:
            # Se o nó atual é o objetivo, reconstruímos o caminho
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        visited.add(current_node)

        for neighbor, cost in current_node.neighbors.items():
            if neighbor not in visited:
                neighbor.parent = current_node
                heapq.heappush(queue, (current_node.actual_cost + cost, neighbor))

    return None

# Busca Gulosa
def busca_gulosa(start, goal):
    queue = [(start.heuristic_cost, start)]  # Fila de prioridade (heurística, nó)
    visited = set()

    while queue:
        _, current_node = heapq.heappop(queue)
        if current_node == goal:
            # Se o nó atual é o objetivo, reconstruímos o caminho
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]

        visited.add(current_node)

        for neighbor, _ in current_node.neighbors.items():
            if neighbor not in visited:
                neighbor.parent = current_node
                heapq.heappush(queue, (neighbor.heuristic_cost, neighbor))

    return None

#funcao para calcular o custo total do caminha achado
def calcular_custo_total(path):
    total_cost = 0
    for i in range(len(path) - 1):
        node = path[i]
        next_node = path[i + 1]
        edge_cost = node.neighbors[next_node]
        total_cost += edge_cost
    return total_cost


'''
A = Node('A', 30)
B = Node('B', 26)
C = Node('C', 21)
D = Node('D', 7)
E = Node('E', 22)
F = Node('F', 36)
G = Node('G', 0)  
H = Node('G', 0)  
'''
# todos os nós
'''A = Node('A', 240)
B = Node('B', 186)
C = Node('C', 182)
D = Node('D', 163)
E = Node('E', 170)
F = Node('F', 150)
G = Node('G', 165)
H = Node('H', 139)
I = Node('I', 120)
J = Node('J', 130)
K = Node('K', 122)
L = Node('L', 104)
M = Node('M', 100)
N = Node('N', 77)
O = Node('O', 72)
P = Node('P', 72)
Q = Node('Q', 65)
R = Node('R', 65)

# Conectando nós
A.add_neighbor(B, 73)
A.add_neighbor(C, 64)
A.add_neighbor(D, 89)
A.add_neighbor(E, 104)
B.add_neighbor(K, 83)
C.add_neighbor(I, 64)
D.add_neighbor(N, 89)
E.add_neighbor(J, 40)
F.add_neighbor(I, 31)
F.add_neighbor(N, 84)
G.add_neighbor(J, 35)
G.add_neighbor(Q, 133)
H.add_neighbor(L, 36)
H.add_neighbor(K, 35)
I.add_neighbor(P, 63)
I.add_neighbor(F, 31)
I.add_neighbor(M, 20)
J.add_neighbor(E, 40)
J.add_neighbor(G, 35)
J.add_neighbor(Q, 80)
J.add_neighbor(N, 53)
K.add_neighbor(H, 35)
L.add_neighbor(I, 28)
L.add_neighbor(P, 63)
L.add_neighbor(H, 36)
M.add_neighbor(I, 20)
M.add_neighbor(O, 50)
N.add_neighbor(F, 84)
N.add_neighbor(J, 53)
N.add_neighbor(D, 89)
O.add_neighbor(R, 72)
O.add_neighbor(M, 50)
O.add_neighbor(P, 41)
P.add_neighbor(L, 63)
P.add_neighbor(R, 65)
P.add_neighbor(O, 41)
R.add_neighbor(O, 72)
R.add_neighbor(Q, 65)
R.add_neighbor(P, 65)'''

A = Node('A', 14)
B = Node('B', 17)
C = Node('C', 12)
D = Node('D', 5)
E = Node('E', 3)
F = Node('F', 5)
F_2 = Node('F_2', 3)
G = Node('G', 1)  
H = Node('H', 0) 

A.add_neighbor(B, 5) 
A.add_neighbor(C, 4) 
B.add_neighbor(F, 10) 
C.add_neighbor(D, 8)
D.add_neighbor(F, 2) 
D.add_neighbor(F_2, 2)
D.add_neighbor(E, 3)
E.add_neighbor(G, 2)
F.add_neighbor(H, 8)
F_2.add_neighbor(G, 3)
G.add_neighbor(H, 1)
B.add_neighbor(A, 5)
C.add_neighbor(A, 4)
F.add_neighbor(B, 10)
D.add_neighbor(C, 8)
F.add_neighbor(D, 2)
F_2.add_neighbor(D, 2)
E.add_neighbor(D, 3)
G.add_neighbor(E, 2)
H.add_neighbor(F, 8)
G.add_neighbor(F_2, 3)
H.add_neighbor(G, 1)

# Executando a busca A*
path = busca_a_estrela(A, H)
if path:
    print("Caminho encontrado usando busca A*:")
    for node in path:
        print(node.name)
    print("Custo do caminho:", calcular_custo_total(path))
else:
    print("Caminho não encontrado usando busca A*")

# Executando a busca em largura
path_bfs = busca_em_largura(A, H)
if path_bfs:
    print("\nCaminho encontrado usando busca em largura:")
    for node in path_bfs:
        print(node.name)
    print("Custo do caminho:", calcular_custo_total(path_bfs))
else:
    print("Caminho não encontrado usando busca em largura")

# Executando a busca em profundidade
path_dfs = busca_em_profundidade(A, H)
if path_dfs:
    print("\nCaminho encontrado usando busca em profundidade:")
    for node in path_dfs:
        print(node.name)
    print("Custo do caminho:", calcular_custo_total(path_dfs))
else:
    print("Caminho não encontrado usando busca em profundidade")

# Executando a busca de custo uniforme
path_uniform_cost = busca_custo_uniforme(A, R)
if path_uniform_cost:
    print("\nCaminho encontrado usando busca de custo uniforme:")
    for node in path_uniform_cost:
        print(node.name)
    print("Custo do caminho:", calcular_custo_total(path_uniform_cost))
else:
    print("Caminho não encontrado usando busca de custo uniforme")

# Executando a busca gulosa
path_greedy = busca_gulosa(A, H)
if path_greedy:
    print("\nCaminho encontrado usando busca gulosa:")
    for node in path_greedy:
        print(node.name)
    print("Custo do caminho:", calcular_custo_total(path_greedy))
else:
    print("Caminho não encontrado usando busca gulosa")