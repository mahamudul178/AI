
def DFS(graph, start):
    visited=set()
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node]- visited)
    return visited
    
graph={
    'A':set(['B','C',]),
    'B':set(['A','D','E']),
    'C':set(['A','F']),
    'D':set(['B']),
    'E':set(['B','F']),
    'F':set(['C', 'E'])
}

print("DFS Traversal: ")
dfs=DFS(graph, 'A')
print(dfs)