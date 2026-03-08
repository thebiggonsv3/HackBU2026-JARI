import pygame as pg
import sys
import game

def levelMenu(fps, fpsClock, screen):

    running = True
    hover = 0
    bg_img = pg.image.load("Assets/Menu.png")

    while running:
        currentHeight = screen.get_height()
        currentWidth = screen.get_width()

        font = pg.font.Font("Assets/Eight-Bit Madness.ttf", int(currentHeight/20))
        text1 = font.render(" Easy ", True, "white")
        text2 = font.render(" Medium ", True, "white")
        text3 = font.render(" Hard ", True, "white")
        text4 = font.render(" Return to Menu ", True, "white")

        rect1 = text1.get_rect(topleft=(currentWidth // 2 - text1.get_width() // 2, ((currentHeight-200)/2) + int(currentHeight/20) * 1.8))
        rect2 = text2.get_rect(topleft=(currentWidth // 2 - text2.get_width() // 2, ((currentHeight-200)/2) + int(currentHeight/20) * 3.6))
        rect3 = text3.get_rect(topleft=(currentWidth // 2 - text3.get_width() // 2, ((currentHeight-200)/2) + int(currentHeight/20) * 5.4))
        rect4 = text4.get_rect(topleft=(currentWidth // 2 - text4.get_width() // 2, ((currentHeight-200)/2) + int(currentHeight/20) * 7.2))

        padding = 30
        box_left = min(rect1.left, rect2.left, rect3.left, rect4.left) - padding
        box_top = rect1.top - padding
        box_right = max(rect1.right, rect2.right, rect3.right, rect4.right) + padding
        box_bottom = rect4.bottom + padding

        menu_rect = pg.Rect(box_left, box_top, box_right-box_left, box_bottom-box_top)

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
                elif rect4.collidepoint(event.pos):
                    hover = 7
                else:
                    hover = 0

            if event.type == pg.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    hover = 4
                elif rect2.collidepoint(event.pos):
                    hover = 5
                elif rect3.collidepoint(event.pos):
                    hover = 6
                elif rect4.collidepoint(event.pos):
                    hover = 8

            if event.type == pg.MOUSEBUTTONUP:

                if rect1.collidepoint(event.pos):
                    # Easy: 1 enemy, a few obstacles, finish in corner
                    data = [
                        game.Character(5, 5),
                        game.Enemy(9, 9),
                        game.Obstacle(3, 3),
                        game.Obstacle(6, 4),
                        game.Obstacle(4, 7),
                        game.Finish(9, 0),
                    ]
                    game.gameLoop(screen, fps, fpsClock, data)
                    running = False

                elif rect2.collidepoint(event.pos):
                    # Medium: 2 enemies, more obstacles, finish in corner
                    data = [
                        game.Character(5, 5),
                        game.Enemy(9, 9),
                        game.Enemy(0, 9),
                        game.Obstacle(3, 3),
                        game.Obstacle(6, 3),
                        game.Obstacle(3, 6),
                        game.Obstacle(6, 6),
                        game.Obstacle(5, 1),
                        game.Finish(9, 0),
                    ]
                    game.gameLoop(screen, fps, fpsClock, data)
                    running = False

                elif rect3.collidepoint(event.pos):
                    # Hard: 3 enemies, dense obstacles, finish tucked away
                    data = [
                        game.Character(5, 5),
                        game.Enemy(9, 9),
                        game.Enemy(0, 9),
                        game.Enemy(9, 0),
                        game.Obstacle(2, 2),
                        game.Obstacle(4, 2),
                        game.Obstacle(6, 2),
                        game.Obstacle(2, 5),
                        game.Obstacle(7, 5),
                        game.Obstacle(2, 7),
                        game.Obstacle(5, 7),
                        game.Obstacle(7, 7),
                        game.Finish(0, 0),
                    ]
                    game.gameLoop(screen, fps, fpsClock, data)
                    running = False

                elif rect4.collidepoint(event.pos):
                    running = False

        bg_scaled = pg.transform.scale(bg_img, (currentWidth, currentHeight))
        screen.blit(bg_scaled, (0, 0))

        panel = pg.Surface((menu_rect.width, menu_rect.height), pg.SRCALPHA)
        pg.draw.rect(panel, (0,0,0,140), (0,0,menu_rect.width,menu_rect.height), border_radius=20)
        screen.blit(panel, menu_rect.topleft)

        # Buttons
        if hover == 1: pg.draw.rect(screen,(67,67,67),rect1,0,10)
        if hover == 4: pg.draw.rect(screen,(45,45,45),rect1,0,10)
        screen.blit(text1,rect1)

        if hover == 2: pg.draw.rect(screen,(67,67,67),rect2,0,10)
        if hover == 5: pg.draw.rect(screen,(45,45,45),rect2,0,10)
        screen.blit(text2,rect2)

        if hover == 3: pg.draw.rect(screen,(67,67,67),rect3,0,10)
        if hover == 6: pg.draw.rect(screen,(45,45,45),rect3,0,10)
        screen.blit(text3,rect3)

        if hover == 7: pg.draw.rect(screen,(67,67,67),rect4,0,10)
        if hover == 8: pg.draw.rect(screen,(45,45,45),rect4,0,10)
        screen.blit(text4,rect4)

        pg.display.flip()
        fpsClock.tick(fps)