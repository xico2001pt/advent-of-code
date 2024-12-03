from common import print_title, print_solutions, read_file

DAY = 2
INPUT_FILE = "day02.txt"


def parse_input(input: str) -> list[list[int]]:
    input = input.split("\n")
    input = [s.split() for s in input]
    return [[int(v) for v in s] for s in input]


def check_increase(v1, v2) -> bool:
    return v1 < v2


def check_decrease(v1, v2) -> bool:
    return v1 > v2


def check_report(report: list[int]) -> bool:
    check_func = check_increase if (report[0] < report[1]) else check_decrease
    curr = report[0]
    for i in range(1, len(report)):
        prev = curr
        curr = report[i]
        dist = abs(prev - curr)
        if dist < 1 or dist > 3 or not check_func(prev, curr):
            return False
    return True


def part1(values: list[list[int]]):
    safe_reports = 0
    for report in values:
        safe_reports += 1 if check_report(report) else 0

    return safe_reports


def part2(values: list[list[int]]):
    safe_reports = 0
    for report in values:
        safe_reports += (
            1
            if any(
                [check_report(report[:i] + report[i + 1 :]) for i in range(len(report))]
            )
            else 0
        )

    return safe_reports


def main():
    print_title(DAY)

    input = read_file(INPUT_FILE)
    values = parse_input(input)

    print_solutions([part1(values), part2(values)])


if __name__ == "__main__":
    main()
