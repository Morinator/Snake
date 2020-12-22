import pygame as pg

from configs.colors import apple_col
from configs.settings import tile_size


class Apple:
    def __init__(self, grid):
        self.pos = grid.random_pos()

    def draw(self, surface):
        r = pg.Rect((self.pos[0] * tile_size, self.pos[1] * tile_size), [tile_size] * 2).inflate(2, 2)
        pg.draw.rect(surface, apple_col, r)
