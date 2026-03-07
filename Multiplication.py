import pygame

pygame.init()
import random
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 50)

playeranswer = ""

def questions():
    number1 = random.randint(1,20)
    number2 = random.randint(1,20)

    questiontext = str(number1) + " * " + str(number2) + " = ?"

    correct_answer = number1 * number2
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
                        playeranswer += str(numbers)

            
    screen.fill("black")
    text_image = font.render(questiontext, True, "white")
    screen.blit(text_image,(300,250))

    answer_image = font.render(playeranswer, True, "Blue")
    screen.blit(answer_image,(350, 400))
    pygame.display.flip()