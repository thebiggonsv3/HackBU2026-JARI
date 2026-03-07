import pygame as pg
import sys
import levels

pg.init()

fps = 60
fpsClock = pg.time.Clock()

info = pg.display.Info()
width = int(info.current_w * (2/3))
height = int(info.current_h * (2/3))

screen = pg.display.set_mode((width, height), pg.RESIZABLE)

running = True
hover = 0

while running:
    currentHeight = screen.get_height()
    currentWidth = screen.get_width()

    font = pg.font.SysFont("Arial", int(currentHeight/20))
    text1 = font.render(" START ", True, "black")
    text2 = font.render(" HELP ", True, "black")
    text3 = font.render(" QUIT ", True, "black")

    rect1 = text1.get_rect(topleft=(currentWidth // 2 - text1.get_width() // 2, ((currentHeight-200)/2) + int(currentHeight/20) * 1.8))
    rect2 = text2.get_rect(topleft=(currentWidth // 2 - text2.get_width() // 2, ((currentHeight-200)/2) + int(currentHeight/20) * 3.6))
    rect3 = text3.get_rect(topleft=(currentWidth // 2 - text3.get_width() // 2, ((currentHeight-200)/2) + int(currentHeight/20) * 5.4))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEMOTION:
            if rect1.collidepoint(event.pos):
                hover = 1
            elif rect2.collidepoint(event.pos):
                hover = 2
            elif rect3.collidepoint(event.pos):
                hover = 3
            else:
                hover = 0

        if event.type == pg.MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos):
                hover = 4
            elif rect2.collidepoint(event.pos):
                hover = 5
            elif rect3.collidepoint(event.pos):
                hover = 6

        if event.type == pg.MOUSEBUTTONUP:
            if rect1.collidepoint(event.pos):
                levels.levelMenu(fps, fpsClock, screen)

            if rect2.collidepoint(event.pos):
                pass

            if rect3.collidepoint(event.pos):
                running = False

    screen.fill((255, 0, 0))
    bg_img = pg.image.load("Assets/Menu.png")
    bg_scaled = pg.transform.scale(bg_img, (currentWidth, currentHeight))
    screen.blit(bg_scaled, (0, 0))

    if hover == 1:
        pg.draw.rect(screen, (67,67,67,67), rect1, 0, 10)
    if hover == 4:
        pg.draw.rect(screen, (45,45,45,45), rect1, 0, 10)
    pg.draw.rect(screen, (255,0,0), rect1, 2, 10)
    screen.blit(text1, rect1)

    if hover == 2:
        pg.draw.rect(screen, (67,67,67,67), rect2, 0, 10)
    if hover == 5:
        pg.draw.rect(screen, (45,45,45,45), rect2, 0, 10)
    screen.blit(text2, rect2)
    pg.draw.rect(screen, (255,0,0), rect2, 2, 10)

    if hover == 3:
        pg.draw.rect(screen, (67,67,67,67), rect3, 0, 10)
    if hover == 6:
        pg.draw.rect(screen, (45,45,45,45), rect3, 0, 10)
    screen.blit(text3, rect3)
    pg.draw.rect(screen, (255,0,0), rect3, 2, 10)

    pg.display.flip()
    fpsClock.tick(fps)

pg.quit()
sys.exit()