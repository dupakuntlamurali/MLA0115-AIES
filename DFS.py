def dfs_recursive(graph, start, visited=None):
    """
    Perform Depth-First Search (DFS) on the given graph from the start node (recursive version).
    
    :param graph: A dictionary representing the adjacency list of the graph
    :param start: The starting node for DFS
    :param visited: A set to keep track of visited nodes (used in recursion)
    :return: A list of nodes in the order they were visited
    """
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result

def dfs_iterative(graph, start):
    """
    Perform Depth-First Search (DFS) on the given graph from the start node (iterative version).
    
    :param graph: A dictionary representing the adjacency list of the graph
    :param start: The starting node for DFS
    :return: A list of nodes in the order they were visited
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Add neighbors to the stack (reverse order for correct DFS order)
            stack.extend(reversed(graph[node]))
    
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
    
    print(f"DFS (Recursive) starting from node {start_node}:")
    recursive_result = dfs_recursive(graph, start_node)
    print(recursive_result)
    
    print(f"\nDFS (Iterative) starting from node {start_node}:")
    iterative_result = dfs_iterative(graph, start_node)
    print(iterative_result)
