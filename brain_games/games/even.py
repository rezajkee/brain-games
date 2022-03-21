"""'Is even' question"""

import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = random.randint(1, 100)
    right_answer = 'no' if question % 2 else 'yes'
    return right_answer, str(question)
