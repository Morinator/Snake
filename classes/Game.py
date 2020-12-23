import sys
import time

import pygame as pg

from classes.Apple import Apple
from classes.Grid import Grid
from classes.Snake import Snake
from configs.colors import LIGHT_GREY, RED
from configs.settings import SCREEN_SIZE, GRID_SIZE, MAX_FPS, FONT, TEXT_POS


class Game:
    def __init__(self):
        self.score = 0
        self.grid = Grid(*GRID_SIZE)
        self.snake = Snake(self.grid)
        self.apple = Apple(self.grid)
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.paused = False
        self.finished = False

    def run(self):
        while not self.finished:
            self.clock.tick(MAX_FPS)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sys.exit()
                    if event.key == pg.K_p:
                        self.paused = not self.paused

                    self.snake.update_direction(event.key)
            if not self.paused:
                self.update_state()
            self.draw(self.screen)

    def update_state(self):
        has_collided = self.snake.move(self.grid)
        self.snake.update_color()
        if has_collided:
            self.finished = True

        if self.snake.li[0] == self.apple.pos:
            self.snake.eat()
            self.apple = Apple(self.grid)
            self.score += 1

    def draw(self, screen):
        [item.draw(screen) for item in [self.grid, self.apple, self.snake]]
        screen.blit(FONT.render(f"Score: {self.score}", True, LIGHT_GREY), TEXT_POS)
        if self.paused:
            self.screen.blit(FONT.render("Paused", True, RED), (200, 200))
        pg.display.update()

    def show_start_screen(self):
        self.screen.blit(FONT.render("Welcome", True, RED), (200, 200))
        pg.display.update()
        time.sleep(0.7)

    def show_end_screen(self):
        self.screen.blit(FONT.render("Erneut versagt, du Narr", True, RED), (10, 200))
        self.screen.blit(FONT.render("Klicken zum Beenden", True, RED), (10, 400))
        pg.display.update()
        while True:
            self.clock.tick(MAX_FPS)
            for event in pg.event.get():
                if event.type in [pg.MOUSEBUTTONDOWN, pg.QUIT]:
                    sys.exit()
