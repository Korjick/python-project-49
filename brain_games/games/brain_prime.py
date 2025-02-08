import random

QUESTION_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_number():
    return random.randint(1, 100)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_task_and_answer() -> (str, str):
    num = generate_number()
    question = f"{QUESTION_TEXT}\nQuestion: {num}"
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer
