import pygame as pg
import settings as st

animationsPaths = [
    pg.image.load("imgs/player_idle_0.png"),
    pg.image.load("imgs/player_idle_1.png")]

class Player():
    def __init__(self, x, y):
        self.player = animationsPaths[0].convert_alpha()
        self.player = pg.transform.scale(self.player, (st.BLOCKS_WIDTH * 1.3, st.BLOCKS_HEIGHT * 1.3))

        self.rect = self.player.get_rect()
        self.rect.x = x
        self.rect.y = y

    def updateAnimations(self, iteration):
        self.player = animationsPaths[iteration // 30].convert_alpha()
        self.player = pg.transform.scale(self.player, (st.BLOCKS_WIDTH * 1.3, st.BLOCKS_HEIGHT * 1.3))
