import random

from brain_games.cli import welcome_user
from brain_games.scripts.utility import game


def get_task_and_answer() -> (str, str):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(['+', '-', '*'])
    match op:
        case '+':
            res = num1 + num2
        case '-':
            res = num1 - num2
        case '*':
            res = num1 * num2
    return (f'What is the result of the expression?\n'
            f'Question: {num1} {op} {num2}',
            str(res))


def main():
    user_name = welcome_user()
    game(play_count=3,
         player_name=user_name,
         task_and_correct_ans_fun=get_task_and_answer)


if __name__ == '__main__':
    main()
