import pygame
import random

# Constants
WIDTH = 800  # Width of the window
HEIGHT = 600  # Height of the window
ROWS = 20  # Number of rows in the maze
COLS = 20  # Number of columns in the maze
CELL_SIZE = WIDTH // COLS  # Size of each cell

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")

# Create a grid
grid = [[0] * COLS for _ in range(ROWS)]

# Set the starting position
start_row, start_col = 0, 0
grid[start_row][start_col] = 1

# Set the ending position
end_row, end_col = ROWS - 1, COLS - 1

# Create a stack to keep track of visited cells
stack = [(start_row, start_col)]

# Generate the maze using Depth-First Search algorithm
while stack:
    current_row, current_col = stack[-1]

    # Find all unvisited neighbors of the current cell
    neighbors = []
    if current_row > 0 and grid[current_row - 1][current_col] == 0:
        neighbors.append((current_row - 1, current_col))
    if current_row < ROWS - 1 and grid[current_row + 1][current_col] == 0:
        neighbors.append((current_row + 1, current_col))
    if current_col > 0 and grid[current_row][current_col - 1] == 0:
        neighbors.append((current_row, current_col - 1))
    if current_col < COLS - 1 and grid[current_row][current_col + 1] == 0:
        neighbors.append((current_row, current_col + 1))

    if neighbors:
        # Choose a random neighbor
        next_row, next_col = random.choice(neighbors)

        # Remove the wall between the current cell and the chosen neighbor
        if next_row < current_row:
            grid[current_row][current_col] |= 1  # Remove the top wall
            grid[next_row][next_col] |= 4  # Remove the bottom wall
        elif next_row > current_row:
            grid[current_row][current_col] |= 4  # Remove the bottom wall
            grid[next_row][next_col] |= 1  # Remove the top wall
        elif next_col < current_col:
            grid[current_row][current_col] |= 8  # Remove the left wall
            grid[next_row][next_col] |= 2  # Remove the right wall
        elif next_col > current_col:
            grid[current_row][current_col] |= 2  # Remove the right wall
            grid[next_row][next_col] |= 8  # Remove the left wall

        # Mark the chosen neighbor as visited
        grid[next_row][next_col] = 1

        # Add the chosen neighbor to the stack
        stack.append((next_row, next_col))
    else:
        # Backtrack if there are no unvisited neighbors
        stack.pop()

# Draw the maze
def draw_maze():
    window.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if grid[row][col] & 1:  # Check if top wall is present
                pygame.draw.line(window, WHITE, (x, y), (x + CELL_SIZE, y), 1)
            if grid[row][col] & 2:  # Check if right wall is present
                pygame.draw.line(
                    window, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 1
                )
            if grid[row][col] & 4:  # Check if bottom wall is present
                pygame.draw.line(
                    window, WHITE, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 1
                )
            if grid[row][col] & 8:  # Check if left wall is present
                pygame.draw.line(window, WHITE, (x, y), (x, y + CELL_SIZE), 1)

    pygame.draw.rect(window, GREEN, (start_col * CELL_SIZE, start_row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(window, GREEN, (end_col * CELL_SIZE, end_row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_maze()
    pygame.display.flip()

# Quit Pygame
pygame.quit()
