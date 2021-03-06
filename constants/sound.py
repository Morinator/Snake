from os import path

import pygame as pg

sound_root = path.join(path.dirname(__file__), '..', 'assets', 'sounds')

# sound effects
MUNCH_SOUND = pg.mixer.Sound(path.join(sound_root, "munch.wav"))
TELEPORTATION_SOUND = pg.mixer.Sound(path.join(sound_root, "teleport.wav"))
EXPLOSION_SOUNDS = [pg.mixer.Sound(path.join(sound_root, f"expl{nr}.wav")) for nr in (3, 6)]
