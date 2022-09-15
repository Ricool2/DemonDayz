import pygame as pg
pg.init()
font = pg.font.Font(None, 30)

def debug(info, y = 100, x = 100):
    w_surface = pg.display.get_surface()
    debug_surf = font.render(str(info), True, 'Black')
    debug_rect = debug_surf.get_rect(center = (x,y))
    pg.draw.rect(w_surface, 'White', debug_rect)
    w_surface.blit(debug_surf, debug_rect)
