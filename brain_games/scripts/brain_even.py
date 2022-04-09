#!/usr/bin/env python


from brain_games.engine import start_the_game
from brain_games.games import even


def main():
    """Start the game 'Brain-Even'"""
    start_the_game(even)


if __name__ == '__main__':
    main()
