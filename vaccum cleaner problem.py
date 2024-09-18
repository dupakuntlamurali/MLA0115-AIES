class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        # Initial position is at the top-left corner
        self.position = (0, 0)
    
    def move(self, direction):
        """Move the vacuum cleaner in the specified direction."""
        x, y = self.position
        if direction == 'up' and x > 0:
            self.position = (x - 1, y)
        elif direction == 'down' and x < self.rows - 1:
            self.position = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.position = (x, y - 1)
        elif direction == 'right' and y < self.cols - 1:
            self.position = (x, y + 1)
    
    def clean(self):
        """Clean the current position."""
        x, y = self.position
        if self.grid[x][y] == 1:  # Only clean if it's dirty
            self.grid[x][y] = 0  # 0 indicates clean

    def print_grid(self):
        """Print the grid."""
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))
        print()
    
    def find_dirty_cells(self):
        """Find all dirty cells in the grid."""
        dirty_cells = [(i, j) for i in range(self.rows) for j in range(self.cols) if self.grid[i][j] == 1]
        return dirty_cells

    def solve(self):
        """Solve the vacuum cleaner problem using a simple heuristic approach."""
        dirty_cells = self.find_dirty_cells()
        while dirty_cells:
            x, y = self.position
            # Find the closest dirty cell
            closest_dirty = min(dirty_cells, key=lambda cell: abs(cell[0] - x) + abs(cell[1] - y))
            while self.position != closest_dirty:
                cx, cy = self.position
                dx, dy = closest_dirty
                # Move towards the dirty cell
                if cx < dx:
                    self.move('down')
                elif cx > dx:
                    self.move('up')
                elif cy < dy:
                    self.move('right')
                elif cy > dy:
                    self.move('left')
                
                # Print the grid after each move
                self.print_grid()
                
                # Clean the cell once we reach it
                if self.position == closest_dirty:
                    self.clean()
                    dirty_cells.remove(closest_dirty)
                    break
        print("All cells are cleaned!")

if __name__ == "__main__":
    # Define the grid with 1s for dirty cells and 0s for clean cells
    grid = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    
    vacuum = VacuumCleaner(grid)
    print("Initial Grid:")
    vacuum.print_grid()
    vacuum.solve()
