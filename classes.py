import random

import pygame as pg

from configs.colors import food_col
from configs.settings import grid_width, grid_height, tile_size


class Food:
    def __init__(self):
        self.pos = random.randrange(grid_width), random.randrange(grid_height)
        self.col = food_col

    def draw(self, surface):
        r = pg.Rect((self.pos[0] * tile_size, self.pos[1] * tile_size), [tile_size] * 2)
        pg.draw.rect(surface, self.col, r)
