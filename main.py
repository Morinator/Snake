import pygame as pg

pg.init()
from configs.sound import laser
from classes.Food import Food
from classes.Grid import Grid
from classes.Snake import Snake
from configs.colors import black
from configs.settings import *
import sys


def update_graphics():
    g.draw(screen)
    f.draw(screen)
    s.draw(screen)
    screen.blit(font.render("Score : " + str(score_value), True, black), text_pos)
    pg.display.update()


screen = pg.display.set_mode((screen_width, screen_height))
g = Grid(grid_width, grid_height)
f = Food(g)
s = Snake(g)
clock = pg.time.Clock()
score_value = 0
while True:
    clock.tick(max_fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
            s.update_direction(event.key)

    s.move(g)
    if s.check_food(f):
        s.grow()
        f = Food(g)
        score_value += 1
        laser.play()
    update_graphics()
