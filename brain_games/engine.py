"""Games engine"""


import prompt


def start_the_game(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    points_to_win = 3
    points_streak = 0
    print(game.DESCRIPTION)
    while points_streak < points_to_win:
        right_answer, question = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if right_answer == user_answer:
            print('Correct!')
            points_streak += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{right_answer}'.")
            print(f"Let's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')
