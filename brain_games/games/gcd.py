"""'QCD' question"""

import random
from math import gcd


def gcd_brief():
    return print('Find the greatest common divisor of given numbers.')


def gcd_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    print(f'Question: {a} {b}')
    right_answer = str(gcd(a, b))
    return right_answer
