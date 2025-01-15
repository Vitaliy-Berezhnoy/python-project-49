from random import randint

MIN_GEN_RANGE = 1
MAX_GEN_RANGE = 100
RULES_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def generating_question_and_answer():
    number = randint(MIN_GEN_RANGE, MAX_GEN_RANGE)
    question = str(number)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return ((question, answer))
