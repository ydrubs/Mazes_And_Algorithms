import pygame
import random

# Constants
WIDTH = 800  # Width of the window
HEIGHT = 800  # Height of the window
ROWS = 20  # Number of rows in the maze
COLS = 20  # Number of columns in the maze
CELL_SIZE = WIDTH // COLS  # Size of each cell

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator")

# Create a grid
grid = [[15] * COLS for _ in range(ROWS)]

# Set the starting position
start_row, start_col = 0, 0
grid[start_row][start_col] = 0

# Set the ending position
end_row, end_col = ROWS - 1, COLS - 1
grid[end_row][end_col] = 0

# Create a stack to keep track of visited cells
stack = [(start_row, start_col)]

# Generate the maze using Depth-First Search algorithm
while stack:
    current_row, current_col = stack[-1]

    # Find all unvisited neighbors of the current cell
    neighbors = []
    if current_row > 1 and grid[current_row - 2][current_col] == 15:
        neighbors.append((current_row - 2, current_col))
    if current_row < ROWS - 2 and grid[current_row + 2][current_col] == 15:
        neighbors.append((current_row + 2, current_col))
    if current_col > 1 and grid[current_row][current_col - 2] == 15:
        neighbors.append((current_row, current_col - 2))
    if current_col < COLS - 2 and grid[current_row][current_col + 2] == 15:
        neighbors.append((current_row, current_col + 2))

    if neighbors:
        # Choose a random neighbor
        next_row, next_col = random.choice(neighbors)

        # Remove the wall between the current cell and the chosen neighbor
        if next_row < current_row:
            grid[current_row - 1][current_col] = 0  # Remove the top wall
        elif next_row > current_row:
            grid[current_row + 1][current_col] = 0  # Remove the bottom wall
        elif next_col < current_col:
            grid[current_row][current_col - 1] = 0  # Remove the left wall
        elif next_col > current_col:
            grid[current_row][current_col + 1] = 0  # Remove the right wall

        # Mark the chosen neighbor as visited
        grid[next_row][next_col] = 0

        # Add the chosen neighbor to the stack
        stack.append((next_row, next_col))
    else:
        # Backtrack if there are no unvisited neighbors
        stack.pop()

# Ensure a path from the start to the end point
for i in range(1, ROWS, 2):
    if grid[i][end_col - 1] == 0:
        grid[i][end_col] = 0
        break

# Draw the maze
# Draw the maze
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
    pygame.draw.rect(window, RED, (end_col * CELL_SIZE, end_row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.circle(window, BLUE, (start_col * CELL_SIZE + CELL_SIZE // 2, start_row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)
    pygame.draw.circle(window, BLUE, (end_col * CELL_SIZE + CELL_SIZE // 2, end_row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 4)

    # Mark the end position with a different shape
    pygame.draw.rect(window, YELLOW, (end_col * CELL_SIZE + CELL_SIZE // 4, end_row * CELL_SIZE + CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2))

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
