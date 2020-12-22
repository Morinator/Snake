import random

import pygame as pg

from configs.colors import snake_col
from configs.game_constants import right, left, down, up, input_movements
from configs.settings import tile_size
from configs.sound import teleport


class Snake:
    def __init__(self, grid):
        self.blocks = [grid.random_pos()]
        self.direction = random.choice([up, down, left, right])
        self.length = 1

    def draw(self, surface):
        for block in self.blocks:
            rect = pg.Rect((block[0] * tile_size, block[1] * tile_size), [tile_size] * 2).inflate(-2, -2)
            pg.draw.rect(surface, snake_col, rect)

    def update_direction(self, key):
        d = input_movements[key]
        valid_direction = self.length < 2 or (d[0] + self.blocks[0][0], d[1] + self.blocks[0][1]) != self.blocks[1]
        if key in input_movements and valid_direction:
            self.direction = d

    def move(self, grid):
        new_head = self.blocks[0][0] + self.direction[0], self.blocks[0][1] + self.direction[1]
        if not (0 <= new_head[0] < grid.width and 0 <= new_head[1] < grid.height):
            teleport.play()
        new_head = new_head[0] % grid.width, new_head[1] % grid.height

        self.blocks.insert(0, new_head)

        if len(self.blocks) > self.length:  # trim tail of snake
            self.blocks.pop()

        return self.blocks[0] in self.blocks[1:]  # check for collision
