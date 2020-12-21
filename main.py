import pygame

from classes import Snake, Food
from configs.colors import black, grid_col_1, grid_col_2
from configs.settings import *


def make_inits():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height))
    surface = pygame.Surface(screen.get_size()).convert()
    snake = Snake()
    food = Food()
    return clock, food, screen, snake, surface


def drawGrid(surface):
    for y in range(0, grid_height):
        for x in range(0, grid_width):
            r = (x * tile_size, y * tile_size, tile_size, tile_size)
            col = grid_col_1 if (x + y) % 2 == 0 else grid_col_2
            pygame.draw.rect(surface, col, r)


def redraw_all(food, screen, snake, surface):
    drawGrid(surface)
    snake.draw(surface)
    food.draw(surface)
    screen.blit(surface, (0, 0))
    screen.blit(pygame.font.SysFont(score_font, size=16).render(f"Score {snake.score}", True, black), (5, 10))
    pygame.display.update()


def main():
    clock, food, screen, snake, surface = make_inits()

    while True:
        clock.tick(max_fps)
        snake.handle_keys()
        snake.move()
        if snake.positions[0] == food.position:
            snake.eat()
            food = Food()

        redraw_all(food, screen, snake, surface)


main()
