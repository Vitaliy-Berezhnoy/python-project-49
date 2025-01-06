from random import randint


def nod(num1, num2):       # нахождение наибольшего общего делителя
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return (num1 + num2)


rules = "Find the greatest common divisor of given numbers."
questions = []
right_answer = []
for _ in range(3):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    questions.append(f"{num1} {num2}")
    right_answer.append(str(nod(num1, num2)))
