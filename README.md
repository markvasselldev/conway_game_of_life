# conway_game_of_life
The Conway's Game of Life is a cellular automaton devised by mathematician John Conway. The rules for the Game of Life are quite simple and are based on the state of cells in a grid:

1. Any live cell with two or three live neighbors survives.

2. A live cell (black square) remains alive in the next generation if it has exactly 2 or 3 live neighbors.
Any dead cell with three live neighbors becomes a live cell.

3. A dead cell (empty square) becomes alive (is "born") in the next generation if it has exactly 3 live neighbors.
All other live cells die in the next generation. Similarly, all other dead cells stay dead.

Live cells with fewer than 2 live neighbors (loneliness) or more than 3 live neighbors (overcrowding) die in the next generation due to underpopulation or overcrowding, respectively.
Dead cells with fewer than 3 live neighbors stay dead in the next generation.
These rules are applied simultaneously to every cell in the grid for each generation. The "neighbors" of a cell are the 8 cells adjacent to it (horizontally, vertically, and diagonally). The game evolves based on the initial configuration of live and dead cells and can create various patterns, including stable patterns, oscillators, gliders, and more complex structures.
