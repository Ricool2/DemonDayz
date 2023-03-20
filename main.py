import pygame as pg
import sys
from settings import *      # импорт всех настроек
from level import Level     # импорт класса заполнения мира
#from debug import debug

class Game:                 # класс игры

    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((w_width[1], w_height[1]))
        #self.window = pg.display.set_mode((1280, 720))              # задает размер окна
        pg.display.set_caption('Demon Dayz')                        # название окна
        self.clock = pg.time.Clock()                                # тикрейт?
        self.level = Level()                                        # заполняет по классу

    def start(self):
        # self.k_quit = pg.key.get_pressed()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                

            self.window.fill('black')
            self.level.start()
            #debug('gogog')
            pg.display.update()
            self.clock.tick(fps)

if __name__ == '__main__':
    game = Game()
    game.start()