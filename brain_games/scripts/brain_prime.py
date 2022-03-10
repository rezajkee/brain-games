#!/usr/bin/env python


from brain_games.game_engine.engine import engine
from brain_games.games.prime import prime_question, prime_brief


def main():
    return engine(prime_question, prime_brief)


if __name__ == '__main__':
    main()
