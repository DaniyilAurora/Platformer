import pygame as pg
import settings as st

class Block():
    def __init__(self, x, y, blockType):
        self.block = pg.image.load(f'imgs/{blockType}.png').convert_alpha()
        self.block = pg.transform.scale(self.block, (st.BLOCKS_WIDTH, st.BLOCKS_HEIGHT))

        self.rect = self.block.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.blockType = blockType