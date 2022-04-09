#!/usr/bin/env python


from brain_games.engine import start_the_game
from brain_games.games import progression


def main():
    """Start the game 'Brain-Progression'"""
    start_the_game(progression)


if __name__ == '__main__':
    main()
