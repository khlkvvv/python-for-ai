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