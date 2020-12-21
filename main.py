import sys

import pygame as pg

from classes.Food import Food
from classes.Grid import Grid
from classes.Snake import Snake
from configs.settings import *


def update_graphics():
    g.draw(screen)
    f.draw(screen)
    s.draw(screen)
    pg.display.update()


pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
g = Grid(grid_width, grid_height)
f = Food(g)
s = Snake(g)
clock = pg.time.Clock()

while True:
    clock.tick(max_fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            sys.exit()
    update_graphics()
