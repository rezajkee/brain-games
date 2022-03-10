"""'Calc' question"""

import random


def calc_brief():
    brief = 'What is the result of the expression?'
    return print(brief)


def calc_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    list_of_operations = ['+', '-', '*']
    operation = random.choice(list_of_operations)

    print(f'Question: {a} {operation} {b}')
    if operation == '+':
        right_answer = str(a + b)
    elif operation == '-':
        right_answer = str(a - b)
    else:
        right_answer = str(a * b)
    return right_answer
