from collections import deque

def bfs(graph, start):
    visited = set()           # Track where you've been
    queue = deque([start])    # FIFO structure
    
    while queue:              # Keep going while there's work
        node = queue.popleft()  # Remove from FRONT
        
        if node not in visited:
            visited.add(node)    # Mark as seen
            
            for neighbor in graph[node]:  # Check all connections
                if neighbor not in visited:
                    queue.append(neighbor)  # Add to BACK
    
    return visited