import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 40)
progress1 = 0
Level1 = 1
while True:
    screen.fill("black")
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if progress1 < 20:
                progress1 += 1
            if progress1 == 20:
                progress1 = 0
                Level1 += 1


    level_progress = f"Level: {Level1}/20"
    level_progress_image = font.render(level_progress, True, "White")
    screen.blit(level_progress_image, (300, 400))

    scoreboard_progress = f"Progress: {progress1}/20"
    scoreboard_progress_image = font.render(scoreboard_progress, True, "White")
    screen.blit(scoreboard_progress_image, (300, 300))
    pygame.display.flip()
