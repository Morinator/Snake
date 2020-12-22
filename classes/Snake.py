import random

import pygame as pg

from configs.colors import snake_col, grid_col_1
from configs.game_constants import right, left, down, up, input_movements
from configs.settings import tile_size
from configs.sound import laser


class Snake:
    def __init__(self, grid):
        self.blocks = [grid.random_pos()]
        self.direction = random.choice([up, down, left, right])
        self.length = 4

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
        """:returns True if the snake collied with itself"""
        new_block = self.blocks[0][0] + self.direction[0], self.blocks[0][1] + self.direction[1]

        if not (0 < new_block[0] < grid.width and 0 < new_block[1] < grid.height):
            laser.play()

        new_block = new_block[0] % grid.width, new_block[1] % grid.height

        self.blocks.insert(0, new_block)

        if len(self.blocks) > self.length:  # trim tail of snake
            self.blocks.pop()

        return self.blocks[0] in self.blocks[1:]
