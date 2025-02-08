import operator
import random

QUESTION_TEXT = "What is the result of the expression?"

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}


def generate_expression():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(list(OPERATIONS.keys()))
    return num1, num2, op


def calculate_answer(num1, num2, op):
    return str(OPERATIONS[op](num1, num2))


def get_task_and_answer() -> (str, str):
    num1, num2, op = generate_expression()
    question = f"{QUESTION_TEXT}\nQuestion: {num1} {op} {num2}"
    correct_answer = calculate_answer(num1, num2, op)
    return question, correct_answer
