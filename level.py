import pygame as pg
from settings import * 
from tile import Tile
from player import Player
from debug import debug

class Level:

    def __init__(self):
        self.w_surface = pg.display.get_surface()

        self.visible_sp = YSortCameraGroup()
        #self.visible_sp = pg.sprite.Group()
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
        self.visible_sp.custom_draw(self.player)
        #self.visible_sp.draw(self.w_surface)
        self.visible_sp.update()
        debug(self.player.direction)

class YSortCameraGroup(pg.sprite.Group):    #

    def __init__(self):
        super().__init__()
        self.w_surface = pg.display.get_surface()
        self.half_w = self.w_surface.get_size()[0] // 2
        self.half_h = self.w_surface.get_size()[1] // 2
        self.offset =pg.math.Vector2()

    def custom_draw(self, player):          #кастомное отображение спрайтов

        self.offset.x = player.rect.centerx - self.half_w
        self.offset.y = player.rect.centery - self.half_h

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset      #отход от левого верхнего края
            self.w_surface.blit(sprite.image, offset_pos)
