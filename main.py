import pygame as pg

pg.init()
from classes.Game import Game

g = Game()
g.show_start_screen()
g.run()
