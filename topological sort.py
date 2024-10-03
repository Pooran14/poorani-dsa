from collections import defaultdict, deque

def topological_sort(graph):
    
    in_degree = defaultdict(int)
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] += 1

    queue = deque([vertex for vertex in graph if in_degree[vertex] == 0])
    sorted_vertices = []

    while queue:
        vertex = queue.popleft()
        sorted_vertices.append(vertex)

        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_vertices) != len(graph):
        raise ValueError("Graph contains a cycle")

    return sorted_vertices

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

sorted_vertices = topological_sort(graph)
print("Topologically sorted vertices:", sorted_vertices)

