import os

INPUTS_FOLDER_NAME = "input"


INPUT_FOLDER_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    INPUTS_FOLDER_NAME
)


def print_title(day: int):
    print(f'Day {day} Solutions:')


def print_solutions(solutions: list[str]):
    for i, s in enumerate(solutions):
        print(f'    - Part {i+1}: {s}')


def read_file(filename: str):
    return open(os.path.join(INPUT_FOLDER_PATH, filename)).read()


def count_frequency(input: list) -> dict:
    freq_dict = {}
    for item in input:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    return freq_dict
