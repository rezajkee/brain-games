"""'Calc' question"""

import random


def calc_brief():
    return print('What is the result of the expression?')


def calc_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    sum, dif, mult = '+', '-', '*'
    list_of_operations = [sum, dif, mult]
    operation = random.choice(list_of_operations)

    print(f'Question: {a} {operation} {b}')
    right_answer = str(eval(str(a) + operation + str(b)))
    return right_answer
