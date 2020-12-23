import pygame as pg

# gameplay
GRID_SIZE = 15, 15
STARTING_LENGTH = 1
MAX_FPS = 6

# graphics
TILE_SIZE = 40
SCREEN_SIZE = TILE_SIZE * GRID_SIZE[0], TILE_SIZE * GRID_SIZE[1]
APPLE_SIZE = -(TILE_SIZE * 0.2)
SNAKE_SIZE = -(TILE_SIZE * 0.1)
# text
TEXT_POS = 10, 10
FONT = pg.font.Font('freesansbold.ttf', int(0.08 * SCREEN_SIZE[0]))