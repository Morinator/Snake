import random
import sys

from configs.colors import snake_col, food_col, grid_col_1
from configs.game_constants import *
from configs.settings import tile_size, screen_height, screen_width, grid_width, grid_height


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width // 2), (screen_height // 2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0
        self.color = snake_col

    def turn(self, point):
        if not (self.length > 1 and (-point[0], -point[1]) == self.direction):
            self.direction = point

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0] + (x * tile_size)) % screen_width), (cur[1] + (y * tile_size)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.__init__()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect(p, (tile_size, tile_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, grid_col_1, r, width=2)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key in input_controls:
                self.turn(input_controls[event.key])


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = food_col
        self.position = random.randrange(grid_width) * tile_size, random.randrange(grid_height) * tile_size

    def draw(self, surface):
        r = pygame.Rect(self.position, [tile_size] * 2)
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, grid_col_1, r, width=2)
