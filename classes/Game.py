import pygame as pg

from configs.settings import SCREEN_SIZE


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()

    def run(self):
        pass

    def draw(self):
        pass

    def show_start_screen(self):
        pass

    def new_game(self):
        pass