def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(f'Visitando nó {start}')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)



grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}


dfs(grafo, 'A')