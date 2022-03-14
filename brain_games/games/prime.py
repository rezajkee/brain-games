"""'Is prime' question"""

import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(1, 100)
    check_index1 = 2
    check_index2 = 0

    while check_index1 * check_index1 <= number and check_index2 != 1:
        if number % check_index1 == 0:
            check_index2 = 1
        check_index1 += 1
    if check_index2 == 1:
        right_answer = 'no'
    elif number == 1:
        right_answer = 'no'
    else:
        right_answer = 'yes'
    question = str(number)
    return right_answer, question
