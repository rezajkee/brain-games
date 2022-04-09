#!/usr/bin/env python


from brain_games.engine import start_the_game
from brain_games.games import gcd


def main():
    """Start the game 'Brain-Gcd'"""
    start_the_game(gcd)


if __name__ == '__main__':
    main()
