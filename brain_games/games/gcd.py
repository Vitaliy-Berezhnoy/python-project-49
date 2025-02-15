from random import randint

MIN_GEN_RANGE = 2
MAX_GEN_RANGE = 10
RULES_GAME = "Find the greatest common divisor of given numbers."


def finding_gcd(num1, num2):       # нахождение наибольшего общего делителя
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return (num1 + num2)


def generating_question_and_answer():
    num1 = randint(MIN_GEN_RANGE, MAX_GEN_RANGE)
    num2 = randint(MIN_GEN_RANGE, MAX_GEN_RANGE)
    question = f"{num1} {num2}"
    answer = str(finding_gcd(num1, num2))
    return ((question, answer))
