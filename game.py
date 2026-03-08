import pygame as pg
import sys
import ai
import copy


class boardObj:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def calculateScreenPos(self, currentWidth, currentHeight, scale, size):
        xpos = (scale*self.x)+((currentWidth-(scale*size)) / 2)
        ypos = (scale*self.y)+((currentHeight-(scale*size))/2)
        return (xpos, ypos)
    
    def move(self, y, x, board):
        board[self.y][self.x] = None
        self.x, self.y = x, y
        board[y][x] = self


class Character(boardObj):

    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen, currentWidth, currentHeight, scale, size):
        charImage = pg.image.load("Assets/Man.png")
        charImage = pg.transform.scale(charImage, (scale,scale))
        screen.blit(charImage, self.calculateScreenPos(currentWidth, currentHeight, scale, size))


class Enemy(boardObj):

    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen, currentWidth, currentHeight, scale, size):
        charImage = pg.image.load("Assets/evil-man.png")
        charImage = pg.transform.scale(charImage, (scale,scale))
        screen.blit(charImage, self.calculateScreenPos(currentWidth, currentHeight, scale, size))

    def aiMove(self, mainCharacter, board):
        newboard = [[0 for a in range(len(board))] for b in range(len(board))]
        for i, a in enumerate(board):
            for p, b in enumerate(a):
                if isinstance(b, Character):
                    newboard[i][p] = 1
                elif isinstance(b, Obstacle):
                    newboard[i][p] = 2
                elif isinstance(b, Enemy):
                    newboard[i][p] = 3
                elif isinstance(b, Finish):
                    newboard[i][p] = 4

        dx, dy = ai.ai(newboard, self.x, self.y)

        if (dx != 0):
            self.move(self.y, self.x+dx, board)
        elif (dy != 0):
            self.move(self.y+dy, self.x, board)


class Finish(boardObj):

    def __init__(self, x, y):
        super().__init__(x, y)
    
    def draw(self, screen, currentWidth, currentHeight, scale, size):
        surface = pg.Surface((scale, scale))
        surface.fill((0, 255, 0))
        pg.draw.rect(surface, (0,255,0), (0,0,scale,scale))
        screen.blit(surface, self.calculateScreenPos(currentWidth,currentHeight,scale,size))


class Obstacle(boardObj):

    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen, currentWidth, currentHeight, scale, size):
        surface = pg.Surface((scale, scale))
        surface.fill((255,255,255))
        pg.draw.rect(surface,(255,255,255),(0,0,scale,scale))
        screen.blit(surface, self.calculateScreenPos(currentWidth,currentHeight,scale,size))


def loadlevel(data, size):
    board = [[None for a in range(size)] for b in range(size)]

    for obj in data:
        board[obj.y][obj.x] = obj

    return board


def finishfunc():
    print("YOU WON")


def losefunc():
    print("YOU LOSE")


def gameLoop(screen, fps, fpsClock, data, size=10):

    origdata = copy.deepcopy(data)

    framecount = 0
    font = pg.font.Font(None,20)

    board = loadlevel(data, size)

    mainCharacter = data[0]

    running = True
    wincon = 0

    while running:

        framecount += 1
        screen.fill((0,0,0))

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:

                dx = 0
                dy = 0

                match event.key:

                    case pg.K_LEFT | pg.K_a:
                        if mainCharacter.x > 0:
                            dx = -1
                    
                    case pg.K_RIGHT | pg.K_d:
                        if mainCharacter.x < size-1:
                            dx = 1

                    case pg.K_UP | pg.K_w:
                        if mainCharacter.y > 0:
                            dy = -1

                    case pg.K_DOWN | pg.K_s:
                        if mainCharacter.y < size-1:
                            dy = 1

                    case pg.K_ESCAPE | pg.K_DELETE:
                        running = False

                if (dy or dx):

                    if isinstance(board[mainCharacter.y+dy][mainCharacter.x+dx], Finish):
                        wincon = 2
                        running = False

                    if board[mainCharacter.y+dy][mainCharacter.x+dx] is None:

                        mainCharacter.move(mainCharacter.y+dy, mainCharacter.x+dx, board)

                        newboard = [row.copy() for row in board]

                        for a in newboard:
                            for b in a:

                                if isinstance(b, Enemy):

                                    b.aiMove(mainCharacter, board)

                                    if (abs(b.x-mainCharacter.x)+abs(b.y-mainCharacter.y)<=1):
                                        wincon = 1
                                        running = False

        currentHeight,currentWidth = screen.get_height(),screen.get_width()
        scale = screen.get_height()/(size*1.2)

        for i in range(size+1):

            pg.draw.line(screen,(255,255,255),
            ((scale*i)+((currentWidth-(scale*size))/2),((currentHeight-(scale*size))/2)),
            ((scale*i)+((currentWidth-(scale*size))/2),(scale*size)+((currentHeight-(scale*size))/2)))

            pg.draw.line(screen,(255,255,255),
            (((currentWidth-(scale*size))/2),(scale*i)+((currentHeight-(scale*size))/2)),
            ((scale*size)+((currentWidth-(scale*size))/2),(scale*i)+((currentHeight-(scale*size))/2)))

        for objy in board:
            for objx in objy:
                if objx is not None:
                    objx.draw(screen,currentWidth,currentHeight,scale,size)

        screen.blit(font.render(str(framecount),True,(255,255,255)),(0,0))

        pg.display.flip()
        fpsClock.tick(fps)

    done(wincon,screen,fps,fpsClock,origdata,size)


def nextlevel():
    pass


def done(wincon,screen,fps,fpsClock,data,size):

    if wincon == 0:
        pg.quit()
        sys.exit()

    else:

        running2 = True
        hover = 0

        while running2:

            currentHeight = screen.get_height()
            currentWidth = screen.get_width()

            font = pg.font.Font("Assets/Eight-Bit Madness.ttf", int(currentHeight/20))

            if wincon == 1:
                text1 = font.render(" Retry? ",True,"white")
            else:
                text1 = font.render(" Next Level? ",True,"white")

            text2 = font.render(" Return to Menu ",True,"white")

            rect1 = text1.get_rect(topleft=(currentWidth//2-text1.get_width()//2,((currentHeight-200)/2)+int(currentHeight/20)*1.8))
            rect2 = text2.get_rect(topleft=(currentWidth//2-text2.get_width()//2,((currentHeight-200)/2)+int(currentHeight/20)*3.6))

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    running2 = False

                if event.type == pg.MOUSEMOTION:
                    if rect1.collidepoint(event.pos):
                        hover = 1
                    elif rect2.collidepoint(event.pos):
                        hover = 2
                    else:
                        hover = 0

                if event.type == pg.MOUSEBUTTONDOWN:
                    if rect1.collidepoint(event.pos):
                        hover = 3
                    elif rect2.collidepoint(event.pos):
                        hover = 4

                if event.type == pg.MOUSEBUTTONUP:

                    if rect1.collidepoint(event.pos):
                        if wincon == 1:
                            gameLoop(screen,fps,fpsClock,data,size)
                        else:
                            nextlevel()

                    elif rect2.collidepoint(event.pos):
                        running2 = False


            screen.fill((255,0,0))

            bg_img = pg.image.load("Assets/Menu.png")
            bg_scaled = pg.transform.scale(bg_img,(currentWidth,currentHeight))
            screen.blit(bg_scaled,(0,0))

            padding = 30
            box_left = min(rect1.left,rect2.left) - padding
            box_top = rect1.top - padding
            box_right = max(rect1.right,rect2.right) + padding
            box_bottom = rect2.bottom + padding

            menu_rect = pg.Rect(box_left,box_top,box_right-box_left,box_bottom-box_top)

            panel = pg.Surface((menu_rect.width,menu_rect.height),pg.SRCALPHA)
            pg.draw.rect(panel,(0,0,0,140),(0,0,menu_rect.width,menu_rect.height),border_radius=20)
            screen.blit(panel,menu_rect.topleft)

            if hover == 1:
                pg.draw.rect(screen,(67,67,67,67),rect1,0,10)
            if hover == 3:
                pg.draw.rect(screen,(45,45,45,45),rect1,0,10)

            screen.blit(text1,rect1)

            if hover == 2:
                pg.draw.rect(screen,(67,67,67,67),rect2,0,10)
            if hover == 4:
                pg.draw.rect(screen,(45,45,45,45),rect2,0,10)

            screen.blit(text2,rect2)

            pg.display.flip()
            fpsClock.tick(fps)