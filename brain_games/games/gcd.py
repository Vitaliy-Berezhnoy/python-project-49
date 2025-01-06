from random import randint


def nod(a, b):       # нахождение наибольшего общего делителя
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


rules = "Find the greatest common divisor of given numbers."
questions = []
right_answer = []
for _ in range(3):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    questions.append(f"{num1} {num2}")
    right_answer.append(str(nod(num1, num2)))
