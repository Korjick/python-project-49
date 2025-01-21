import random

from brain_games.cli import welcome_user
from brain_games.scripts.utility import game


def get_task_and_answer() -> (str, str):
    length = random.randint(5, 12)

    start = random.randint(1, 10)
    step = random.randint(1, 10)

    progression = [start + i * step for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]

    progression[hidden_index] = ".."
    return (f'What number is missing in the progression?\n'
            f'Question: {" ".join(str(el) for el in progression)}',
            str(hidden_value))


def main():
    user_name = welcome_user()
    game(play_count=3,
         player_name=user_name,
         task_and_correct_ans_fun=get_task_and_answer)


if __name__ == '__main__':
    main()
