import pygame as pg
from settings import * 
from tile import Tile
from player import Player
from debug import debug

class Level:

    def __init__(self):
        self.w_surface = pg.display.get_surface()

        self.visible_sp = YSortCameraGroup()
        self.obstacle_sp = pg.sprite.Group()

        self.create_world()

    def create_world(self):
        for row_i, row in enumerate(world):
            for obj_i, obj in enumerate(row):
                x = obj_i * tilesize
                y = row_i * tilesize

                if obj == 'r':
                    Tile((x,y), [self.visible_sp, self.obstacle_sp])
                elif obj == 'p':
                    self.player = Player((x,y), [self.visible_sp], self.obstacle_sp)
            # print(row_index)
            # print(row)
    
    def start(self):
        self.visible_sp.draw(self.w_surface)
        self.visible_sp.update()
        debug(self.player.direction)

class YSortCameraGroup(pg.sprite.Group):

    def __init__(self):
        super().__init__()
