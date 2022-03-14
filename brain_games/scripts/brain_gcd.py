#!/usr/bin/env python


from brain_games.engine import start_the_game
from brain_games.games.gcd import get_question_and_answer, DESCRIPTION


def main():
    return start_the_game(get_question_and_answer, DESCRIPTION)


if __name__ == '__main__':
    main()
