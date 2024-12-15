import os

INPUTS_FOLDER_NAME = "input"


INPUT_FOLDER_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), INPUTS_FOLDER_NAME
)


def print_title(day: int):
    print(f"Day {day} Solutions:")


def print_solutions(solutions: list[str]):
    for i, s in enumerate(solutions):
        print(f"    - Part {i+1}: {s}")


def print_matrix(matrix: list[list]):
    for row in matrix:
        print(row)
    print("")


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


def get_overlapping_blocks(
    values: list[list], block_size: tuple[int, int]
) -> list[list[list]]:
    num_rows = len(values)
    num_cols = len(values[0])
    block_height, block_width = block_size

    blocks = []
    for row in range(num_rows - block_height + 1):
        for col in range(num_cols - block_width + 1):
            block = [
                values[r][col : col + block_width]
                for r in range(row, row + block_height)
            ]
            blocks.append(block)

    return blocks


def find_occurrences_matrix(
    search_space: list[list[str]], target: str
) -> set[tuple[int, int]]:
    result = set()
    for i, row in enumerate(search_space):
        for j, v in enumerate(row):
            if v == target:
                result.add((i, j))
    return result
