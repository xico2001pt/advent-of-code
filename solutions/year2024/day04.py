from solutions.solution_base import SolutionBase
import re


def get_horizontal_lines(values: list[str]) -> list[str]:
    return values


def get_vertical_lines(values: list[str]) -> list[str]:
    num_rows = len(values)
    num_columns = len(values[0])

    return [
        "".join([values[j][i] for j in range(num_rows)]) for i in range(num_columns)
    ]


def get_down_diagonals(values: list[str]) -> list[str]:
    num_rows = len(values)
    num_columns = len(values[0])
    diagonals = []

    for col in range(num_columns):
        diagonal = []
        i, j = 0, col
        while i < num_rows and j < num_columns:
            diagonal.append(values[i][j])
            i += 1
            j += 1
        diagonals.append("".join(diagonal))

    for row in range(1, num_rows):
        diagonal = []
        i, j = row, 0
        while i < num_rows and j < num_columns:
            diagonal.append(values[i][j])
            i += 1
            j += 1
        diagonals.append("".join(diagonal))

    return diagonals


def get_up_diagonals(values: list[str]) -> list[str]:
    num_rows = len(values)
    num_columns = len(values[0])
    diagonals = []

    for row in range(num_rows):
        diagonal = []
        i, j = row, 0
        while i >= 0 and j < num_columns:
            diagonal.append(values[i][j])
            i -= 1
            j += 1
        diagonals.append("".join(diagonal))

    for col in range(1, num_columns):
        diagonal = []
        i, j = num_rows - 1, col
        while i >= 0 and j < num_columns:
            diagonal.append(values[i][j])
            i -= 1
            j += 1
        diagonals.append("".join(diagonal))

    return diagonals


def count_word_occurrences(word: str, search_space: str):
    return len(re.findall(word, search_space))


def count_word_occurrences_in_list(word: str, search_spaces: list[str]):
    return sum(
        [count_word_occurrences(word, search_space) for search_space in search_spaces]
    )


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


def get_main_diagonals(values: list[str]) -> tuple[list[str]]:
    num_rows = len(values)
    num_columns = len(values[0])
    return (
        [values[i][i] for i in range(min(num_columns, num_rows))],  # Main diagonal
        [
            values[i][num_columns - 1 - i] for i in range(min(num_columns, num_rows))
        ],  # Secondary diagonal
    )


def validate_mas(diagonals: tuple[list[str]], word: str) -> bool:
    word1, word2 = "".join(diagonals[0]), "".join(diagonals[1])
    inv_word = word[::-1]
    return (word1 == word or word1 == inv_word) and (word2 == word or word2 == inv_word)


class Day04(SolutionBase):
    def load_input(self, input: str):
        self.values = input.split("\n")

    def part1(self):
        word = "XMAS"
        search_spaces = (
            get_horizontal_lines(self.values)
            + get_vertical_lines(self.values)
            + get_up_diagonals(self.values)
            + get_down_diagonals(self.values)
        )
        return count_word_occurrences_in_list(
            word, search_spaces
        ) + count_word_occurrences_in_list(word[::-1], search_spaces)

    def part2(self):
        word = "MAS"
        all_x = get_overlapping_blocks(self.values, (3, 3))
        return sum([validate_mas(get_main_diagonals(x_box), word) for x_box in all_x])

    def get_main_diagonals(self, values: list[str]) -> tuple[list[str]]:
        num_rows = len(values)
        num_columns = len(values[0])
        return (
            [values[i][i] for i in range(min(num_columns, num_rows))],  # Main diagonal
            [
                values[i][num_columns - 1 - i]
                for i in range(min(num_columns, num_rows))
            ],  # Secondary diagonal
        )

    def validate_mas(self, diagonals: tuple[list[str]], word: str) -> bool:
        word1, word2 = "".join(diagonals[0]), "".join(diagonals[1])
        inv_word = word[::-1]
        return (word1 == word or word1 == inv_word) and (
            word2 == word or word2 == inv_word
        )
