from random import randint

MIN_GEN_RANGE = 1
MAX_GEN_RANGE = 130
RULES_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# функция проверяет является ли число простым
# если число простое -> True 
# если нет -> False
def is_prime(number):
    if number <= 1: 
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generating_question_and_answer():
    number = randint(MIN_GEN_RANGE, MAX_GEN_RANGE)
    question = str(number)
    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'
    return ((question, answer))
