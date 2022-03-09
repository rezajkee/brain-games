#!/usr/bin/env python


from brain_games.game_engine.engine import engine
from brain_games.games.calc import calc_question, calc_brief


def main():
    return engine(calc_question, calc_brief)


if __name__ == '__main__':
    main()
