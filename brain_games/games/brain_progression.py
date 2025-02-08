import random

QUESTION_TEXT = "What number is missing in the progression?"


def generate_progression():
    length = random.randint(5, 12)
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    return [start + i * step for i in range(length)]


def hide_element(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = ".."
    return hidden_value


def get_task_and_answer() -> (str, str):
    progression = generate_progression()
    correct_answer = str(hide_element(progression))
    question = (f"{QUESTION_TEXT}\n"
                f"Question: {' '.join(str(el) for el in progression)}")
    return question, correct_answer
