import random

import pygame as pg

from constants.colors import LIGHT_GREEN, DARK_GREEN
from constants.settings import TILE_SIZE


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, surface):
        for x in range(self.width):
            for y in range(self.height):
                color = LIGHT_GREEN if (x + y) % 2 == 0 else DARK_GREEN
                pg.draw.rect(surface, color, pg.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def random_pos(self):
        return random.randrange(self.width), random.randrange(self.height)
