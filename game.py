#python-game
import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT, GRID_SIZE, SNAKE_SIZE, FPS = 800, 600, 20, 20, 15
BLACK, WHITE, RED = (0, 0, 0), (255, 255, 255), (255, 0, 0)
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)

class Snake:
    def __init__(self):
        self.length, self.positions, self.direction, self.color = 1, [((WIDTH//2), (HEIGHT//2))], random.choice([UP, DOWN, LEFT, RIGHT]), RED

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur, x, y = self.get_head_position(), self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
        self.reset() if len(self.positions) > 2 and new in self.positions[2:] else self.positions.insert(0, new)
        self.positions = self.positions[:self.length]

    def reset(self):
        self.length, self.positions, self.direction = 1, [((WIDTH//2), (HEIGHT//2))], random.choice([UP, DOWN, LEFT, RIGHT])

    def render(self, surface):
        [pygame.draw.rect(surface, self.color, (p[0], p[1], SNAKE_SIZE, SNAKE_SIZE)) for p in self.positions]

class Fruit:
    def __init__(self):
        self.position, self.color = (0, 0), WHITE
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (WIDTH//GRID_SIZE)-1) * GRID_SIZE, random.randint(0, (HEIGHT//GRID_SIZE)-1) * GRID_SIZE)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))

def draw_grid(surface):
    [[pygame.draw.rect(surface, WHITE, (x, y, GRID_SIZE, GRID_SIZE), 1) for x in range(0, WIDTH, GRID_SIZE)] for y in range(0, HEIGHT, GRID_SIZE)]

def main():
    clock, screen = pygame.time.Clock(), pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size()).convert()
    snake, fruit = Snake(), Fruit()

    while True:
        [exit() if event.type == pygame.QUIT else setattr(snake, 'direction', globals()[f'{event.key}']) for event in pygame.event.get() if event.type == pygame.KEYDOWN]
        snake.update()
        [setattr(snake, 'length', snake.length + 1) and fruit.randomize_position() for _ in [0] if snake.get_head_position() == fruit.position]

        surface.fill(BLACK)
        draw_grid(surface)
        snake.render(surface)
        fruit.render(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
