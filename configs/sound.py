import pygame as pg

# music
pg.mixer.music.load("assets/sounds/mario.mp3")
pg.mixer.music.set_volume(0.75)
pg.mixer.music.play(-1)  # on loop

# sounds
munch_sound = pg.mixer.Sound("assets/sounds/munch.wav")
teleportation_sound = pg.mixer.Sound("assets/sounds/teleport.wav")
