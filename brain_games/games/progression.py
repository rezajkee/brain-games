"""'Progression' question"""

import random


def progr_brief():
    brief = 'What number is missing in the progression?'
    return print(brief)


def progr_question():
    start = random.randint(1, 20)
    step = random.randint(5, 10)
    progress = list(range(start, 100, step))
    length = int(len(progress))
    hidden_elem = random.randint(0, length - 1)
    right_answer = str(progress[hidden_elem])
    progress[hidden_elem] = '..'
    print('Question: ' + ' '.join(map(str, progress)))
    return right_answer
