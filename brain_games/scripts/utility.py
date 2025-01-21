import prompt


def ask_and_answer(player_name: str, task: str, correct_ans: str) -> bool:
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