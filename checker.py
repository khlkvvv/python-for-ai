<<<<<<< HEAD
def DFS(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbour in node:
                if neighbour not in visited:
                    stack.append(neighbour)
    return visited
=======
rows = 5
cols = 5

for i in range(rows):
    print("*" * cols)
>>>>>>> f3a90b71ff6181555b16f87ae8e6bb1e0e15c082
