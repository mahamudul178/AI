from queue import Queue

def bfs(graph, start):
    visited=set()
    queue=Queue()
    queue.put(start)

    while not queue.empty():
        vertex= queue.get()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in  visited:
                    queue.put(neighbour)

graph={
    'A':['B','C',],
    'B':['D','E',],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

bfs(graph, 'A')