from solutions.solution_base import SolutionBase
from functools import cmp_to_key


def process_rules(rules: list[tuple[int, int]]) -> dict[set[int]]:
    processed = {}

    for pre, after in rules:
        if pre not in processed:
            processed[pre] = set()
        processed[pre].add(after)

    return processed


def sum_middle_elements(targets: list[list[int]]) -> int:
    return sum([t[len(t) // 2] for t in targets])


class Day05(SolutionBase):
    def load_input(self, input: str):
        rules, updates = input.split("\n\n")
        self.parse_rules_input(rules)
        self.parse_updates_input(updates)

    def parse_rules_input(self, input: str):
        rules = [tuple(map(int, line.split("|"))) for line in input.split("\n")]
        self.rules = process_rules(rules)

    def parse_updates_input(self, input: str):
        self.updates = [list(map(int, line.split(","))) for line in input.split("\n")]

    def part1(self):
        cmp = cmp_to_key(lambda x, y: -1 if y in self.rules.get(x, {}) else 0)

        result = 0
        for update in self.updates:
            s = sorted(update, key=cmp)
            if s == update:
                result += s[len(update) // 2]
        return result

    def part2(self):
        cmp = cmp_to_key(lambda x, y: -1 if y in self.rules.get(x, {}) else 0)

        result = 0
        for update in self.updates:
            s = sorted(update, key=cmp)
            if s != update:
                result += s[len(update) // 2]
        return result
