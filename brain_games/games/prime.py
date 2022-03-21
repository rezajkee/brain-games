"""'Is prime' question"""

import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    check_index1 = 2
    check_index2 = 0

    while check_index1 * check_index1 <= question and check_index2 != 1:
        if question % check_index1 == 0:
            check_index2 = 1
        check_index1 += 1
    if check_index2 == 1:
        return False
    elif question == 1:
        return False
    else:
        return True


def get_question_and_answer():
    question = random.randint(1, 100)
    right_answer = 'yes' if is_prime(question) else 'no'
    return right_answer, str(question)
