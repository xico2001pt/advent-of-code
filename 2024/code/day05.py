from common import print_title, print_solutions, read_file
from functools import cmp_to_key

DAY = 5
INPUT_FILES = {"rules": "day05_rules.txt", "updates": "day05_updates.txt"}


def parse_rules_input(input: str) -> list[tuple[int, int]]:
    return [tuple(map(int, line.split("|"))) for line in input.split("\n")]


def parse_updates_input(input: str) -> list[list[int]]:
    return [list(map(int, line.split(","))) for line in input.split("\n")]


def process_rules(rules: list[tuple[int, int]]) -> dict[set[int]]:
    processed = {}

    for pre, after in rules:
        if pre not in processed:
            processed[pre] = set()
        processed[pre].add(after)

    return processed


def sum_middle_elements(targets: list[list[int]]):
    return sum([t[len(t) // 2] for t in targets])


def part1(rules: dict[set[int]], updates: list[list[int]]):
    cmp = cmp_to_key(lambda x, y: -1 if y in rules.get(x, {}) else 0)

    result = 0
    for update in updates:
        s = sorted(update, key=cmp)
        if s == update:
            result += s[len(update) // 2]
    return result


def part2(rules: dict[set[int]], updates: list[list[int]]):
    cmp = cmp_to_key(lambda x, y: -1 if y in rules.get(x, {}) else 0)

    result = 0
    for update in updates:
        s = sorted(update, key=cmp)
        if s != update:
            result += s[len(update) // 2]
    return result


def main():
    print_title(DAY)

    rules_input, updates_input = read_file(INPUT_FILES["rules"]), read_file(
        INPUT_FILES["updates"]
    )

    rules = parse_rules_input(rules_input)
    updates = parse_updates_input(updates_input)

    rules = process_rules(rules)

    print_solutions([part1(rules, updates), part2(rules, updates)])


if __name__ == "__main__":
    main()
