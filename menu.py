import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("GAME")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    #RGB Value
    screen.fill((255, 255, 255))

    pygame.display.flip()

pygame.quit()
sys.exit()
