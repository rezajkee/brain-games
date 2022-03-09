"""Games engine"""


import prompt


def engine(game, brief):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    win_streak = 0
    brief()
    while win_streak < 3:
        right_answer = game()
        user_answer = prompt.string('Your answer: ')
        if right_answer == user_answer:
            print('Correct!')
            win_streak += 1
        else:
            part_one = f"'{user_answer}' is wrong answer ;(. "
            part_two = f"Correct answer was '{right_answer}'."
            print(part_one + part_two)
            print(f"Let's try again, {name}!")
            break
    if win_streak == 3:
        print(f'Congratulations, {name}!')
