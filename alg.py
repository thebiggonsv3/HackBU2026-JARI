import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 40)

playeranswer = ""

def questions():
    exponent1 = random.randint(1,9)
    exponent2 = random.randint(1,9)
    questiontype = random.choice(["product", "quotient", "power"])
    if questiontype == "product":
        exponent3 = exponent1 + exponent2
        if exponent1 > 1 and exponent2 > 1:
            questiontext = "Solve x^" + str(exponent1) + " * x^" + str(exponent2)
        elif exponent1 == 1 and exponent2 == 1:
            questiontext = "SOlve x * x"
        elif exponent1 == 1:
            questiontext = "Solve x * x^" + str(exponent2)
        elif exponent2 == 1:
            questiontext = "Solve x^" + str(exponent1) + " * x"
        correct_answer = "x^" + str(exponent3)
    elif questiontype == "quotient":
        exponent3 = exponent1 - exponent2
        if exponent1 > 1 and exponent2 > 1:
            questiontext = "Solve x^" + str(exponent1) + " / x^" + str(exponent2)
            correct_answer = "x^" + str(exponent3)
        elif exponent1 == 1:
            questiontext = "Solve x / x^" + str(exponent2)
            correct_answer = "x^" + str(exponent3)
        elif exponent2 == 1:
            questiontext = "Solve x^" + str(exponent1) + " / x"
            correct_answer = "x^" + str(exponent3)
        else:
            questiontext = "Solve x / x"
        if exponent1 == exponent2:
            correct_answer = "1"
    elif questiontype == "power":
        exponent1 = random.randint(2,10)
        exponent2 = random.randint(2,10)
        exponent3 = exponent1 * exponent2
        questiontext = "Solve (x^" + str(exponent1) + ")^" + str(exponent2)
        correct_answer = "x^" + str(exponent3)

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
                
                if event.key == pygame.K_MINUS:
                    playeranswer += "-"

            
    screen.fill("black")
    text_image = font.render(questiontext, True, "white")
    screen.blit(text_image,(600,250))
    
    questiontitle = "Question:"
    questiontitle_image = font.render(questiontitle, True, "White")
    screen.blit(questiontitle_image,(600,180))

    answer_image = font.render(playeranswer, True, "Blue")
    screen.blit(answer_image,(630, 300))
    pygame.display.flip()