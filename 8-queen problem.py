def is_safe(board, row, col):
    
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    
    if row >= len(board):
        return True

    
    for col in range(len(board)):
        if is_safe(board, row, col):
            
            board[row][col] = 1

            
            if solve_n_queens(board, row + 1):
                return True

            
            board[row][col] = 0

    
    return False


def print_board(board):
    for row in board:
        print(" ".join(['Q' if col == 1 else '.' for col in row]))
    print()


def solve_8_queens():
    
    board = [[0 for _ in range(8)] for _ in range(8)]

    
    if solve_n_queens(board, 0):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists!")


solve_8_queens()
