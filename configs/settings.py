import pygame as pg

# gameplay
GRID_SIZE = 15, 15
STARTING_LENGTH = 1

# graphics
MAX_FPS = 5
TILE_SIZE = 40
SCREEN_SIZE = TILE_SIZE * GRID_SIZE[0], TILE_SIZE * GRID_SIZE[1]
APPLE_SIZE = -10
# text
TEXT_POS = 10, 10
FONT = pg.font.Font('freesansbold.ttf', int(0.08 * SCREEN_SIZE[0]))
