import random

def questions1():
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


def questions2():
    exponent1 = random.randint(1,9)
    exponent2 = random.randint(1,9)
    questiontype = random.choice(["product", "quotient", "power"])
    def format_power(exp):
        if exp == 1:
            return "x"
        else:
            return "x^" + str(exp)

    if questiontype == "product":
        exponent3 = exponent1 + exponent2
        questiontext = "Solve " + format_power(exponent1) + " * " + format_power(exponent2)
        correct_answer = format_power(exponent3)

    elif questiontype == "quotient":
        exponent3 = exponent1 - exponent2
        questiontext = "Solve " + format_power(exponent1) + " / " + format_power(exponent2)

        if exponent3 == 0:
            correct_answer = "1"
        else:
            correct_answer = format_power(exponent3)

    elif questiontype == "power":
        exponent1 = random.randint(2,10)
        exponent2 = random.randint(2,10)
        exponent3 = exponent1 * exponent2
        
        questiontext = "Solve (" + format_power(exponent1) + ")^" + str(exponent2)
        correct_answer = format_power(exponent3)

    return questiontext, correct_answer

def questions3():
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)
    coefficient = number1 * number2
    power = number2 - 1

    if number2 > 1 and number1 > 1:
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

