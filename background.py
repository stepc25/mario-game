import pygame as pg

class Background():
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.background = pg.image.load(f'img/level/1-0.png')
        self.background = pg.transform.scale(self.background,
                                  (int(self.settings.screen_width*self.settings.background_multiplier),
                                  int(self.settings.screen_height)))
        self.rect = self.background.get_rect()
        self.rect = self.rect.move((0,0))
        
    def update(self,x_shift):
        self.rect.x += x_shift