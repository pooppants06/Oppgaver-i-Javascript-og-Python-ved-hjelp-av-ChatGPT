import pygame
import random

# Initialiserer Pygame
pygame.init()

# Definerer konstanter
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Farger
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Oppretter vindu
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Oppdaterer skjermen
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(win, WHITE, (x,0), (x,HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(win, WHITE, (0,y), (WIDTH,y))

# Klasse for slangen
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH//2, GRID_HEIGHT//2)]
        self.direction = (0, -1)  # Oppover

    def move(self):
        head = self.body[0]
        x, y = self.direction
        new_head = ((head[0] + x) % GRID_WIDTH, (head[1] + y) % GRID_HEIGHT)
        if new_head in self.body[1:]:
            return False  # Kollisjon med kroppen
        self.body.insert(0, new_head)
        return True

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(win, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Klasse for maten
class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        return (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

    def draw(self):
        pygame.draw.rect(win, RED, (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Starter hovedloopen
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.direction = (1, 0)

        win.fill(BLACK)
        draw_grid()

        if snake.move():
            snake.draw()
            food.draw()
        else:
            running = False  # Spillet avsluttes hvis slangen kolliderer med seg selv

        if snake.body[0] == food.position:
            snake.grow()
            food.position = food.randomize_position()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
