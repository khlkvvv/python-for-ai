def dfs(graph, start):
    visited = set()           # Track where you've been
    stack = [start]           # LIFO structure
    
    while stack:              # Keep going while there's work
        node = stack.pop()    # Remove from END (LIFO!)
        
        if node not in visited:
            visited.add(node)    # Mark as seen
            
            for neighbor in graph[node]:  # Check all connections
                if neighbor not in visited:
                    stack.append(neighbor)  # Add to END
    
    return visited