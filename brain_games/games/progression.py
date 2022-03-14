"""'Progression' question"""

import random


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    start_of_progr = random.randint(1, 20)
    step_of_progr = random.randint(5, 10)
    progression = list(range(start_of_progr, 100, step_of_progr))
    length_of_progr = int(len(progression))
    hidden_elem = random.randint(0, length_of_progr - 1)
    right_answer = str(progression[hidden_elem])
    progression[hidden_elem] = '..'
    question = ' '.join(map(str, progression))
    return right_answer, question
