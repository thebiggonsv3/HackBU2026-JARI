import pygame as pg
import sys
import ai

# Board object which is the base class that all other board objects are based on
class boardObj:

    # Initialization function
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    # Calculuates screen position from board coordanites
    def calculateScreenPos(self, currentWidth, currentHeight, scale, size):
        xpos = (scale*self.x)+((currentWidth-(scale*size)) / 2)
        ypos = (scale*self.y)+((currentHeight-(scale*size))/2)
        return (xpos, ypos)
    
    # Moves Board object on the board
    def move(self, y, x, board):
        board[self.y][self.x] = None
        self.x, self.y = x, y
        board[y][x] = self

# Character class which inherits from the Board Object Class
class Character(boardObj):

    # Initialization function for Characcter (calls board object initialization)
    def __init__(self, x, y):
        super().__init__(x, y)

    # Draws character to screen using an image
    def draw(self, screen, currentWidth, currentHeight, scale, size):
        charImage = pg.image.load("Assets/Man.png")
        charImage = pg.transform.scale(charImage, (scale,scale))
        screen.blit(charImage, self.calculateScreenPos(currentWidth, currentHeight, scale, size))

# Enemy class which inherits from the Board Object Class
class Enemy(boardObj):

    # Initialization function for Enemy (calls board object initialization)
    def __init__(self, x, y):
        super().__init__(x, y)

    # Draws Enemy to screen using an image
    def draw(self, screen, currentWidth, currentHeight, scale, size):
        charImage = pg.image.load("Assets/evil-man.png")
        charImage = pg.transform.scale(charImage, (scale,scale))
        screen.blit(charImage, self.calculateScreenPos(currentWidth, currentHeight, scale, size))

    # Basic AI for Enemy (moves towards player based on relative x and y position)
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
        pg.draw.rect(surface, (0, 255, 0), (0, 0, scale, scale))
        screen.blit(surface, self.calculateScreenPos(currentWidth, currentHeight, scale, size))


# Obstacle nemy class which inherits from the Board Object Class
class Obstacle(boardObj):

    # Initialization function for Obstacle (calls board object initialization)
    def __init__(self, x, y):
        super().__init__(x, y)

    # Draws Obstacle to the screen by creating a rectangle
    def draw(self, screen, currentWidth, currentHeight, scale, size):
        surface = pg.Surface((scale, scale))
        surface.fill((255, 255, 255)) 
        pg.draw.rect(surface, (255, 255, 255), (0, 0, scale, scale))
        screen.blit(surface, self.calculateScreenPos(currentWidth, currentHeight, scale, size))


# Reformats level data into board data
def loadlevel(data, size):
    board = [[None for a in range(size)] for b in range(size)]

    for obj in data:
        board[obj.y][obj.x] = obj

    return board

def finishfunc():
    print("YOU WON")
    pass

def losefunc():
    print("YOU LOSE")
    pass

# Game function 
def gameLoop(screen, fps, fpsClock, data, size=10):

    # Variable initialization
    framecount = 0
    font=pg.font.Font(None,20)

    board = loadlevel(data, size)

    # Initializes boardObjects to the board
    mainCharacter = data[0]

    # main gameloop
    running = True
    
    while running:

        # reset screen and increment frame counter
        framecount += 1
        screen.fill((0, 0, 0))

        # Event handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            # Key input handler (moves character and ai if possible)
            if event.type == pg.KEYDOWN:
                dx = 0
                dy = 0
                match event.key:

                    # Left arrow detection
                    case pg.K_LEFT | pg.K_a:
                        if mainCharacter.x > 0:
                            dx = -1
                    
                    # Right arrow detection
                    case pg.K_RIGHT | pg.K_d:
                        if mainCharacter.x < size-1:
                            dx = 1

                    # Up arrow detection
                    case pg.K_UP | pg.K_w:
                        if mainCharacter.y > 0:
                            dy = -1

                    # Down arrow detection
                    case pg.K_DOWN | pg.K_s:
                        if mainCharacter.y < size-1:
                            dy = 1

                    # Quit Functionality
                    case pg.K_ESCAPE | pg.K_DELETE:
                        running = False
                            
                # Functionality based on arrow movement
                if (dy or dx):
                    if isinstance(board[mainCharacter.y+dy][mainCharacter.x+dx], Finish):
                        finishfunc()
                    if board[mainCharacter.y+dy][mainCharacter.x+dx] is None:
                        mainCharacter.move(mainCharacter.y+dy, mainCharacter.x+dx, board)
                        newboard = [row.copy() for row in board]
                        for a in newboard:
                            for b in a:
                                if isinstance(b, Enemy):
                                    b.aiMove(mainCharacter, board)
                                    if (abs(b.x - mainCharacter.x) + abs(b.y - mainCharacter.y) <= 1):
                                        losefunc()
                                        running = False
            

        # Gets current height and width of the window and gets the standard scale for the board/grid
        currentHeight, currentWidth  = screen.get_height(), screen.get_width()
        scale = screen.get_height() / (size * 1.2)

        # Draws grid lines to the screen
        for i in range(size+1):
            pg.draw.line(screen, (255, 255, 255), ((scale*i)+((currentWidth-(scale*size)) / 2), ((currentHeight-(scale*size))/2)), ((scale*i)+((currentWidth-(scale*size)) / 2), (scale*size) + ((currentHeight-(scale*size))/2)))
            pg.draw.line(screen, (255, 255, 255), (((currentWidth-(scale*size)) / 2), (scale*i)+((currentHeight-(scale*size))/2)), ((scale*size)+((currentWidth-(scale*size)) / 2), (scale*i) + ((currentHeight-(scale*size))/2)))
                
        # Draws boardObjects to the board
        for objy in board:
            for objx in objy:
                if objx is not None:
                    objx.draw(screen, currentWidth, currentHeight, scale, size)


        #Draws frame counter and updates the screen
        screen.blit(font.render(str(framecount),True,(255, 255, 255)),(0, 0))
        pg.display.flip()
        fpsClock.tick(fps)
    pg.quit()
    sys.exit()
