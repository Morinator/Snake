import random

import pygame as pg

from configs.colors import snake_yellow, snake_brown
from configs.game_constants import right, left, down, up, arrow_key_to_direction
from configs.settings import tile_size
from configs.sound import teleportation_sound, munch_sound


class Snake:
    def __init__(self, grid):
        self.li = [grid.random_pos()]
        self.direction = random.choice([up, down, left, right])
        self.length = 1
        self.col = snake_yellow
        self.eat_cd = 0

    def draw(self, surface):
        for i in self.li:
            rect = pg.Rect((i[0] * tile_size, i[1] * tile_size), [tile_size] * 2).inflate(-2, -2)
            pg.draw.rect(surface, self.col, rect)

    def update_direction(self, key):
        if key in arrow_key_to_direction:
            d = arrow_key_to_direction[key]
            valid_direction = len(self.li) < 2 or (d[0] + self.li[0][0], d[1] + self.li[0][1]) != self.li[1]
            if valid_direction:
                self.direction = d

    def move(self, grid):
        new_head = self.li[0][0] + self.direction[0], self.li[0][1] + self.direction[1]
        if not (0 <= new_head[0] < grid.width and 0 <= new_head[1] < grid.height):
            teleportation_sound.play()
        new_head = new_head[0] % grid.width, new_head[1] % grid.height

        self.li.insert(0, new_head)

        if len(self.li) > self.length:  # trim tail of snake
            self.li.pop()

        return self.li[0] in self.li[1:]  # check for collision

    def update_color(self):
        self.eat_cd = max(0, self.eat_cd - 1)
        self.col = snake_yellow if self.eat_cd == 0 else snake_brown

    def eat(self):
        self.length += 1
        self.eat_cd = 2
        munch_sound.play()
