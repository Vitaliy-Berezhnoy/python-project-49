from random import randint

import prompt

import brain_games.cli


def game_even():
    name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num_questions = 3
    num_errors = 0
    while num_questions > 0:
        number = randint(1, 100)
        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print(f'Question: {number}')
        response_user = prompt.string('Your answer: ')
        if response_user == right_answer:
            print('Correct!')
            num_questions -= 1
        else:
            print(f"'{response_user}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            num_questions = 0
            num_errors = 1
    if num_errors == 0:
        print(f"Congratulations, {name}!")


def main():
    game_even()


if __name__ == '__main__':
    main()
