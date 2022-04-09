#!/usr/bin/env python


from brain_games.engine import start_the_game
from brain_games.games import prime


def main():
    """Start the game 'Brain-Prime'"""
    start_the_game(prime)


if __name__ == '__main__':
    main()
