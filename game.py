import pygame as pg

class boardObj:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

class Character(boardObj):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
    pass

def main():


    pg.init()

    fps = 60
    fpsClock = pg.time.Clock()
    info = pg.display.Info()
    width = int(info.current_w * (2/3))
    height = int(info.current_h * (2/3))

    screen = pg.display.set_mode((width, height), pg.RESIZABLE)
    gameLoop(screen, fps, fpsClock)


def gameLoop(screen, fps, fpsClock):
    boardObjs = []
    boardObjs.append(Character(0, 0, "test"))
    while True:
        
        screen.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        currentHeight = screen.get_height()
        currentWidth = screen.get_width()
        scale = screen.get_height() / 12
        for i in range(11):
            pg.draw.line(screen, (255, 255, 255), ((scale*i)+((currentWidth-(scale*10)) / 2), ((currentHeight-(scale*10))/2)), ((scale*i)+((currentWidth-(scale*10)) / 2), (scale*10) + ((currentHeight-(scale*10))/2)))
            pg.draw.line(screen, (255, 255, 255), (((currentWidth-(scale*10)) / 2), (scale*i)+((currentHeight-(scale*10))/2)), ((scale*10)+((currentWidth-(scale*10)) / 2), (scale*i) + ((currentHeight-(scale*10))/2)))
                
        for objs in boardObjs:
            if (isinstance(objs, Character)):
                pass

        pg.display.flip()
        fpsClock.tick(fps)

if __name__ == "__main__":
    main()
