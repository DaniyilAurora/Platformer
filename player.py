import pygame as pg
import settings as st

class Player():
    def __init__(self, x, y):
        self.player = pg.image.load("imgs/player.png").convert_alpha()
        self.player = pg.transform.scale(self.player, (st.BLOCKS_WIDTH * 1.3, st.BLOCKS_HEIGHT * 1.3))

        self.rect = self.player.get_rect()
        self.rect.x = x
        self.rect.y = y