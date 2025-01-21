from typing import Callable, Tuple

import prompt


def _ask_and_answer(player_name: str, task: str, correct_ans: str) -> bool:
    print(task)
    ans = prompt.string('Your answer: ')
    if ans == correct_ans:
        print('Correct!')
        return True
    else:
        print(f"'{ans}' is wrong answer ;(.",
              f"Correct answer was '{correct_ans}'.")
        print(f"Let's try again, {player_name}!")
        return False


def game(play_count: int,
         player_name: str,
         task_and_correct_ans_fun: Callable[[], Tuple[str, str]]) -> None:
    for i in range(play_count):
        task, ans = task_and_correct_ans_fun()
        res = _ask_and_answer(
            player_name=player_name,
            task=task,
            correct_ans=ans,
        )
        if not res:
            return
    print(f'Congratulations, {player_name}!')
