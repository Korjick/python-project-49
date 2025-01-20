import random

import prompt

from brain_games.cli import welcome_user


def game(player_name: str):
    for i in range(3):
        print('Answer "yes" if the number is even, otherwise answer "no".')
        num = random.randint(1, 100)
        is_mod = num % 2 == 0
        print(f'Question: {num}')
        ans = prompt.string('Your answer: ')
        if (is_mod and ans == 'yes') or (not is_mod and ans == 'no'):
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(.",
                  f"Correct answer was '{'yes' if is_mod else 'no'}'.")
            print(f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')


def main():
    user_name = welcome_user()
    game(user_name)


if __name__ == '__main__':
    main()
