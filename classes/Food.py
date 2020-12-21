import pygame as pg

from configs.colors import food_col
from configs.settings import tile_size


class Food:
    def __init__(self, grid):
        self.pos = grid.random_pos()
        self.col = food_col

    def draw(self, surface):
        r = pg.Rect((self.pos[0] * tile_size, self.pos[1] * tile_size), [tile_size] * 2)
        pg.draw.rect(surface, self.col, r)
