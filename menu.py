import pygame as pg
import sys
from levels import levelMenu

pg.init()

fps = 60
fpsClock = pg.time.Clock()

info = pg.display.Info()
width = int(info.current_w * (2/3))
height = int(info.current_h * (2/3))

screen = pg.display.set_mode((width, height), pg.RESIZABLE)

font = pg.font.SysFont("Arial", 30)

title = font.render("GAME", True, "black")
text1 = font.render(" START ", True, "black")
text2 = font.render(" HELP ", True, "black")
text3 = font.render(" QUIT ", True, "black")



# Background color
bg = (255, 255, 255)

running = True
while running:
    currentHeight = screen.get_height()
    currentWidth = screen.get_width()
    title_rect = title.get_rect(topleft=(currentWidth // 2 - title.get_width() // 2, ((currentHeight-200)/2)))
    rect1 = text1.get_rect(topleft=(currentWidth // 2 - text1.get_width() // 2, ((currentHeight-200)/2) + 100))
    rect2 = text2.get_rect(topleft=(currentWidth // 2 - text2.get_width() // 2, ((currentHeight-200)/2) + 150))
    rect3 = text3.get_rect(topleft=(currentWidth // 2 - text3.get_width() // 2, ((currentHeight-200)/2) + 200))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos):
                levelMenu(fps, fpsClock, screen)

            if rect2.collidepoint(event.pos):
                pass

            if rect3.collidepoint(event.pos):
                running = False

    screen.fill(bg)

    # Prints the title
    screen.blit(title, title_rect)

    # Prints the buttons
    pg.draw.rect(screen, (255,0,0), rect1, 2)

    screen.blit(text1, rect1)
    pg.draw.rect(screen, (255,0,0), rect1, 2)

    screen.blit(text2, rect2)
    pg.draw.rect(screen, (255,0,0), rect2, 2)

    screen.blit(text3, rect3)
    pg.draw.rect(screen, (255,0,0), rect3, 2)


    pg.display.flip()
    fpsClock.tick(fps)

pg.quit()
sys.exit()
