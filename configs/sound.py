import pygame as pg

# music
pg.mixer.music.load("assets/sounds/mario.mp3")
pg.mixer.music.set_volume(0.75)
pg.mixer.music.play()

# sounds
munch = pg.mixer.Sound("assets/sounds/munch.wav")
teleport_sound = pg.mixer.Sound("assets/sounds/teleport.wav")
