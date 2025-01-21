import random

from brain_games.cli import welcome_user
from brain_games.scripts.utility import game


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_task_and_answer() -> (str, str):
    num = random.randint(1, 100)
    is_prime = _is_prime(num)
    return (f'Answer "yes" if given number is prime. Otherwise answer "no".\n'
            f'Question: {num}',
            'yes' if is_prime else 'no')


def main():
    user_name = welcome_user()
    game(play_count=3,
         player_name=user_name,
         task_and_correct_ans_fun=get_task_and_answer)


if __name__ == '__main__':
    main()
