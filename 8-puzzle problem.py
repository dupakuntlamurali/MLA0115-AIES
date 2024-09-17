import heapq

class PuzzleState:
    def __init__(self, board, g, parent=None):
        self.board = board
        self.g = g  # Cost to reach this state
        self.h = self.manhattan_distance()  # Heuristic estimate
        self.f = self.g + self.h  # Total cost
        self.parent = parent  # To keep track of the path

    def __lt__(self, other):
        return self.f < other.f

    def manhattan_distance(self):
        """Calculate the Manhattan Distance heuristic."""
        distance = 0
        goal = [(i, j) for i in range(3) for j in range(3)]  # Goal state positions
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:  # Skip the blank tile
                    goal_x, goal_y = divmod(value - 1, 3)
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def generate_successors(self):
        """Generate all possible moves from the current state."""
        successors = []
        x, y = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0][0]  # Find blank tile
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right moves

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]  # Swap tiles
                successors.append(PuzzleState(new_board, self.g + 1, self))

        return successors

    def is_goal(self):
        """Check if the current state is the goal state."""
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal

    def print_board(self):
        """Print the current board configuration."""
        for row in self.board:
            print(row)
        print()

def a_star_search(start_state):
    """A* search algorithm to solve the puzzle."""
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            return current_state  # Found the goal

        closed_set.add(tuple(map(tuple, current_state.board)))

        for successor in current_state.generate_successors():
            if tuple(map(tuple, successor.board)) not in closed_set:
                heapq.heappush(open_list, successor)

    return None  # No solution found

def print_solution(solution_state):
    """Print the sequence of moves leading to the solution."""
    path = []
    current = solution_state
    while current:
        path.append(current)
        current = current.parent
    path.reverse()

    for state in path:
        state.print_board()

initial_board = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]


initial_state = PuzzleState(initial_board, 0)


solution = a_star_search(initial_state)


if solution:
    print("Solution found!")
    print_solution(solution)
else:
    print("No solution exists!")
