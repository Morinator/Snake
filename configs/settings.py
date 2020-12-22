import pygame as pg

# gameplay
grid_size = 15, 15

# graphics
max_fps = 5
tile_size = 40
screen_size = tile_size * grid_size[0], tile_size * grid_size[1]

# text
text_pos = 10, 10
font = pg.font.Font('freesansbold.ttf', int(0.08 * screen_size[0]))
