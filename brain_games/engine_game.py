import prompt


def engine(rule: str, questions: list, right_answer: list):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rule)
    num_questions = len(questions)
    num_errors = 0
    while num_questions > 0:
        print(f"Question: {questions[num_questions - 1]}")
        response_user = prompt.string('Your answer: ')
        if response_user == right_answer[num_questions - 1]:
            print('Correct!')
            num_questions -= 1
        else:
            print(f"'{response_user}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{right_answer[num_questions - 1]}'.")
            print(f"Let's try again, {name}!")
            num_questions = 0
            num_errors = 1
    if num_errors == 0:
        print(f"Congratulations, {name}!")