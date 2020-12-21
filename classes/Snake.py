import random

import pygame as pg

from configs.colors import snake_col
from configs.game_constants import right, left, down, up
from configs.settings import tile_size


class Snake:

    def __init__(self, grid):
        self.blocks = [grid.random_pos()]
        self.direction = random.choice([up, down, left, right])

    def draw(self, surface):
        for block in self.blocks:
            r = pg.Rect((block[0] * tile_size, block[1] * tile_size), [tile_size] * 2)
            pg.draw.rect(surface, snake_col, r)

    def update_direction(self):
        pass

    def eat(self):
        pass

    def move(self, grid):
        new_block = (self.blocks[0][0] + self.direction[0]) % grid.width, \
                    (self.blocks[0][1] + self.direction[1]) % grid.height
        self.blocks.insert(0, new_block)
        self.blocks.pop()
