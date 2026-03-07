import pygame as pg
import sys


# Board object which is the base class that all other board objects are based on
class boardObj:

    # Initialization function
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    # Calculuates screen position from board coordanites
    def calculateScreenPos(self, currentWidth, currentHeight, scale):
        xpos = (scale*self.x)+((currentWidth-(scale*10)) / 2)
        ypos = (scale*self.y)+((currentHeight-(scale*10))/2)
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
    def draw(self, screen, currentWidth, currentHeight, scale):
        charImage = pg.image.load("Assets/Man.png")
        charImage = pg.transform.scale(charImage, (scale,scale))
        screen.blit(charImage, self.calculateScreenPos(currentWidth, currentHeight, scale))


# Enemy class which inherits from the Board Object Class
class Enemy(boardObj):

    # Initialization function for Enemy (calls board object initialization)
    def __init__(self, x, y):
        super().__init__(x, y)

    # Draws Enemy to screen using an image
    def draw(self, screen, currentWidth, currentHeight, scale):
        charImage = pg.image.load("Assets/evil-test.png")
        charImage = pg.transform.scale(charImage, (scale,scale))
        screen.blit(charImage, self.calculateScreenPos(currentWidth, currentHeight, scale))

    # Basic AI for Enemy (moves towards player based on relative x and y position)
    def aiMove(self, mainCharacter, board):
        if (mainCharacter.x < self.x) and  board[self.y][self.x-1] is None:
            self.move(self.y, self.x-1, board)
        elif (mainCharacter.x > self.x) and  board[self.y][self.x+1] is None:
            self.move(self.y, self.x+1, board)
        elif (mainCharacter.y < self.y) and  board[self.y-1][self.x] is None:
            self.move(self.y-1, self.x, board)
        elif (mainCharacter.y > self.y) and  board[self.y+1][self.x] is None:
            self.move(self.y+1, self.x, board)
        


# Obstacle nemy class which inherits from the Board Object Class
class Obstacle(boardObj):

    # Initialization function for Obstacle (calls board object initialization)
    def __init__(self, x, y):
        super().__init__(x, y)

    # Draws Obstacle to the screen by creating a rectangle
    def draw(self, screen, currentWidth, currentHeight, scale):
        surface = pg.Surface((scale, scale))
        surface.fill((255, 255, 255)) 
        pg.draw.rect(surface, (255, 255, 255), (0, 0, scale, scale))
        screen.blit(surface, self.calculateScreenPos(currentWidth, currentHeight, scale))


#Main Function for testing
def main():
    pg.init()

    fps = 60
    fpsClock = pg.time.Clock()
    info = pg.display.Info()
    width = int(info.current_w * (2/3))
    height = int(info.current_h * (2/3))

    screen = pg.display.set_mode((width, height), pg.RESIZABLE)
    gameLoop(screen, fps, fpsClock)



# Game function 
def gameLoop(screen, fps, fpsClock):

    # Variable initialization
    framecount = 0
    font=pg.font.Font(None,20)

    # Creates an empty board full of None variables
    board = [[None for a in range(10)] for b in range(10)]

    # Initializes boardObjects to the board
    mainCharacter = Character(0, 0)
    board[0][0] = mainCharacter

    enemy = Enemy(5,5)
    board[5][5] = enemy

    enemies = [enemy]

    board[6][6] = Obstacle(6, 6)

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
                    case pg.K_LEFT:
                        if mainCharacter.x > 0:
                            dx = -1
                    
                    # Right arrow detection
                    case pg.K_RIGHT:
                        if mainCharacter.x < 9:
                            dx = 1

                    # Up arrow detection
                    case pg.K_UP:
                        if mainCharacter.y > 0:
                            dy = -1

                    # Down arrow detection
                    case pg.K_DOWN:
                        if mainCharacter.y < 9:
                            dy = 1
                        
                # Functionality based on arrow movement
                if (dy != 0 or dx != 0):
                    if board[mainCharacter.y+dy][mainCharacter.x+dx] is None:
                        mainCharacter.move(mainCharacter.y+dy, mainCharacter.x+dx, board)

                        for enemy in enemies:
                            enemy.aiMove(mainCharacter, board)
            

        # Gets current height and width of the window and gets the standard scale for the board/grid
        currentHeight = screen.get_height()
        currentWidth = screen.get_width()
        scale = screen.get_height() / 12

        # Draws grid lines to the screen
        for i in range(11):
            pg.draw.line(screen, (255, 255, 255), ((scale*i)+((currentWidth-(scale*10)) / 2), ((currentHeight-(scale*10))/2)), ((scale*i)+((currentWidth-(scale*10)) / 2), (scale*10) + ((currentHeight-(scale*10))/2)))
            pg.draw.line(screen, (255, 255, 255), (((currentWidth-(scale*10)) / 2), (scale*i)+((currentHeight-(scale*10))/2)), ((scale*10)+((currentWidth-(scale*10)) / 2), (scale*i) + ((currentHeight-(scale*10))/2)))
                
        # Draws boardObjects to the board
        for objy in board:
            for objx in objy:
                if objx is not None:
                    objx.draw(screen, currentWidth, currentHeight, scale)


        #Draws frame counter and updates the screen
        screen.blit(font.render(str(framecount),True,(255, 255, 255)),(0, 0))
        pg.display.flip()
        fpsClock.tick(fps)
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()