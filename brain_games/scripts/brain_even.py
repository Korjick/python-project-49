import random

from brain_games.cli import welcome_user
from brain_games.scripts.utility import ask_and_answer


def game(player_name: str):
    for i in range(3):
        num = random.randint(1, 100)
        is_mod = num % 2 == 0
        res = ask_and_answer(
            player_name=player_name,
            task=f'Answer "yes" if the number is even, otherwise answer "no".\nQuestion: {num}',
            correct_ans='yes' if is_mod else 'no',
        )
        if not res:
            return
    print(f'Congratulations, {player_name}!')


def main():
    user_name = welcome_user()
    game(user_name)


if __name__ == '__main__':
    main()
