"""'Is prime' question"""

import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    if question == 1:
        return False
    if question % 2 == 0:
        return question == 2
    check_index = 3
    while check_index * check_index <= question and question % check_index != 0:
        check_index += 2
    return check_index * check_index > question


def get_question_and_answer():
    question = random.randint(1, 100)
    right_answer = 'yes' if is_prime(question) else 'no'
    return right_answer, str(question)
