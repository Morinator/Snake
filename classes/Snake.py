import random

import pygame as pg

from constants.colors import SNAKE_YELLOW, SNAKE_BROWN
from constants.game_constants import right, left, down, up, arrow_key_to_direction
from constants.settings import TILE_SIZE, STARTING_LENGTH
from constants.sound import TELEPORTATION_SOUND, MUNCH_SOUND, EXPLOSION_SOUNDS


class Snake:
    def __init__(self, grid):
        self.li = [grid.random_pos()]
        self.direction = random.choice([up, down, left, right])
        self.length = STARTING_LENGTH
        self.col = SNAKE_YELLOW
        self.eat_cd = 0

    def draw(self, surface):
        for i in self.li:
            rect = pg.Rect((i[0] * TILE_SIZE, i[1] * TILE_SIZE), [TILE_SIZE] * 2).inflate(-2, -2)
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
            TELEPORTATION_SOUND.play()
        new_head = new_head[0] % grid.width, new_head[1] % grid.height

        self.li.insert(0, new_head)

        if len(self.li) > self.length:  # trim tail of snake
            self.li.pop()

        collides = self.li[0] in self.li[1:]
        if collides:
            random.choice(EXPLOSION_SOUNDS).play()
        return collides

    def update_color(self):
        self.eat_cd = max(0, self.eat_cd - 1)
        self.col = SNAKE_YELLOW if self.eat_cd == 0 else SNAKE_BROWN

    def eat(self):
        self.length += 1
        self.eat_cd = 2
        MUNCH_SOUND.play()
