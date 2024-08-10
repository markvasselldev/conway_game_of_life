import tkinter as tk

import window
import grid
import board

class Game(tk.Frame):
    """Class representing the Conway's Game of Life."""

    def __init__(self):
        """Initialize the game with window details, grid, and board."""
        self._window_details = window.Window()
        self.rows, self.cols = 20, 20  # Set the number of rows and columns for the grid
        self._grid_details = grid.Grid(self.rows, self.cols)

        self.board = board.Board(self.rows, self.cols)  # Initialize the game board
        self.current_job = None  # Placeholder for the job identifier for scheduled tasks
        
        # Calculate the height of the play area
        self._play_area_height = self._window_details.get_height() - (
            abs(self._window_details.get_height() - self._window_details.get_width())
        )

    def start(self):
        """Start the game by setting up the Tkinter root and UI components."""
        self.root = tk.Tk()

        # Initialize the Tkinter Frame with the root window
        tk.Frame.__init__(self, self.root)
        self.root.title("Conway's Game of Life")

        # Configure the frame to fill the entire window
        self.pack(fill=tk.BOTH, expand=1)

        # Set the minimum and maximum window size based on window details
        self.root.maxsize(self._window_details.get_width(), self._window_details.get_height())
        self.root.minsize(self._window_details.get_width(), self._window_details.get_height())
        
        # Create a canvas for drawing the grid and cells
        self.canvas = tk.Canvas(self.root, 
                                width=self._window_details.get_width(), 
                                height=self._window_details.get_height())
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)

        # Determine the size of each square in the grid
        self.sq_size = self._grid_details.get_square_size(
            self._window_details.get_width() - (self._window_details.get_margin_x() * 2)
        )

        # Create and pack buttons for controlling the simulation
        start_btn = tk.Button(self, text="Start Simulation", borderwidth=5, 
                              command=self.start_simulation, bg="green")
        stop_btn = tk.Button(self, text="Stop Simulation", borderwidth=5, 
                             command=self.stop_simulation, bg="red")
        clear_btn = tk.Button(self, text="Clear Board", borderwidth=5, 
                              command=self.clear_board, bg="grey")

        clear_btn.pack(fill=tk.BOTH, side=tk.BOTTOM)
        stop_btn.pack(fill=tk.BOTH, side=tk.BOTTOM)
        start_btn.pack(fill=tk.BOTH, side=tk.BOTTOM)

        # Bind the left mouse click event to the cell_clicked method
        self.canvas.bind("<Button-1>", self.cell_clicked)

        # Draw the initial grid
        self.draw_grid()

        # Start the Tkinter main event loop
        self.root.mainloop()

    def draw_grid(self) -> None:
        """Draw the grid lines on the canvas."""
        for i in range(self._grid_details.get_cols() + 1):
            # Draw vertical lines
            self.canvas.create_line(
                self._window_details.get_margin_x() + i * self.sq_size,
                self._window_details.get_margin_y(),
                self._window_details.get_margin_x() + i * self.sq_size,
                self._play_area_height - self._window_details.get_margin_y()
            )
            # Draw horizontal lines
            self.canvas.create_line(
                self._window_details.get_margin_x(),
                self._window_details.get_margin_y() + i * self.sq_size,
                self._window_details.get_width() - self._window_details.get_margin_x(),
                self._window_details.get_margin_y() + i * self.sq_size
            )
            
    def start_simulation(self):
        """Start the simulation by applying rules and scheduling the next update."""
        self.board.apply_rules()  # Apply the rules to update the board state
        self.draw_board()  # Draw the updated board
        self.current_job = self.after(1000, self.start_simulation)  # Schedule the next update

    def stop_simulation(self):
        """Stop the simulation by canceling the scheduled update."""
        if self.current_job is not None:
            self.after_cancel(self.current_job)
            self.current_job = None

    def clear_board(self):
        """Clear the game board and update the display."""
        self.board.clear_board()  # Clear the board data
        self.draw_board()  # Update the board display

    def draw_board(self) -> None:
        """Draw the cells on the canvas based on the board state."""
        for row in range(self.rows):
            for col in range(self.cols):
                self.draw_selected_cell(row, col)  # Draw each cell based on its state

    def cell_clicked(self, event):
        """Handle cell click events to toggle cell state."""
        x, y = event.x, event.y

        # Check if the click is within the grid boundaries
        if (self._window_details.get_margin_x() <= x <= self._window_details.get_width() - self._window_details.get_margin_x() and 
            self._window_details.get_margin_y() <= y <= self._play_area_height - self._window_details.get_margin_x()):

            # Calculate the row and column based on the click coordinates
            r = int(x // self.sq_size - 1)
            c = int(y // self.sq_size - 1)

            # Toggle the state of the clicked cell
            self.board.board[r][c] = not self.board.board[r][c]
            self.draw_selected_cell(r, c)  # Redraw the cell to reflect the new state

    def draw_selected_cell(self, row, col) -> None:
        """Draw a single cell on the canvas based on its state."""
        cell_name = f'{row}-{col}'  # Unique tag for the cell in the canvas
        self.canvas.delete(cell_name)  # Delete any existing rectangle for this cell

        if self.board.board[row][col]:
            # Draw a filled rectangle if the cell is alive
            self.canvas.create_rectangle(
                self._window_details.get_margin_x() + row * self.sq_size + .2,
                self._window_details.get_margin_y() + col * self.sq_size + .2,
                self._window_details.get_margin_x() + (row + 1) * self.sq_size - .2,
                self._window_details.get_margin_y() + (col  + 1) * self.sq_size - .2,
                fill='#490be6',
                tags=cell_name
            )
