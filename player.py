import pygame as pg
import sys
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sp):
        super().__init__(groups)
        self.image = pg.image.load('./graph/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -24)

        self.direction = pg.math.Vector2()
        self.speed = 5

        self.obstacle_sp = obstacle_sp

    def k_input(self):                  # get keyboard inputs
        keys = pg.key.get_pressed()

        # move_keys = {1:pg.K_w, 2:pg.K_s, 3:pg.K_a, 4:pg.K_d}

        # for key in move_keys:
        #     se
        if keys[pg.K_w]:               # for key UP change direction on 2D graph
            self.direction.y = -1
        elif keys[pg.K_s]:           # for key DOWN change direction on 2D graph
            self.direction.y = 1
        else:
            # pass
            self.direction.y = 0        # moves nowhere for any other or double keys
        
        if keys[pg.K_a]:               # for key LEFT change direction on 2D graph
            self.direction.x = -1
        elif keys[pg.K_d]:            # for key RIGHT change direction on 2D graph
            self.direction.x = 1
        else:
            # pass
            self.direction.x = 0 

        if keys[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sp:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:    # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:    # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sp:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:    # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:    # moving up
                        self.hitbox.top = sprite.hitbox.bottom


    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def update(self):
        self.k_input()
        self.move(self.speed)