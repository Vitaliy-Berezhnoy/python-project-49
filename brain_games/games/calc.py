from random import choice, randint

MIN_GEN_RANGE = 1
MAX_GEN_RANGE = 25
OPERATIONS = ('+', '-', '*')
RULES_GAME = "What is the result of the expression?"


def generating_question_and_answer(): 
    num1 = randint(MIN_GEN_RANGE, MAX_GEN_RANGE)
    num2 = randint(MIN_GEN_RANGE, MAX_GEN_RANGE)
    operation = choice(OPERATIONS)
    question = f"{str(num1)} {operation} {str(num2)}"
    match operation:
        case "+":
            answer = str(num1 + num2)
        case "-":
            answer = str(num1 - num2)
        case "*":
            answer = str(num1 * num2)
    return ((question, answer))
