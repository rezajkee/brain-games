"""'Calc' question"""

import random
import operator


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    operand1 = random.randint(1, 10)
    operand2 = random.randint(1, 10)
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    operation = random.choice(list(operations.keys()))

    right_answer = str(operations[operation](operand1, operand2))
    question = f'{operand1} {operation} {operand2}'
    return right_answer, question
