import random
import time
import os
import sys

def clear_console():
    """Clears the console."""
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def resize_console(rows, cols):
    """Resize the console window to fit the grid."""
    if sys.platform.startswith('win'):
        os.system(f"mode con: cols={cols * 2} lines={rows + 5}")
    # Other OS-specific commands can be added if needed.

def create_grid(rows, cols):
    """Create a new grid of the given size."""
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

def draw_grid(grid, generation):
    """Draw the grid to the console."""
    clear_console()
    print(f"Generation {generation} - To exit the program press <Ctrl-C>")
    for row in grid:
        print(' '.join(['█' if cell else '.' for cell in row]))

def count_neighbors(grid, row, col):
    """Count the number of live neighbors around the given cell."""
    rows, cols = len(grid), len(grid[0])
    return sum(grid[(row + i) % rows][(col + j) % cols]
               for i in range(-1, 2) for j in range(-1, 2)
               if (i, j) != (0, 0))

def update_grid(grid):
    """Update the grid for the next generation."""
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            neighbors = count_neighbors(grid, row, col)
            if grid[row][col]:
                new_grid[row][col] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[row][col] = 1 if neighbors == 3 else 0
    return new_grid

def run_game(rows=20, cols=20, generations=500):
    """Run Conway's Game of Life."""
    grid = create_grid(rows, cols)
    resize_console(rows, cols)

    for generation in range(1, generations + 1):
        draw_grid(grid, generation)
        new_grid = update_grid(grid)
        if new_grid == grid:
            break
        grid = new_grid
        time.sleep(0.2)

    print("Simulation complete. Press <Enter> to exit.")
    input()

if __name__ == '__main__':
    run_game()
