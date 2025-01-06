import brain_games.engine_game
from brain_games.games.progression import questions, right_answer, rules


def main():
    brain_games.engine_game.engine(rules, questions, right_answer)


if __name__ == '__main__':
    main()