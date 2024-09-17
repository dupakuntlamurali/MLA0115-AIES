from collections import deque

# Function to check if the current state is valid
def is_valid_state(state):
    m_left, c_left, m_right, c_right = state
    # Check if the number of missionaries and cannibals is within limits
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    # Check if cannibals outnumber missionaries on the left or right side
    if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
        return False
    return True

# Function to check if the current state is the goal
def is_goal_state(state):
    return state == (0, 0, 3, 3)

# Function to generate the next possible states
def get_next_states(state, boat_side):
    m_left, c_left, m_right, c_right = state
    next_states = []
    if boat_side == 'left':
        # Move 1 missionary from left to right
        next_states.append((m_left - 1, c_left, m_right + 1, c_right, 'right'))
        # Move 2 missionaries from left to right
        next_states.append((m_left - 2, c_left, m_right + 2, c_right, 'right'))
        # Move 1 cannibal from left to right
        next_states.append((m_left, c_left - 1, m_right, c_right + 1, 'right'))
        # Move 2 cannibals from left to right
        next_states.append((m_left, c_left - 2, m_right, c_right + 2, 'right'))
        # Move 1 missionary and 1 cannibal from left to right
        next_states.append((m_left - 1, c_left - 1, m_right + 1, c_right + 1, 'right'))
    else:
        # Move 1 missionary from right to left
        next_states.append((m_left + 1, c_left, m_right - 1, c_right, 'left'))
        # Move 2 missionaries from right to left
        next_states.append((m_left + 2, c_left, m_right - 2, c_right, 'left'))
        # Move 1 cannibal from right to left
        next_states.append((m_left, c_left + 1, m_right, c_right - 1, 'left'))
        # Move 2 cannibals from right to left
        next_states.append((m_left, c_left + 2, m_right, c_right - 2, 'left'))
        # Move 1 missionary and 1 cannibal from right to left
        next_states.append((m_left + 1, c_left + 1, m_right - 1, c_right - 1, 'left'))
    
    return [state for state in next_states if is_valid_state(state[:4])]

# Function to solve the missionaries and cannibals problem using BFS
def missionaries_cannibals_bfs():
    initial_state = (3, 3, 0, 0, 'left')  # (missionaries_left, cannibals_left, missionaries_right, cannibals_right, boat_side)
    queue = deque([initial_state])
    visited = set([initial_state])
    parent = {initial_state: None}

    while queue:
        current_state = queue.popleft()

        # Check if we've reached the goal
        if is_goal_state(current_state[:4]):
            return current_state, parent

        # Get the next possible states
        for next_state in get_next_states(current_state[:4], current_state[4]):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)
                parent[next_state] = current_state

    return None, None  # No solution found

# Function to print the solution path
def print_solution_path(parent, goal_state):
    path = []
    current_state = goal_state
    while current_state is not None:
        path.append(current_state)
        current_state = parent[current_state]
    path.reverse()

    print("Solution path (Missionaries Left, Cannibals Left, Missionaries Right, Cannibals Right, Boat Side):")
    for state in path:
        print(state)

# Main function to solve the missionaries and cannibals problem
def solve_missionaries_cannibals_problem():
    goal_state, parent = missionaries_cannibals_bfs()
    if goal_state:
        print("Solution found:")
        print_solution_path(parent, goal_state)
    else:
        print("No solution exists!")

# Solve the problem
solve_missionaries_cannibals_problem()
