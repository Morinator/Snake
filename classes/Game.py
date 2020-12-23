import sys
import time

import pygame as pg
from pygments.styles.paraiso_dark import RED

from classes.Apple import Apple
from classes.Grid import Grid
from classes.Snake import Snake
from configs.colors import LIGHT_GREY
from configs.settings import SCREEN_SIZE, GRID_SIZE, MAX_FPS, FONT, TEXT_POS


class Game:
    def __init__(self):
        self.score = 0
        self.grid = Grid(*GRID_SIZE)
        self.snake = Snake(self.grid)
        self.apple = Apple(self.grid)
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()

    def draw(self, screen):
        [item.draw(screen) for item in [self.grid, self.apple, self.snake]]
        screen.blit(FONT.render(f"Score: {self.score}", True, LIGHT_GREY), TEXT_POS)
        pg.display.update()

    def run(self):
        while True:
            self.clock.tick(MAX_FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sys.exit()
                    self.snake.update_direction(event.key)

            has_collided = self.snake.move(self.grid)
            self.snake.update_color()
            if has_collided:
                sys.exit()

            if self.snake.li[0] == self.apple.pos:
                self.snake.eat()
                self.apple = Apple(self.grid)
                self.score += 1

            self.draw(self.screen)

    def show_start_screen(self):
        self.screen.blit(FONT.render("Welcome", True, RED), (200, 200))
        pg.display.update()
        time.sleep(0.7)
