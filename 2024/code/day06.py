from common import print_title, print_solutions, read_file, find_occurrences_matrix
import copy

DAY = 6
INPUT_FILE = "day06.txt"

PLAYER = "^"
OBSTACLE = "#"
VISITED = "X"
EMPTY = "."

INITIAL_DIRECTION = (-1, 0)


def parse_input(input: str) -> list[list[str]]:
    return [[c for c in row] for row in input.split("\n")]


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


def simulate_navigation(map: list[list[str]]) -> bool:
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


def part1(map: list[list[str]]):
    simulate_navigation(map)
    return len(find_occurrences_matrix(map, "X"))


def part2(map: list[list[str]]):
    n_rows, n_columns = len(map), len(map[0])

    result = 0
    for i in range(n_rows):
        print(f"Progress: {i+1}/{n_rows}")
        for j in range(n_columns):
            elem = map[i][j]
            if elem == EMPTY:
                new_map = copy.deepcopy(map)
                new_map[i][j] = OBSTACLE
                result += 1 if simulate_navigation(new_map) else 0

    return result


def main():
    print_title(DAY)

    input = read_file(INPUT_FILE)
    map = parse_input(input)

    print_solutions([part1(copy.deepcopy(map)), part2(map)])


if __name__ == "__main__":
    main()
