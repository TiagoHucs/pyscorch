import pygame as pg


class Sound:
    def __init__(self):
        pg.mixer.init()
        self.path = 'resources/sounds/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        pg.mixer.music.set_volume(0.3)