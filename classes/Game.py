import sys

import pygame as pg

from classes.Apple import Apple
from classes.Grid import Grid
from classes.Snake import Snake
from constants.colors import LIGHT_GREY, RED
from constants.settings import SCREEN_SIZE, GRID_SIZE, MAX_FPS, FONT, SCORE_POS, LIVES_POS, STARTING_LIVES


class Game:
    def __init__(self):
        self.score = 0
        self.grid = Grid(*GRID_SIZE)
        self.snake = Snake(self.grid)
        self.apple = Apple(self.grid)
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.paused = False
        self.curr_events = None
        self.lives = STARTING_LIVES

    def run(self):
        while self.lives > 0:
            self.clock.tick(MAX_FPS)
            self.curr_events = pg.event.get()
            for event in self.curr_events:
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key in [pg.K_ESCAPE, pg.K_p]:
                        self.paused = not self.paused
            if not self.paused:
                self.update_state()
            self.draw(self.screen)

    def update_state(self):
        for event in self.curr_events:
            if event.type == pg.KEYDOWN:
                self.snake.update_direction(event.key)

        has_collided = self.snake.move(self.grid)
        self.snake.update_color()
        if has_collided:
            self.lives -= 1

        if self.snake.li[0] == self.apple.pos:
            self.snake.eat()
            self.apple = Apple(self.grid)
            self.score += 1

    def draw(self, screen):
        [item.draw(screen) for item in [self.grid, self.apple, self.snake]]
        screen.blit(FONT.render(f"Score: {self.score}", True, LIGHT_GREY), SCORE_POS)
        screen.blit(FONT.render(f"Lives: {self.lives}", True, LIGHT_GREY), LIVES_POS)


        if self.paused:
            self.screen.blit(FONT.render("Paused", True, RED), (200, 200))
        pg.display.update()

    def show_end_screen(self):
        self.screen.blit(FONT.render("Erneut versagt, du Narr", True, RED), (25, 200))
        self.screen.blit(FONT.render("Klicken zum Beenden", True, RED), (25, 400))
        pg.display.update()
        while True:
            self.clock.tick(MAX_FPS)
            [sys.exit() for event in pg.event.get() if event.type in [pg.MOUSEBUTTONDOWN, pg.QUIT]]
