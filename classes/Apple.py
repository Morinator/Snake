import pygame as pg

from configs.colors import APPLE_RED
from configs.settings import TILE_SIZE, APPLE_SIZE


class Apple:
    def __init__(self, grid):
        self.pos = grid.random_pos()

    def draw(self, surface):
        r = pg.Rect((self.pos[0] * TILE_SIZE, self.pos[1] * TILE_SIZE), [TILE_SIZE] * 2).inflate([APPLE_SIZE] * 2)
        pg.draw.rect(surface, APPLE_RED, r)
