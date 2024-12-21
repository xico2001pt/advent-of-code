from solutions.solution_base import SolutionBase
import copy

PLAYER = "^"
OBSTACLE = "#"
VISITED = "X"
EMPTY = "."

INITIAL_DIRECTION = (-1, 0)


def find_occurrences_matrix(
    search_space: list[list[str]], target: str
) -> set[tuple[int, int]]:
    result = set()
    for i, row in enumerate(search_space):
        for j, v in enumerate(row):
            if v == target:
                result.add((i, j))
    return result


def is_outside_map(pos: tuple[int, int], y_max: int, x_max: int) -> bool:
    y, x = pos
    return y < 0 or x < 0 or y >= y_max or x >= x_max


def rotate(dir: tuple[int, int]) -> tuple[int, int]:
    if dir == (-1, 0):
        return (0, 1)
    elif dir == (0, 1):
        return (1, 0)
    elif dir == (1, 0):
        return (0, -1)
    return (-1, 0)


class Day06(SolutionBase):
    def load_input(self, input: str):
        self.map = [[c for c in row] for row in input.split("\n")]

    def part1(self):
        map = copy.deepcopy(self.map)
        self.simulate_navigation(map)
        return len(find_occurrences_matrix(map, VISITED))

    def part2(self):
        map = copy.deepcopy(self.map)
        n_rows, n_columns = len(map), len(map[0])

        result = 0
        for i in range(n_rows):
            print(f"Progress: {i+1}/{n_rows}")
            for j in range(n_columns):
                elem = map[i][j]
                if elem == EMPTY:
                    new_map = copy.deepcopy(map)
                    new_map[i][j] = OBSTACLE
                    result += 1 if self.simulate_navigation(new_map) else 0

        return result

    def simulate_navigation(self, map: list[list[str]]) -> bool:
        n_rows, n_columns = len(map), len(map[0])
        initial_pos = list(find_occurrences_matrix(map, PLAYER))[0]
        py, px = initial_pos
        direction = INITIAL_DIRECTION

        obstacle_hits = set()

        while True:
            map[py][px] = VISITED

            next_pos = (py + direction[0], px + direction[1])

            if is_outside_map(next_pos, n_rows, n_columns):
                break

            if map[next_pos[0]][next_pos[1]] in OBSTACLE:
                entry = (py, px, direction)
                if entry in obstacle_hits:  # Loop
                    return True

                obstacle_hits.add(entry)

                direction = rotate(direction)
            else:
                py, px = next_pos[0], next_pos[1]

            if (py, px) == initial_pos and direction == INITIAL_DIRECTION:  # Loop
                return True

        return False
