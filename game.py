import pygame as pg
import sys

class boardObj:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
    def calculateScreenPos(self, currentWidth, currentHeight, scale):
        xpos = (scale*self.x)+((currentWidth-(scale*10)) / 2)
        ypos = (scale*self.y)+((currentHeight-(scale*10))/2)
        return (xpos, ypos)
    def move(self, y, x, board):
        board[self.y][self.x] = None
        self.x, self.y = x, y
        board[y][x] = self
    def draw(screen, currentWidth, currentHeight, scale):
        pass

class Character(boardObj):
    def __init__(self, x, y):
        super().__init__(x, y)
    def draw(self, screen, currentWidth, currentHeight, scale):
        charImage = pg.image.load("Assets/Man.png")
        charImage = pg.transform.scale(charImage, (scale,scale))
        screen.blit(charImage, self.calculateScreenPos(currentWidth, currentHeight, scale))

class Enemy(boardObj):
    def __init__(self, x, y):
        super().__init__(x, y)
    def draw(self, screen, currentWidth, currentHeight, scale):
        charImage = pg.image.load("Assets/evil-test.png")
        charImage = pg.transform.scale(charImage, (scale,scale))
        screen.blit(charImage, self.calculateScreenPos(currentWidth, currentHeight, scale))
    def aiMove(self, mainCharacter, board):
        if (mainCharacter.x < self.x) and  board[self.y][self.x-1] is None:
            self.move(self.y, self.x-1, board)
        elif (mainCharacter.x > self.x) and  board[self.y][self.x+1] is None:
            self.move(self.y, self.x+1, board)
        elif (mainCharacter.y < self.y) and  board[self.y-1][self.x] is None:
            self.move(self.y-1, self.x, board)
        elif (mainCharacter.y > self.y) and  board[self.y+1][self.x] is None:
            self.move(self.y+1, self.x, board)
        



class Obstacle(boardObj):
    def __init__(self, x, y):
        super().__init__(x, y)
    def draw(self, screen, currentWidth, currentHeight, scale):
        surface = pg.Surface((scale, scale))
        surface.fill((255, 255, 255)) 
        pg.draw.rect(surface, (255, 255, 255), (0, 0, scale, scale))
        screen.blit(surface, self.calculateScreenPos(currentWidth, currentHeight, scale))


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
     

    board = [[None for a in range(10)] for b in range(10)]
    mainCharacter = Character(0, 0)
    board[0][0] = mainCharacter
    board[5][5] = Enemy(5, 5)
    board[6][6] = Obstacle(6, 6)
    running = True
    while running:
        framecount += 1
        screen.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_LEFT:
                        if mainCharacter.x > 0:
                            if board[mainCharacter.y][mainCharacter.x-1] is None:
                                mainCharacter.move(mainCharacter.y, mainCharacter.x-1, board)
                                for a in board:
                                    for b in a:
                                        if isinstance(b, Enemy):
                                            b.aiMove(mainCharacter, board)
                    case pg.K_RIGHT:
                        if mainCharacter.x < 9:
                            if board[mainCharacter.y][mainCharacter.x+1] is None:
                                mainCharacter.move(mainCharacter.y, mainCharacter.x+1, board)
                                for a in board:
                                    for b in a:
                                        if isinstance(b, Enemy):
                                            b.aiMove(mainCharacter, board)
                    case pg.K_UP:
                        if mainCharacter.y > 0:
                            if board[mainCharacter.y-1][mainCharacter.x] is None:
                                mainCharacter.move(mainCharacter.y-1, mainCharacter.x, board)
                                for a in board:
                                    for b in a:
                                        if isinstance(b, Enemy):
                                            b.aiMove(mainCharacter, board)
                    case pg.K_DOWN:
                        if mainCharacter.y < 9:
                            if board[mainCharacter.y+1][mainCharacter.x] is None:
                                mainCharacter.move(mainCharacter.y+1, mainCharacter.x, board)
                                for a in board:
                                    for b in a:
                                        if isinstance(b, Enemy):
                                            b.aiMove(mainCharacter, board)
            
        currentHeight = screen.get_height()
        currentWidth = screen.get_width()
        scale = screen.get_height() / 12
        for i in range(11):
            pg.draw.line(screen, (255, 255, 255), ((scale*i)+((currentWidth-(scale*10)) / 2), ((currentHeight-(scale*10))/2)), ((scale*i)+((currentWidth-(scale*10)) / 2), (scale*10) + ((currentHeight-(scale*10))/2)))
            pg.draw.line(screen, (255, 255, 255), (((currentWidth-(scale*10)) / 2), (scale*i)+((currentHeight-(scale*10))/2)), ((scale*10)+((currentWidth-(scale*10)) / 2), (scale*i) + ((currentHeight-(scale*10))/2)))
                
        for objy in board:
            for objx in objy:
                if objx is not None:
                    objx.draw(screen, currentWidth, currentHeight, scale)

        screen.blit(font.render(str(framecount),True,(255, 255, 255)),(0, 0))
        pg.display.flip()
        fpsClock.tick(fps)
    pg.quit()
    sys.exit()
if __name__ == "__main__":
    main()
