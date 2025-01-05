from random import randint

rules = 'Answer "yes" if the number is even, otherwise answer "no".'
questions = []
right_answer = []
for _ in range(3):
    number = randint(1, 100)
    questions.append(number)
    if number % 2 == 0:
        right_answer.append('yes')
    else:
        right_answer.append('no')
