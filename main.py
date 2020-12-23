import pygame as pg

pg.init()
from classes.Apple import Apple
from classes.Grid import Grid
from classes.Snake import Snake
from configs.colors import *
from configs.settings import *
import sys


def update_all_graphics():
    [item.draw(screen) for item in [grid, apple, snake]]
    screen.blit(FONT.render(f"Score: {score}", True, LIGHT_GREY), TEXT_POS)
    pg.display.update()


screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()
score = 0

grid = Grid(*GRID_SIZE)
apple = Apple(grid)
snake = Snake(grid)
while True:
    clock.tick(MAX_FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            snake.update_direction(event.key)

    has_collided = snake.move(grid)
    snake.update_color()
    if has_collided:
        sys.exit()

    if snake.li[0] == apple.pos:
        snake.eat()
        apple = Apple(grid)
        score += 1

    update_all_graphics()
