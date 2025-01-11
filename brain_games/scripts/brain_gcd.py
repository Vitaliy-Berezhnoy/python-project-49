from brain_games.engine_game import run_game
from brain_games.games.gcd import (
    displays_rules_game,
    generating_question_and_answer,
)


def main():
    run_game(displays_rules_game, generating_question_and_answer)


if __name__ == '__main__':
    main()
