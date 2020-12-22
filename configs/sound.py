import pygame as pg

music_path = "assets/sounds/mario.mp3"
pg.mixer.music.load(music_path)
pg.mixer.music.set_volume(0.75)
pg.mixer.music.play()

bite = pg.mixer.Sound("assets/sounds/bite.wav")
teleport = pg.mixer.Sound("assets/sounds/teleport.wav")