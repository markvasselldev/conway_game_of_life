class Board:
    """Class representing the game board for Conway's Game of Life."""

    def __init__(self, rows: int, cols: int) -> None:
        """Initialize the board with the given number of rows and columns."""
        self._num_rows = rows
        self._num_cols = cols
        # Initialize the board as a 2D list with all cells set to False (dead)
        self.board = [[False for _ in range(cols)] for _ in range(rows)]

    def display(self) -> None:
        """Print the current state of the board to the console."""
        for row in range(self._num_rows):
            print(self.board[row])  # Display each row of the board

    def apply_rules(self) -> None:
        """Apply the rules of Conway's Game of Life to update the board."""
        positions_to_update = []  # List to keep track of cells that need to be toggled

        # Iterate through each cell on the board
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                number_of_neighbors = self.count_neighbors(row, col)  # Count living neighbors
                if self.board[row][col]:  # If the cell is alive
                    # Mark for update if too many or too few neighbors
                    if number_of_neighbors > 3 or number_of_neighbors < 2:
                        positions_to_update.append((row, col))
                else:  # If the cell is dead
                    # Mark for update if exactly 3 neighbors (cell becomes alive)
                    if number_of_neighbors == 3:
                        positions_to_update.append((row, col))

        # Toggle the state of cells that were marked for update
        for row, col in positions_to_update:
            self.board[row][col] = not self.board[row][col]

    def count_neighbors(self, row: int, col: int) -> int:
        """Count the number of living neighbors around a given cell."""
        # Determine the indices of adjacent cells, wrapping around the edges
        up = row - 1 if row != 0 else self._num_rows - 1
        down = row + 1 if row != self._num_rows - 1 else 0
        left = col - 1 if col != 0 else self._num_cols - 1
        right = col + 1 if col != self._num_cols - 1 else 0

        # Sum the values of the neighboring cells (True = 1, False = 0)
        total_living_neighbors = sum([
            self.board[up][left],    # Top left
            self.board[row][left],   # Middle left
            self.board[down][left],  # Bottom left
            self.board[up][col],     # Top center
            self.board[down][col],   # Bottom center
            self.board[up][right],   # Top right
            self.board[row][right],  # Middle right
            self.board[down][right], # Bottom right
        ])

        return total_living_neighbors  # Return the total number of living neighbors

    def clear_board(self) -> None:
        """Clear the board, setting all cells to dead."""
        # Reinitialize the board to all False (dead) cells
        self.board = [[False for _ in range(self._num_cols)] for _ in range(self._num_rows)]

