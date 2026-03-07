import pygame as pg
import sys

pg.init()

fps = 60
fpsClock = pg.time.Clock()
info = pg.display.Info()
width = int(info.current_w * (2/3))
height = int(info.current_h * (2/3))
screen = pg.display.set_mode((width, height), pg.RESIZABLE) 

font = pg.font.SysFont("Arial", 30)

text1 = font.render(" START ", True, "white")
text2 = font.render(" PLAY ", True, "white")
text3 = font.render(" HELP ", True, "white")

rect1 = text1.get_rect(topleft=(width // 2 - text1.get_width() // 2, 250))
rect2 = text2.get_rect(topleft=(width // 2 - text2.get_width() // 2, 300))
rect3 = text3.get_rect(topleft=(width // 2 - text3.get_width() // 2, 350))

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
                msg = "HELP Button was pressed"

    screen.fill(bg)

    screen.blit(text1, rect1)
    pg.draw.rect(screen, (255,0,0), rect1, 2)

    screen.blit(text2, rect2)
    pg.draw.rect(screen, (255,0,0), rect2, 2)

    screen.blit(text3, rect3)
    pg.draw.rect(screen, (255,0,0), rect3, 2)

    img = font.render(msg, True, (0,0,255))
    imgrect = img.get_rect(center=(width//2, height//2))
    screen.blit(img, imgrect)

    pg.display.flip()
    fpsClock.tick(fps)

pg.quit()
sys.exit()