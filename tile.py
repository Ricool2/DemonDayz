import pygame as pg
from settings import *

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pg.image.load('./graph/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topright = pos)