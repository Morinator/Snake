import os

import pygame as pg

sound_root = os.path.join(os.path.dirname(__file__), '..', 'assets', 'sounds')

# music
pg.mixer.music.load(os.path.join(sound_root, "mario.mp3"))
pg.mixer.music.set_volume(0.75)
pg.mixer.music.play(-1)  # on loop

# sounds
MUNCH_SOUND = pg.mixer.Sound(os.path.join(sound_root, "munch.wav"))
TELEPORTATION_SOUND = pg.mixer.Sound(os.path.join(sound_root, "teleport.wav"))
