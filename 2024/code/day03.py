from common import print_title, print_solutions, read_file
import re

DAY = 3
INPUT_FILE = "day03.txt"


def find_operations(memory: str) -> list[str]:
    return re.findall("mul\([0-9]?[0-9]?[0-9]?,[0-9]?[0-9]?[0-9]?\)", memory)


def find_operations_with_enablers(memory: str) -> list[str]:
    return re.findall(
        "(do\(\))|(don't\(\))|(mul\([0-9]?[0-9]?[0-9]?,[0-9]?[0-9]?[0-9]?\))", memory
    )


def extract_numbers(s: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", s)))


def is_mul_op(t: tuple[str]) -> bool:
    return len(t[2]) > 0


def is_do_op(t: tuple[str]) -> bool:
    return len(t[0]) > 0


def part1(memory: str):
    ops = find_operations(memory)

    result = 0
    for op in ops:
        a, b = extract_numbers(op)
        result += a * b

    return result


def part2(memory: str):
    ops = find_operations_with_enablers(memory)

    result = 0
    is_mul_enabled = True
    for op in ops:
        if is_mul_op(op):
            if is_mul_enabled:
                a, b = extract_numbers(op[2])
                result += a * b
        else:
            is_mul_enabled = is_do_op(op)

    return result


def main():
    print_title(DAY)

    input = read_file(INPUT_FILE)

    print_solutions([part1(input), part2(input)])


if __name__ == "__main__":
    main()
