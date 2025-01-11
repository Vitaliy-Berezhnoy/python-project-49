from random import randint


# функция создает арифметическую прогрессию
def generating_a_progression(first: int, step: int, empty: int) -> str:
    question = ''
    for i in range(1, 11):
        if i == empty:
            question += '.. '
        else:
            question += str(first + step * (i - 1)) + ' '
    question = question.strip()
    return (question)


def displays_rules_game():
    print("What number is missing in the progression?")


def generating_question_and_answer():
    LEN_PROGRESSION = 10
    MIN_GEN_RANGE = 1
    MAX_GEN_RANGE = 50
    #
    first_element = randint(MIN_GEN_RANGE, MAX_GEN_RANGE)
    step = randint(MIN_GEN_RANGE, MAX_GEN_RANGE)
    index_of_missing_element = randint(MIN_GEN_RANGE, LEN_PROGRESSION)
    #
    answer = str(first_element + step * (index_of_missing_element - 1))
    question = ''
    for i in range(LEN_PROGRESSION):
        if i + 1 == index_of_missing_element:
            question += '.. '
        else:
            question += str(first_element + step * i) + ' '
    question = question.strip()
    return ((question, answer))
