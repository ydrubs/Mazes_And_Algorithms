import pygame
import random

# Define constants
WIDTH = 800
HEIGHT = 600
ROWS = 15
COLS = 20
CELL_SIZE = min(WIDTH // COLS, HEIGHT // ROWS)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)


def generate_maze():
    stack = [(0, 0)]

    while stack:
        col, row = stack[-1]
        grid[row][col] |= 16  # Mark the cell as visited

        neighbors = [
            (col, row - 1, 1, 4),  # Top neighbor
            (col + 1, row, 2, 8),  # Right neighbor
            (col, row + 1, 4, 1),  # Bottom neighbor
            (col - 1, row, 8, 2)   # Left neighbor
        ]
        unvisited_neighbors = []

        for ncol, nrow, dir_current, dir_neighbor in neighbors:
            if 0 <= ncol < COLS and 0 <= nrow < ROWS and grid[nrow][ncol] & 16 == 0:
                unvisited_neighbors.append((ncol, nrow, dir_current, dir_neighbor))

        if unvisited_neighbors:
            ncol, nrow, dir_current, dir_neighbor = random.choice(unvisited_neighbors)
            grid[row][col] &= ~dir_current  # Remove the current cell's wall
            grid[nrow][ncol] &= ~dir_neighbor  # Remove the neighbor's wall
            stack.append((ncol, nrow))
        else:
            stack.pop()


def draw_maze(screen):
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            if grid[row][col] & 1:  # Top wall
                pygame.draw.line(screen, WHITE, (x, y), (x + CELL_SIZE, y))
            if grid[row][col] & 2:  # Right wall
                pygame.draw.line(screen, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE))
            if grid[row][col] & 4:  # Bottom wall
                pygame.draw.line(screen, WHITE, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE))
            if grid[row][col] & 8:  # Left wall
                pygame.draw.line(screen, WHITE, (x, y), (x, y + CELL_SIZE))

            if row == ROWS - 1 and col == COLS - 1:  # Exit cell
                pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE))


# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Initialize the grid
grid = [[15] * COLS for _ in range(ROWS)]

# Generate the maze
generate_maze()

# Set up player position
player_row = 0
player_col = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player_row > 0 and not grid[player_row][player_col] & 1:
                    player_row -= 1
            elif event.key == pygame.K_RIGHT:
                if player_col < COLS - 1 and not grid[player_row][player_col] & 2:
                    player_col += 1
            elif event.key == pygame.K_DOWN:
                if player_row < ROWS - 1 and not grid[player_row][player_col] & 4:
                    player_row += 1
            elif event.key == pygame.K_LEFT:
                if player_col > 0 and not grid[player_row][player_col] & 8:
                    player_col -= 1

    if player_row == ROWS - 1 and player_col == COLS - 1:  # Check if player reached the exit
        screen.fill((255, 0, 0))  # Red screen
        font = pygame.font.Font(None, 48)  # Create a font object
        text = font.render("You Win!", True, (0, 255, 0))  # Render the text
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center the text on the screen
        screen.blit(text, text_rect)  # Draw the text on the screen
        pygame.display.flip()  # Update the display
        pygame.time.wait(2000)  # Pause for 2 seconds
        running = False  # End the game

    # Clear the screen
    screen.fill(BLACK)

    # Draw the maze
    draw_maze(screen)

    # Draw yellow circle in player's position
    pygame.draw.circle(screen, YELLOW, (player_col * CELL_SIZE + CELL_SIZE // 2, player_row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
