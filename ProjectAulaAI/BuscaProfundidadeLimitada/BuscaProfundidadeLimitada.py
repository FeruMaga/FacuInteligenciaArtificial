class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def depth_limited_search(node, target, depth):
    if node is None:  # Caso base: nó é nulo
        return False

    if node.data == target:  # Caso base: encontrou o elemento
        print("Elemento", target, "encontrado na árvore.")
        return True

    if depth <= 0:  # Caso base: profundidade máxima atingida
        return False

    # Recursão para os nós filhos
    if depth_limited_search(node.left, target, depth - 1):
        return True
    if depth_limited_search(node.right, target, depth - 1):
        return True

    return False

def create_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    return root

def main():
    root = create_tree()  # Carregar Árvore

    target = 9  # Buscar
    max_depth = 3  # Profundidade Máxima
    print("Busca em profundidade limitada para o elemento", target, ":")
    if not depth_limited_search(root, target, max_depth):
        print("Elemento", target, "NÃO encontrado na árvore.")

if __name__ == "__main__":
    main()