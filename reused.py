import pygame as pg

def init():
    pg.init()

    fps = 60
    fpsClock = pg.time.Clock()
    info = pg.display.Info()
    width = int(info.current_w * (2/3))
    height = int(info.current_h * (2/3))
    screen = pg.display.set_mode((width, height), pg.RESIZABLE)

    return screen, fpsClock, fps, width, height