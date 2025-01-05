from random import choice, randint

rules = "What is the result of the expression?"
questions = []
right_answer = []
for _ in range(3):
    num1 = randint(1, 25)
    num2 = randint(1, 25)
    operation = choice('+-*')
    questions.append(f"{str(num1)} {operation} {str(num2)}")
    match operation:
        case "+":
            right_answer.append(str(num1 + num2))
        case "-":
            right_answer.append(str(num1 - num2))
        case "*":
            right_answer.append(str(num1 * num2))
