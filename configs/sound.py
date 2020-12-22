import pygame as pg

music_path = "assets/sounds/mario.mp3"
pg.mixer.music.load(music_path)
pg.mixer.music.play()

bite = pg.mixer.Sound("assets/sounds/bite.wav")
laser = pg.mixer.Sound("assets/sounds/laser.wav")
explosion = pg.mixer.Sound("assets/sounds/explosion.wav")