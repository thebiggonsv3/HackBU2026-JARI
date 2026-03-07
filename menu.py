import pygame as pg
import reused

screen, fpsClock, fps, width, height = reused.init()

font = pg.font.SysFont("Arial", 30)

text1 = font.render(" START ", True, "black")
text2 = font.render(" HELP ", True, "black")
text3 = font.render(" QUIT ", True, "black")

rect1 = text1.get_rect(topleft=(reused.width // 2 - text1.get_width() // 2, 250))
rect2 = text2.get_rect(topleft=(reused.width // 2 - text2.get_width() // 2, 300))
rect3 = text3.get_rect(topleft=(reused.width // 2 - text3.get_width() // 2, 350))

# Background color
bg = (255, 255, 255)
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
                msg = "HELP Button was pressed"

            if rect3.collidepoint(event.pos):
                msg = "QUIT Button was pressed"

    reused.screen.fill(bg)

    reused.screen.blit(text1, rect1)
    pg.draw.rect(reused.screen, (255,0,0), rect1, 2)

    reused.screen.blit(text2, rect2)
    pg.draw.rect(reused.screen, (255,0,0), rect2, 2)

    reused.screen.blit(text3, rect3)
    pg.draw.rect(reused.screen, (255,0,0), rect3, 2)

    img = font.render(msg, True, (0,0,255))
    imgrect = img.get_rect(center=(reused.width//2, reused.height//2))
    reused.screen.blit(img, imgrect)

    pg.display.flip()
    reused.fpsClock.tick(reused.fps)

pg.quit()
sys.exit()