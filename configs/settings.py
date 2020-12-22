import pygame as pg

max_fps = 6

tile_size = 50
grid_size = 15, 15

screen_size = tile_size * grid_size[0], tile_size * grid_size[1]
text_pos = 10, 10
font = pg.font.Font('freesansbold.ttf', int(0.08 * screen_size[0]))
