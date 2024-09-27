def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


graph = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C'],
    'E': ['A']
}


start = 'A' 
print(f"Breadth-First Search {start}:")
bfs(graph, start)
