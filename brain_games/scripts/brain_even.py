#!/usr/bin/env python

from random import randint
import prompt


def is_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    win_streak = 0

    while win_streak < 3:
        number = randint(1, 100)
        print('Question: ' + str(number))
        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        user_answer = prompt.string('Your answer: ')
        if right_answer == user_answer:
            print('Correct!')
            win_streak += 1
        else:
            print('\'' + user_answer + '\' is wrong answer ;(. Correct answer was \'' + right_answer + '\'.\nLet\'s try again, ' + name + '!')
            break
    if win_streak == 3:
        print('Congratulations, ' + name + '!')


def main():
    is_even()


if __name__ == '__main__':
    main()
