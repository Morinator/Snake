import random

import pygame as pg

from configs.colors import snake_col, grid_col_1
from configs.game_constants import right, left, down, up, input_movements
from configs.settings import tile_size


class Snake:
    def __init__(self, grid):
        self.blocks = [grid.random_pos()]
        self.direction = random.choice([up, down, left, right])
        self.max_length = 1

    def draw(self, surface):
        for block in self.blocks:
            rect = pg.Rect((block[0] * tile_size, block[1] * tile_size), [tile_size] * 2)
            pg.draw.rect(surface, snake_col, rect)
            pg.draw.rect(surface, grid_col_1, rect, width=2)

    def update_direction(self, key):
        d = input_movements[key]
        if key in input_movements and (-d[0], - d[1]) != self.direction:
            self.direction = d

    def move(self, grid):
        new_block = (self.blocks[0][0] + self.direction[0]) % grid.width, \
                    (self.blocks[0][1] + self.direction[1]) % grid.height
        self.blocks.insert(0, new_block)
        if self.blocks[0] in self.blocks[1:]:
            print("versaaagt")
        if len(self.blocks) > self.max_length:
            self.blocks.pop()

    def grow(self, amount=1):
        self.max_length += amount

    def check_food(self, food):
        return food.pos == self.blocks[0]
