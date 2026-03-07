import pygame as pg
import sys

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("GAME")

font = pg.font.SysFont("Arial", 14)

text1 = font.render(" START ", True, "white")
text2 = font.render(" PLAY ", True, "white")
text3 = font.render(" STOP ", True, "white")

rect1 = text1.get_rect(topleft=(10, 10))
rect2 = text2.get_rect(topleft=(100, 10))
rect3 = text3.get_rect(topleft=(200, 10))

bg = (127, 127, 127)
msg = ""

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos):
                msg = "START Button was pressed"

            if rect2.collidepoint(event.pos):
                msg = "PLAY Button was pressed"

            if rect3.collidepoint(event.pos):
                msg = "STOP Button was pressed"

    screen.fill(bg)

    screen.blit(text1, rect1)
    pg.draw.rect(screen, (255,0,0), rect1, 2)

    screen.blit(text2, rect2)
    pg.draw.rect(screen, (255,0,0), rect2, 2)

    screen.blit(text3, rect3)
    pg.draw.rect(screen, (255,0,0), rect3, 2)

    img = font.render(msg, True, (0,0,255))
    imgrect = img.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    screen.blit(img, imgrect)

    pg.display.update()

pg.quit()
sys.exit()