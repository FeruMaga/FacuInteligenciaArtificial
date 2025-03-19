import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def criar_grafo_exemplo():
    G = nx.Graph()

    # Adiciona nós
    G.add_nodes_from(["A", "B", "C", "D", "E"])

    # Adiciona arestas
    G.add_edges_from([("A", "B"), ("B", "D"), ("B", "E"), ("E", "H"), ("A", "C"), ("C", "F"), ("C", "G")])

    return G

def desenhar_grafo(grafo):
    pos = nx.spring_layout(grafo)  # Define a posição dos nós
    nx.draw(grafo, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=10)
    plt.show()

grafo_exemplo = criar_grafo_exemplo()

desenhar_grafo(grafo_exemplo)

def busca_largura(grafo, inicio, objetivo):
    fila = deque([(inicio, [inicio])])
    print(str(fila))

    while fila:
        (vertice, caminho) = fila.popleft()
        print("vertice: " + str(vertice))
        print("caminho: " + str(caminho))
        for vizinho in grafo[vertice]:
            print("vizinho: " + str(vizinho))
            if vizinho not in caminho:
                if vizinho == objetivo:
                    return caminho + [vizinho]
                else:
                    fila.append((vizinho, caminho + [vizinho]))


fila = deque([('A', ['A'])])
print(str(fila))
(vertice, caminho) = fila.popleft()
print(str((vertice, caminho)))

grafo_exemplo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

resultado = busca_largura(grafo_exemplo, 'A', 'H')
print("Caminho mais curto:", resultado)