import random

from brain_games.cli import welcome_user
from brain_games.scripts.utility import ask_and_answer


def game(player_name: str):
    for i in range(3):
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

        res = ask_and_answer(
            player_name=player_name,
            task=f'What is the result of the expression?\nQuestion: {num1} {op} {num2}',
            correct_ans=str(res),
        )
        if not res:
            return
    print(f'Congratulations, {player_name}!')


def main():
    user_name = welcome_user()
    game(user_name)


if __name__ == '__main__':
    main()
