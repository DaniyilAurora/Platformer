import pygame as pg
import settings as st

animationsIdle = [
    pg.image.load("imgs/player_idle_0.png"),
    pg.image.load("imgs/player_idle_1.png")
]

animationsWalking = [
    pg.image.load("imgs/player_walking_0.png"),
    pg.image.load("imgs/player_walking_1.png"),
    pg.image.load("imgs/player_walking_2.png"),
    pg.image.load("imgs/player_walking_3.png"),
    pg.image.load("imgs/player_walking_4.png"),
    pg.image.load("imgs/player_walking_5.png"),
]

class Player():
    def __init__(self, x, y):
        self.player = animationsIdle[0].convert_alpha()
        self.player = pg.transform.scale(self.player, (st.BLOCKS_WIDTH * 1.3, st.BLOCKS_HEIGHT * 1.3))

        self.rect = self.player.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.walking = False
        self.direction = "right"
        self.grounded = False

    def updateAnimations(self, iteration):
        if not self.walking:
            self.player = animationsIdle[iteration // 30].convert_alpha()
            self.player = pg.transform.scale(self.player, (st.BLOCKS_WIDTH * 1.3, st.BLOCKS_HEIGHT * 1.3))
            
            if self.direction == "left":
                self.player = pg.transform.flip(self.player, True, False)
        else:
            self.player = animationsWalking[iteration // 5 % 6].convert_alpha()
            self.player = pg.transform.scale(self.player, (st.BLOCKS_WIDTH * 1.3, st.BLOCKS_HEIGHT * 1.3))
            
            if self.direction == "left":
                self.player = pg.transform.flip(self.player, True, False)
