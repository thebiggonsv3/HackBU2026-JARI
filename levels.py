import pygame as pg
import sys

def levelMenu(fps, fpsClock, screen):
    font = pg.font.SysFont("Arial", 30)

    text1 = font.render(" EASY ", True, "white")
    text2 = font.render(" MEDIUM ", True, "white")
    text3 = font.render(" HARD ", True, "white")

    bg = (127, 127, 127)
    msg = ""
    running = True
    while running:
        currentHeight = screen.get_height()
        currentWidth = screen.get_width()
        rect1 = text1.get_rect(center=(((currentWidth // 2)-text2.get_width()), (currentHeight-50)/2 ))
        rect2 = text2.get_rect(center=((currentWidth // 2), (currentHeight-50)/2))
        rect3 = text3.get_rect(center=(((currentWidth // 2)+text2.get_width()), (currentHeight-50)/2))
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
        pg.draw.rect(screen, (0,255,0), rect1, 2)

        screen.blit(text2, rect2)
        pg.draw.rect(screen, (255,255,0), rect2, 2)

        screen.blit(text3, rect3)
        pg.draw.rect(screen, (255,0,0), rect3, 2)

        img = font.render(msg, True, (0,0,255))
        imgrect = img.get_rect(center=(currentWidth//2, currentHeight//2))
        screen.blit(img, imgrect)

        pg.display.flip()
        fpsClock.tick(fps)

    pg.quit()
    sys.exit()
