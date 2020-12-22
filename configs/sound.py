import pygame as pg

music_path = "assets/sounds/mario.mp3"
pg.mixer.music.load(music_path)
pg.mixer.music.play()

bite_path = "assets/sounds/bite.mp3"
laser = pg.mixer.Sound("assets/sounds/bite.wav")
explosion = pg.mixer.Sound("assets/sounds/explosion.wav")