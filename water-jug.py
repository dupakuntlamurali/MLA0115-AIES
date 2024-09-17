from collections import deque

def is_valid(state, jug1_max, jug2_max):
    x, y = state
    return 0 <= x <= jug1_max and 0 <= y <= jug2_max

def bfs(jug1_max, jug2_max, target):
    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty
    visited.add((0, 0))
    solution = []
    
    while queue:
        state = queue.popleft()
        solution.append(state)

        x, y = state
        
        if x == target or y == target:
            return solution

        next_states = [
            (jug1_max, y),  # Fill Jug 1
            (x, jug2_max),  # Fill Jug 2
            (0, y),         # Empty Jug 1
            (x, 0),         # Empty Jug 2
            (x - min(x, jug2_max - y), y + min(x, jug2_max - y)),  # Pour Jug 1 into Jug 2
            (x + min(y, jug1_max - x), y - min(y, jug1_max - x))   # Pour Jug 2 into Jug 1
        ]
        
        for next_state in next_states:
            if next_state not in visited and is_valid(next_state, jug1_max, jug2_max):
                queue.append(next_state)
                visited.add(next_state)

    return "No solution"

def print_solution(solution):
    if isinstance(solution, list):
        print("Steps to reach the target:")
        for step in solution:
            print(f"Jug 1: {step[0]} liters, Jug 2: {step[1]} liters")
    else:
        print(solution)

jug1_max = 4
jug2_max = 3
target = 2

solution = bfs(jug1_max, jug2_max, target)
print_solution(solution)
