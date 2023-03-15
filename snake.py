import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False
    
    def move(self):
        head = self.body[0]
        x = (head[0] + self.direction[0]) % GRID_WIDTH
        y = (head[1] + self.direction[1]) % GRID_HEIGHT
        if (x, y) in self.body[1:]:
            return False
        self.body.insert(0, (x, y))
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True
    
    def change_direction(self, direction):
        if (direction[0] + self.direction[0], direction[1] + self.direction[1]) != (0, 0):
            self.direction = direction

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)

    def draw(self, surface):
        x = self.position[0] * GRID_SIZE
        y = self.position[1] * GRID_SIZE
        pygame.draw.rect(surface, RED, (x, y, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, BLACK, (x, y, GRID_SIZE, GRID_SIZE), 1)
        
def main():
# Définition de la surface d'affichage
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake")

    snake = Snake()
    food = Food()

    running = True
    clock = pygame.time.Clock()

    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        if not snake.move():
            running = False
        if snake.body[0] == food.position:
            food.position = food.random_position()
            snake.grow = True

        screen.fill(WHITE)
        for segment in snake.body:
            x = segment[0] * GRID_SIZE
            y = segment[1] * GRID_SIZE
            pygame.draw.rect(screen, GREEN, (x, y, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BLACK, (x, y, GRID_SIZE, GRID_SIZE), 1)
        food.draw(screen)
        pygame.display.update()

        # Réglage de la vitesse du jeu
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()