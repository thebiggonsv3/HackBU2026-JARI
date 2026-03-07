import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 40)

playeranswer = ""

def questions():
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)
    coefficient = number1 * number2
    power = number2 - 1

    if number2 and number1 > 1:
        questiontext = "Derive " + str(number1) + "x^" + str(number2)
    elif number2 == 1 and number1 > 1:
        questiontext = "Derive " + str(number1) + "x"
    elif number1 == 1 and number2 > 1:
        questiontext = "Derive x^" + str(number2)
    else:
        questiontext = "Derive x"
    
    if power > 1:
        correct_answer = str(coefficient) + "x^" + str(power)
    elif power == 1:
        correct_answer = str(coefficient) + "x"
    else:
        correct_answer = str(coefficient)

    return questiontext, correct_answer

questiontext, correct_answer = questions()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if playeranswer == str(correct_answer):
                    questiontext, correct_answer = questions()
                playeranswer = ""
            elif event.key == pygame.K_BACKSPACE:
                playeranswer = playeranswer [:-1]
            else:
                for numbers in range (10):
                    if event.key == pygame.K_0 + numbers:
                        if numbers == 6 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            pass
                        else:
                            playeranswer += str(numbers)
                
                if event.key == pygame.K_x:
                    playeranswer += "x"
                
                if event.key == pygame.K_6 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    playeranswer += "^"

            
    screen.fill("black")
    text_image = font.render(questiontext, True, "white")
    screen.blit(text_image,(600,250))
    
    questiontitle = "Question:"
    questiontitle_image = font.render(questiontitle, True, "White")
    screen.blit(questiontitle_image,(600,180))

    answer_image = font.render(playeranswer, True, "Blue")
    screen.blit(answer_image,(630, 300))
    pygame.display.flip()