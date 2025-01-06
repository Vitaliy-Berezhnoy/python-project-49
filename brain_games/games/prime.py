from random import randint


# функция проверяет является ли число простым
# если число простое -> False 
# если нет -> True
def is_prime(number):
    if number <= 1: 
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


rules = '"yes" if given number is prime. Otherwise answer "no".'
questions = []
right_answer = []
for _ in range(3):
    number = randint(1, 100)
    questions.append(number)
    if is_prime(number):
        right_answer.append('yes')
    else:
        right_answer.append('no')
