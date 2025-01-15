from brain_games.engine_game import run_game
from brain_games.games.calc import (
    RULES_GAME,
    generating_question_and_answer,
)


def main():
    run_game(RULES_GAME, generating_question_and_answer)


if __name__ == '__main__':
    main()
