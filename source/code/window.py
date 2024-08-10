class Window:
    """Class representing the window settings for the game."""

    def __init__(self) -> None:
        """Initialize the window with default height, width, canvas size, and margins."""
        self._height = 800  # Default height of the window
        self._width = 600  # Default width of the window
        self._canvas_percent = 0.80  # Percentage of the window height used by the canvas
        self._margin_x = 20  # Horizontal margin around the canvas
        self._margin_y = 20  # Vertical margin around the canvas

    def get_margin_x(self) -> int:
        """Return the horizontal margin size."""
        return self._margin_x
    
    def get_margin_y(self) -> int:
        """Return the vertical margin size."""
        return self._margin_y

    def convert_to_tk_geomerty_format(self) -> str:
        """Convert the window dimensions to a Tkinter-compatible geometry string.
        
        Returns:
            str: The window dimensions formatted as 'widthxheight'.
        """
        return str(self._width) + "x" + str(self._height)
    
    def get_height(self) -> int:
        """Return the height of the window."""
        return self._height
    
    def get_width(self) -> int:
        """Return the width of the window."""
        return self._width
    
    def set_height(self, height: int) -> None:
        """Set the height of the window.
        
        Args:
            height (int): The new height for the window.
        """
        self._height = height
    
    def set_width(self, width: int) -> None:
        """Set the width of the window.
        
        Args:
            width (int): The new width for the window.
        """
        self._width = width
