"""'Is prime' question"""

import random


def prime_brief():
    brief = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return print(brief)


def prime_question():
    number = random.randint(1, 100)
    i = 2
    j = 0
    
    while i * i <= number and j != 1:
        if number % i == 0:
            j = 1
        i += 1
    if j == 1:
        right_answer = 'no'
    elif number == 1:
        right_answer = 'no'
    else:
        right_answer = 'yes'
    print('Question: ' + str(number))
    return right_answer
