import pygame as pg

pg.init()
from configs.sound import bite
from classes.Apple import Apple
from classes.Grid import Grid
from classes.Snake import Snake
from configs.colors import *
from configs.settings import *
import sys


def update_graphics():
    [item.draw(screen) for item in [grid, apple, snake]]
    screen.blit(font.render(f"Score : {score}", True, light_grey), text_pos)
    pg.display.update()


screen = pg.display.set_mode(screen_size)
grid = Grid(grid_width, grid_height)
apple = Apple(grid)
snake = Snake(grid)
clock = pg.time.Clock()
score = 0

while True:
    clock.tick(max_fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            snake.update_direction(event.key)

    has_collided = snake.move(grid)
    if has_collided:
        sys.exit()

    if apple.pos == snake.blocks[0]:
        snake.length += 1
        apple = Apple(grid)
        score += 1
        bite.play()
    update_graphics()
