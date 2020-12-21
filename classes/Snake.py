import pygame as pg

from configs.colors import snake_col
from configs.settings import tile_size


class Snake:

    def __init__(self, grid):
        self.blocks = [grid.random_pos()]

    def draw(self, surface):
        for block in self.blocks:
            r = pg.Rect((block[0] * tile_size, block[1] * tile_size), [tile_size] * 2)
            pg.draw.rect(surface, snake_col, r)

    def update_direction(self):
        pass

    def eat(self):
        pass

    def move(self):
        pass
