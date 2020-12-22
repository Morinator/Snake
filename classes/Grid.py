import random

import pygame as pg

from configs.colors import grid_col_1, grid_col_2
from configs.settings import tile_size


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, surface):
        for x in range(self.width):
            for y in range(self.height):
                col = grid_col_1 if (x + y) % 2 == 0 else grid_col_2
                pg.draw.rect(surface, col, pg.Rect(x * tile_size, y * tile_size, tile_size, tile_size))

    def random_pos(self):
        return random.randrange(self.width), random.randrange(self.height)
