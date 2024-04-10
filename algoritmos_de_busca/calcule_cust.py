class Node:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.x = 0  # Defina as coordenadas x e y conforme necessário
        self.y = 0

    def add_neighbor(self, neighbor, distance):
        # Adicione a lógica para adicionar vizinhos conforme necessário
        pass

# Definindo os nós com seus custos
A = Node('A', 240)
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
R = Node('R', 0)

# Conectando nós
# Adicione a lógica para conectar os nós conforme necessário

def calculate_cost(node, goal):
    # Definindo a heurística como a distância em linha reta (hipotenusa)
    dx = abs(node.x - goal.x)
    dy = abs(node.y - goal.y)
    h = (dx**2 + dy**2) ** 0.5  # Distância Euclidiana
    g = node.cost
    f = g + h
    return f

# Definindo coordenadas (x, y) para cada nó (hipoteticamente)
# Defina as coordenadas dos nós conforme necessário

# Definindo o nó objetivo como 'R'
goal_node = R

# Calculando o custo total (f) de cada nó em relação ao nó objetivo 'R'
nodes = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R]
for node in nodes:
    node.f = calculate_cost(node, goal_node)

# Imprimindo o custo total (f) de cada nó
for node in nodes:
    print(f"Node {node.name}: Cost = {node.f}")
