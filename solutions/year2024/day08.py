from solutions.solution_base import SolutionBase


EMPTY = "."


def is_outside_map(pos: tuple[int, int], y_max: int, x_max: int) -> bool:
    y, x = pos
    return y < 0 or x < 0 or y >= y_max or x >= x_max


def group_antennas(map: list[list[str]]) -> dict[str, list]:
    antennas = dict()
    for i, row in enumerate(map):
        for j, value in enumerate(row):
            if value is not EMPTY:
                if value not in antennas:
                    antennas[value] = list()
                antennas[value].append((i, j))
    return antennas


def generate_unique_pairs(elements: list) -> list[tuple]:
    size = len(elements)

    result = []
    for i in range(size):
        for j in range(i + 1, size):
            result.append((elements[i], elements[j]))
    return result


def calculate_antinode_positions(
    pair: tuple[tuple[int, int], tuple[int, int]],
    anyDistance: bool,
    y_max: int,
    x_max: int,
) -> list[tuple[int, int]]:
    p1, p2 = pair
    di, dj = p2[0] - p1[0], p2[1] - p1[1]

    if not anyDistance:
        return ((p1[0] - di, p1[1] - dj), (p1[0] + 2 * di, p1[1] + 2 * dj))

    positions = []

    pi, pj = p1[0], p1[1]
    while True:
        if pi < 0 or pj < 0:
            break
        positions.append((pi, pj))
        pi -= di
        pj -= dj

    pi, pj = p1[0], p1[1]
    while True:
        if pi >= y_max or pj >= x_max:
            break
        positions.append((pi, pj))
        pi += di
        pj += dj

    return positions


def generate_antinodes_map(
    map: list[list[str]], anyDistance: bool = False
) -> list[list[int]]:
    NUM_ROWS = len(map)
    NUM_COLUMNS = len(map[0])

    antinodes_map = [[0 for _ in range(NUM_COLUMNS)] for _ in range(NUM_ROWS)]

    antennas = group_antennas(map)
    for positions in antennas.values():
        pairs = generate_unique_pairs(positions)
        for pair in pairs:
            antinodes = calculate_antinode_positions(
                pair, anyDistance, NUM_ROWS, NUM_COLUMNS
            )
            for i, j in antinodes:
                if not is_outside_map((i, j), NUM_ROWS, NUM_COLUMNS):
                    antinodes_map[i][j] = 1

    return antinodes_map


class Day08(SolutionBase):
    def load_input(self, input: str):
        self.map = [[c for c in row] for row in input.split("\n")]

    def part1(self):
        return sum([sum(row) for row in generate_antinodes_map(self.map)])

    def part2(self):
        return sum([sum(row) for row in generate_antinodes_map(self.map, True)])
