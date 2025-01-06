from random import randint


def progress(first, step, empty):    # создает арифметическую прогрессию
    temp = ''
    for i in range(1, 11):
        if i == empty:
            temp += '.. '
        else:
            temp += str(first + step * (i - 1)) + ' '
    temp = temp.strip()
    return (temp)


rules = "What number is missing in the progression?"
questions = []
right_answer = []
for _ in range(3):
    first = randint(2, 50)
    step = randint(2, 20)
    empty = randint(1, 10)
    right_answer.append(str(first + step * (empty - 1)))
    questions.append(progress(first, step, empty))    
