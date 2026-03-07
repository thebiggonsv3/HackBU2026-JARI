import pygame as pg
pg.init()
screen = pg.display.set_mode((800, 600))
bg_image = pg.image.load("Assets/Menu.png").convert()
print(bg_image.get_size())
pg.quit()