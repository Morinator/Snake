import pygame as pg

# music
pg.mixer.music.load("assets/sounds/mario.mp3")
pg.mixer.music.set_volume(0.75)
pg.mixer.music.play(-1)  # on loop

# sounds
MUNCH_SOUND = pg.mixer.Sound("assets/sounds/munch.wav")
TELEPORTATION_SOUND = pg.mixer.Sound("assets/sounds/teleport.wav")
