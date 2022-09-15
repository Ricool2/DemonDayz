import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sp):
        super().__init__(groups)
        self.image = pg.image.load('./graph/player.png').convert_alpha()
        self.rect = self.image.get_rect(topright = pos)

        self.direction = pg.math.Vector2()
        self.speed = 5

        self.obstacle_sp = obstacle_sp

    def k_input(self):                  # get keyboard inputs
        keys = pg.key.get_pressed()

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

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sp:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:    # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:    # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sp:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:    # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:    # moving up
                        self.rect.top = sprite.rect.bottom


    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        # self.rect.center += self.direction * speed

    def update(self):
        self.k_input()
        self.move(self.speed)