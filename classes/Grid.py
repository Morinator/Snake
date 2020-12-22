import random

import pygame as pg

from configs.colors import grid_color_1, grid_color_2
from configs.settings import tile_size


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, surface):
        for x in range(self.width):
            for y in range(self.height):
                color = grid_color_1 if (x + y) % 2 == 0 else grid_color_2
                pg.draw.rect(surface, color, pg.Rect(x * tile_size, y * tile_size, tile_size, tile_size))

    def random_pos(self):
        return random.randrange(self.width), random.randrange(self.height)
