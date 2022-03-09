#!/usr/bin/env python


from brain_games.game_engine.engine import engine
from brain_games.games.gcd import gcd_question, gcd_brief


def main():
    return engine(gcd_question, gcd_brief)


if __name__ == '__main__':
    main()
