import sys

import pygame as pg

from configs.colors import grid_col_1, grid_col_2
from configs.settings import *

screen = pg.display.set_mode((screen_width, screen_height))
from classes import *

pg.init()


def draw_grid():
    for x in range(grid_width):
        for y in range(grid_height):
            col = grid_col_1 if (x + y) % 2 == 0 else grid_col_2
            pg.draw.rect(screen, col, pg.Rect(x * tile_size, y * tile_size, tile_size, tile_size))


def redraw_all():
    draw_grid()
    f.draw(screen)
    pg.display.update()


clock = pg.time.Clock()

f = Food()

while True:
    clock.tick(max_fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            sys.exit()
    redraw_all()
