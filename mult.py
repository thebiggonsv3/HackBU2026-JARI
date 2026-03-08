import pygame

pygame.init()
import random
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont(None, 45)
font2 = pygame.font.SysFont(None, 30)
congrats = "Congratulations!"
congrats_image = font2.render(congrats, True, "White")
  
correct_message = ""
makeamove = "You may make a move"
makeamove_image = font2.render(makeamove, True, "White")
  

wronganswer = "Incorrect Answer!"
wronganswer_image = font2.render(wronganswer, True, "White")

loseturn = "You Lose Your Turn!"
loseturn_image = font2.render(loseturn, True, "White")
playeranswer = ""


def questions():
    number1 = random.randint(1,15)
    number2 = random.randint(1,15)

    symbols = [ '+', '-', '*']
    randomymbol = random.choice(symbols)

    if randomymbol == '+':
        correct_answer = number1 + number2
    elif randomymbol == '-':
        correct_answer = number1 - number2
    elif randomymbol == '*':
        correct_answer = number1 * number2

    questiontext = str(number1) + " " + randomymbol + " " + str(number2) + " = ?"

    return questiontext, correct_answer
questiontext, correct_answer = questions()

while True:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if playeranswer == str(correct_answer):
                    questiontext, correct_answer = questions()
                    correct_message = 1
                else:
                    correct_message = 2
                playeranswer = ""
            
            elif event.key == pygame.K_BACKSPACE:
                playeranswer = playeranswer [:-1]
            elif event.key == pygame.K_MINUS:
                playeranswer += "-"
            else:
                for numbers in range (10):
                    if event.key == pygame.K_0 + numbers:
                        playeranswer += str(numbers)
            
    text_image = font.render(questiontext, True, "white")
    screen.blit(text_image,(600,250))
    
    questiontitle = "Question:"
    questiontitle_image = font.render(questiontitle, True, "White")
    screen.blit(questiontitle_image,(600,180))

    answer_image = font.render(playeranswer, True, "Blue")
    screen.blit(answer_image,(630, 300))

    if correct_message == 1:
        screen.blit(congrats_image,(500,380))
        screen.blit(makeamove_image,(500,480))
    if correct_message == 2:
        screen.blit(wronganswer_image,(500,380))
        screen.blit(loseturn_image,(500,430))
    
    pygame.display.flip()
