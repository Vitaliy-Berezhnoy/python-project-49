import prompt

NUMBER_QUESTIONS = 3


def run_game(RULES_GAME, generating_question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(RULES_GAME)
    for _ in range(NUMBER_QUESTIONS):
        question, right_answer = generating_question_and_answer()
        print(f"Question: {question}")
        response_user = prompt.string('Your answer: ')
        if response_user != right_answer:
            print(f"'{response_user}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f"Congratulations, {name}!")        
