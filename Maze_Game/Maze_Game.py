import pygame
import random

# Constants
CELL_SIZE = 20
ROWS = 15
COLS = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()

# Create the window
window_width = COLS * CELL_SIZE
window_height = ROWS * CELL_SIZE
window = pygame.display.set_mode((window_width, window_height))

# Maze grid
grid = [[15] * COLS for _ in range(ROWS)]

# Start position
start_row = 0
start_col = 0

# End position
end_row = ROWS - 1
end_col = COLS - 1

# Movable object
class MovableObject:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def move_up(self):
        if self.row > 0 and not grid[self.row][self.col] & 1:
            self.row -= 1

    def move_down(self):
        if self.row < ROWS - 1 and not grid[self.row + 1][self.col] & 1:
            self.row += 1

    def move_left(self):
        if self.col > 0 and not grid[self.row][self.col - 1] & 2:
            self.col -= 1

    def move_right(self):
        if self.col < COLS - 1 and not grid[self.row][self.col] & 2:
            self.col += 1

# Create a movable object
movable_object = MovableObject(start_row, start_col)

# Maze generation using DFS algorithm
def generate_maze(row, col):
    grid[row][col] &= ~8  # Remove left wall

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Left, Right, Up, Down
    random.shuffle(directions)

    for direction in directions:
        dx, dy = direction
        new_row, new_col = row + dx, col + dy

        if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 15:
            if dx == -1:
                grid[row][col] &= ~1  # Remove top wall
                grid[new_row][new_col] &= ~4  # Remove bottom wall
            elif dx == 1:
                grid[new_row][new_col] &= ~1  # Remove top wall
                grid[row][col] &= ~4  # Remove bottom wall
            elif dy == -1:
                grid[row][col] &= ~8  # Remove left wall
                grid[new_row][new_col] &= ~2  # Remove right wall
            elif dy == 1:
                grid[new_row][new_col] &= ~8  # Remove left wall
                grid[row][col] &= ~2  # Remove right wall

            generate_maze(new_row, new_col)

# Generate the maze
generate_maze(start_row, start_col)

# Draw the maze and movable object
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
    pygame.draw.rect(window, YELLOW, (end_col * CELL_SIZE, end_row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.circle(
        window,
        YELLOW,
        (movable_object.col * CELL_SIZE + CELL_SIZE // 2, movable_object.row * CELL_SIZE + CELL_SIZE // 2),
        CELL_SIZE // 2
    )

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                movable_object.move_up()
            elif event.key == pygame.K_DOWN:
                movable_object.move_down()
            elif event.key == pygame.K_LEFT:
                movable_object.move_left()
            elif event.key == pygame.K_RIGHT:
                movable_object.move_right()

    draw_maze()
    pygame.display.flip()

# Quit Pygame
pygame.quit()
