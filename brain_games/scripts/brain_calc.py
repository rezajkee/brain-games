#!/usr/bin/env python


from brain_games.engine import start_the_game
from brain_games.games import calc


def main():
    """Start the game 'Brain-Calc'"""
    start_the_game(calc)


if __name__ == '__main__':
    main()
