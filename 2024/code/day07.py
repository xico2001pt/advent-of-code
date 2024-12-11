from common import print_title, print_solutions, read_file

DAY = 7
INPUT_FILE = "day07.txt"


def parse_input(input: str) -> list[tuple[int, list[int]]]:
    input = input.split("\n")
    input = [tuple(s.split(":")) for s in input]
    for i, (res, eq) in enumerate(input):
        input[i] = (int(res), list(map(int, eq.strip().split())))
    return input


def test_equation(
    values: list[int], target: int, current: int, isFirst: bool = False
) -> bool:
    if len(values) == 0:
        return target == current

    return test_equation(values[1:], target, current + values[0]) or test_equation(
        values[1:], target, (1 if isFirst else current) * values[0]
    )


def concat(num1: int, num2: int) -> int:
    return int(str(num1) + str(num2))


def test_equation_with_concat(
    values: list[int], target: int, current: int, isFirst: bool = False
) -> bool:
    if len(values) == 0:
        return target == current

    return (
        test_equation_with_concat(values[1:], target, current + values[0])
        or test_equation_with_concat(
            values[1:], target, (1 if isFirst else current) * values[0]
        )
        or test_equation_with_concat(values[1:], target, concat(current, values[0]))
    )


def part1(equations: list[tuple[int, list[int]]]):
    result = 0
    for target, equation in equations:
        if test_equation(equation, target, 0, True):
            result += target

    return result


def part2(equations: list[tuple[int, list[int]]]):
    result = 0
    for target, equation in equations:
        if test_equation_with_concat(equation, target, 0, True):
            result += target

    return result


def main():
    print_title(DAY)

    input = read_file(INPUT_FILE)
    equations = parse_input(input)

    print_solutions([part1(equations), part2(equations)])


if __name__ == "__main__":
    main()
