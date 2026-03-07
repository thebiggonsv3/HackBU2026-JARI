import pygame as pg

class boardObj:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
    def calculateScreenPos(self, currentWidth, currentHeight, scale):
        xpos = (scale*self.x)+((currentWidth-(scale*10)) / 2)
        ypos = (scale*self.y)+((currentHeight-(scale*10))/2)
        return (xpos, ypos)
    def draw(screen, currentWidth, currentHeight, scale):
        pass

class Character(boardObj):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)
    def draw(self, screen, currentWidth, currentHeight, scale):
        charImage = pg.image.load("test.png")
        screen.blit(charImage, self.calculateScreenPos(currentWidth, currentHeight, scale))


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
    framecount = 0
    font=pg.font.Font(None,20)
     

    mainCharacter = Character(0, 0, "test")
    boardObjs = [mainCharacter]
    while True:
        framecount += 1
        screen.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_LEFT:
                        if mainCharacter.x > 0:
                            mainCharacter.x -= 1
                    case pg.K_RIGHT:
                        if mainCharacter.x < 9:
                            mainCharacter.x += 1
                    case pg.K_DOWN:
                        if mainCharacter.y < 9:
                            mainCharacter.y += 1
                    case pg.K_UP:
                        if mainCharacter.y > 0:
                            mainCharacter.y -= 1
            
        currentHeight = screen.get_height()
        currentWidth = screen.get_width()
        scale = screen.get_height() / 12
        for i in range(11):
            pg.draw.line(screen, (255, 255, 255), ((scale*i)+((currentWidth-(scale*10)) / 2), ((currentHeight-(scale*10))/2)), ((scale*i)+((currentWidth-(scale*10)) / 2), (scale*10) + ((currentHeight-(scale*10))/2)))
            pg.draw.line(screen, (255, 255, 255), (((currentWidth-(scale*10)) / 2), (scale*i)+((currentHeight-(scale*10))/2)), ((scale*10)+((currentWidth-(scale*10)) / 2), (scale*i) + ((currentHeight-(scale*10))/2)))
                
        for objs in boardObjs:
            objs.draw(screen, currentWidth, currentHeight, scale)

        screen.blit(font.render(str(framecount),True,(255, 255, 255)),(0, 0))
        pg.display.flip()
        fpsClock.tick(fps)

if __name__ == "__main__":
    main()
