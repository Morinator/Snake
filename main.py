import pygame as pg

pg.init()
from configs.sound import munch
from classes.Apple import Apple
from classes.Grid import Grid
from classes.Snake import Snake
from configs.colors import *
from configs.settings import *
import sys


def update_all_graphics():
    [item.draw(screen) for item in [grid, apple, snake]]
    screen.blit(font.render(f"Score : {score}", True, light_grey), text_pos)
    pg.display.update()


screen = pg.display.set_mode(screen_size)
clock = pg.time.Clock()
score = 0

grid = Grid(*grid_size)
apple = Apple(grid)
snake = Snake(grid)

while True:
    clock.tick(max_fps)

    for event in pg.event.get():  # event handling
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            snake.update_direction(event.key)

    has_collided = snake.move(grid)
    if has_collided:
        sys.exit()

    if snake.li[0] == apple.pos:
        snake.length += 1
        apple = Apple(grid)
        score += 1
        munch.play()
    update_all_graphics()
