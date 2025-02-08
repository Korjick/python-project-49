import random

QUESTION_TEXT = "Find the greatest common divisor of given numbers."


def generate_numbers():
    return random.randint(1, 100), random.randint(1, 100)


def gcd_euclid(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def get_task_and_answer() -> (str, str):
    num1, num2 = generate_numbers()
    question = f"{QUESTION_TEXT}\nQuestion: {num1} {num2}"
    correct_answer = str(gcd_euclid(num1, num2))
    return question, correct_answer
