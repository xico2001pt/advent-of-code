from common import (
    print_title,
    print_solutions,
    read_file,
    count_frequency
)

DAY = 1
INPUT_FILE = "day01.txt"


def parse_input(input: str) -> tuple[list[int], list[int]]:
    input = input.split()
    input = [int(v) for v in input]
    return input[0::2], input[1::2]


def part1(list1: list[int], list2: list[int]):
    list1, list2 = sorted(list1), sorted(list2)

    result = 0
    for v1, v2 in zip(list1, list2):
        result += abs(v1 - v2)

    return result


def part2(list1: list[int], list2: list[int]):
    freq = count_frequency(list2)

    result = 0
    for v in list1:
        result += v * freq.get(v, 0)

    return result


def main():
    print_title(DAY)

    input = read_file(INPUT_FILE)
    list1, list2 = parse_input(input)

    print_solutions([
        part1(list1, list2),
        part2(list1, list2)
    ])


if __name__ == "__main__":
    main()
