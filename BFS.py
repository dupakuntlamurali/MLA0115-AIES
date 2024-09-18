from collections import deque

def bfs(graph, start):
    """
    Perform Breadth-First Search (BFS) on the given graph from the start node.
    
    :param graph: A dictionary representing the adjacency list of the graph
    :param start: The starting node for BFS
    :return: A list of nodes in the order they were visited
    """
    visited = set()      # Set to keep track of visited nodes
    queue = deque([start])  # Queue to manage the BFS order
    result = []          # List to store the order of visited nodes
    
    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            visited.add(node)   # Mark the node as visited
            result.append(node) # Add node to the result list
            
            # Enqueue all unvisited adjacent nodes
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    start_node = 'A'
    print(f"BFS starting from node {start_node}:")
    result = bfs(graph, start_node)
    print(result)
