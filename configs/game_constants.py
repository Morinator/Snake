import pygame as pg

up, down, left, right = (0, -1), (0, 1), (-1, 0), (1, 0)

arrow_key_to_direction = {
    **dict.fromkeys([pg.K_UP, pg.K_w], up),
    **dict.fromkeys([pg.K_LEFT, pg.K_a], left),
    **dict.fromkeys([pg.K_DOWN, pg.K_s], down),
    **dict.fromkeys([pg.K_RIGHT, pg.K_d], right),
}
