import random

from brain_games.cli import welcome_user
from brain_games.scripts.utility import game


def _gcd_euclid(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def get_task_and_answer() -> (str, str):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return (f'Find the greatest common divisor of given numbers.\n'
            f'Question: {num1} {num2}',
            str(_gcd_euclid(num1, num2)))


def main():
    user_name = welcome_user()
    game(play_count=3,
         player_name=user_name,
         task_and_correct_ans_fun=get_task_and_answer)


if __name__ == '__main__':
    main()
