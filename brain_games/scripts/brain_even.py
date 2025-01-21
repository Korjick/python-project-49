import random

from brain_games.cli import welcome_user
from brain_games.scripts.utility import game


def get_task_and_answer() -> (str, str):
    num = random.randint(1, 100)
    is_mod = num % 2 == 0
    return (f'Answer "yes" if the number is even, otherwise answer "no".\n'
            f'Question: {num}',
            'yes' if is_mod else 'no')


def main():
    user_name = welcome_user()
    game(play_count=3,
         player_name=user_name,
         task_and_correct_ans_fun=get_task_and_answer)


if __name__ == '__main__':
    main()
