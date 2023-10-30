def dfs(graph, node, visited):
  if node not in visited:
    visited.add(node)
    print("'" + node + "', " , end = '') # Print the current node
    # Recursively explore all of the adjacent nodes.
    for neighbor in graph[node]:
      if neighbor not in visited:
        dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
visited = set()
print("DFS Traversal:")
dfs(graph, 'A', visited)
# If the graph is disconnected
for node in graph:
    if node not in visited:  
      dfs(graph, node, visited)
