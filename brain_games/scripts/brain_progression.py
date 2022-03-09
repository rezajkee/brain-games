#!/usr/bin/env python


from brain_games.game_engine.engine import engine
from brain_games.games.progression import progr_question, progr_brief


def main():
    return engine(progr_question, progr_brief)


if __name__ == '__main__':
    main()
