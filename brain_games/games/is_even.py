"""'Is even' question"""

import random


def is_even_brief():
    return print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even_question():
    number = random.randint(1, 100)
    print('Question: ' + str(number))
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
