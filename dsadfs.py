def dfs_(graph, vertex):
    visited = set()  
    stack = [vertex] 

    while stack:
        node = stack.pop()  
        if node not in visited:
            print(node, end=" ") 
            visited.add(node)

           
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {0: [1, 2],1: [0,2,3],2: [0,1],3: [1]}
strat=2   
print(f"Depth-First Search  {strat}:")
dfs_(graph, strat)