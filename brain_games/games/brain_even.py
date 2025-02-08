import random

QUESTION_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_number():
    return random.randint(1, 100)


def is_even(number):
    return number % 2 == 0


def get_task_and_answer() -> (str, str):
    num = generate_number()
    question = f"{QUESTION_TEXT}\nQuestion: {num}"
    correct_answer = 'yes' if is_even(num) else 'no'
    return question, correct_answer
