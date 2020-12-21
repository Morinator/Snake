import pygame

from classes import Snake, Food
from configs.colors import black, grid_col_1, grid_col_2
from configs.settings import *


def drawGrid(surface):
    for y in range(0, grid_height):
        for x in range(0, grid_width):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * tile_size, y * tile_size), (tile_size, tile_size))
                pygame.draw.rect(surface, grid_col_1, r)
            else:
                rr = pygame.Rect((x * tile_size, y * tile_size), (tile_size, tile_size))
                pygame.draw.rect(surface, grid_col_2, rr)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    while True:
        clock.tick(max_fps)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.positions[0] == food.position:
            snake.length += 1
            snake.score += 1
            food = Food()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = pygame.font.SysFont("monospace", 16).render(f"Score {snake.score}", True, black)
        screen.blit(text, (5, 10))
        pygame.display.update()


main()
