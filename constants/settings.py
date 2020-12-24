import pygame as pg

# gameplay
GRID_SIZE = 15, 15
STARTING_LENGTH = 1
MAX_FPS = 6
STARTING_LIVES = 3

# graphics
TILE_SIZE = 40
SCREEN_SIZE = TILE_SIZE * GRID_SIZE[0], TILE_SIZE * GRID_SIZE[1]
APPLE_SIZE = -(TILE_SIZE * 0.2)
SNAKE_SIZE = -(TILE_SIZE * 0.1)

# text
SCORE_POS = 10, 10
LIVES_POS = 0.7 * (SCREEN_SIZE[0]), 10
FONT = pg.font.Font(pg.font.match_font('arial'), int(0.08 * SCREEN_SIZE[0]))
