def nearest_neighbor(distance_matrix):
    """
    Solve the Traveling Salesman Problem using the Nearest Neighbor heuristic.
    
    :param distance_matrix: A 2D list representing the distance between cities
    :return: The tour and its distance
    """
    num_cities = len(distance_matrix)
    unvisited = set(range(num_cities))
    current_city = 0
    tour = [current_city]
    total_distance = 0
    
    while len(unvisited) > 1:
        unvisited.remove(current_city)
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        total_distance += distance_matrix[current_city][next_city]
        current_city = next_city
        tour.append(current_city)
    
    # Return to the starting city
    total_distance += distance_matrix[current_city][tour[0]]
    tour.append(tour[0])
    
    return tour, total_distance

if __name__ == "__main__":
    # Example distance matrix (symmetric and diagonal elements are zero)
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    tour, total_distance = nearest_neighbor(distance_matrix)
    print(f"Tour: {tour}")
    print(f"Total distance: {total_distance}")
