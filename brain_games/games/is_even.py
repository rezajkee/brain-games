"""'Is even' question"""

import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(1, 100)
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = str(number)
    return right_answer, question
