from random import randint

LEN_PROGRESSION = 10
MIN_GEN_RANGE = 1
MAX_GEN_RANGE = 50
RULES_GAME = "What number is missing in the progression?"


def generating_question_and_answer():
    first_element = randint(MIN_GEN_RANGE, MAX_GEN_RANGE)
    step = randint(MIN_GEN_RANGE, MAX_GEN_RANGE)
    index_of_missing_element = randint(MIN_GEN_RANGE, LEN_PROGRESSION)
    #
    answer = str(first_element + step * (index_of_missing_element - 1))
    question = []
    for i in range(LEN_PROGRESSION):
        if i + 1 == index_of_missing_element:
            question.append('..')
        else:
            question.append(str(first_element + step * i))
    question = ' '.join(question)
    return ((question, answer))
