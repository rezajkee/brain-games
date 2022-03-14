"""'QCD' question"""

import random
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    right_answer = str(gcd(first_number, second_number))
    question = f'{first_number} {second_number}'
    return right_answer, question
