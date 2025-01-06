from random import randint

rules = '"yes" if given number is prime. Otherwise answer "no".'
questions = []
right_answer = []
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
for _ in range(3):
    number = randint(2, 31)
    questions.append(number)
    if number in prime_numbers:
        right_answer.append('yes')
    else:
        right_answer.append('no')
