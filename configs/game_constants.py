import pygame as pg

up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)
arrow_key_to_direction = {pg.K_LEFT: left, pg.K_RIGHT: right, pg.K_DOWN: down, pg.K_UP: up}
