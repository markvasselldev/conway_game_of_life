class Grid:
    """Class representing the grid layout for Conway's Game of Life."""

    def __init__(self, rows: int, cols: int) -> None:
        """Initialize the grid with the given number of rows and columns."""
        self._rows = rows  # Number of rows in the grid
        self._cols = cols  # Number of columns in the grid

    def get_rows(self) -> int:
        """Return the number of rows in the grid."""
        return self._rows

    def get_cols(self) -> int:
        """Return the number of columns in the grid."""
        return self._cols

    def get_col_width(self, canvas_width: float) -> float:
        """Calculate the width of each column in the grid based on the canvas width.
        
        Args:
            canvas_width (float): The width of the canvas.
        
        Returns:
            float: The width of each column.
        """
        return canvas_width / self._cols

    def get_col_height(self, canvas_height: float) -> float:
        """Calculate the height of each row in the grid based on the canvas height.
        
        Args:
            canvas_height (float): The height of the canvas.
        
        Returns:
            float: The height of each row.
        """
        return canvas_height / self._rows

    def get_square_size(self, play_area_width: float) -> float:
        """Calculate the size of each square in the grid based on the play area width.
        
        Args:
            play_area_width (float): The width of the play area.
        
        Returns:
            float: The size of each square.
        """
        return play_area_width / self.get_cols()
