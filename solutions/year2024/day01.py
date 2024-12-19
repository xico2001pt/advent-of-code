from collections import Counter
from solutions.solution_base import SolutionBase


class Day01(SolutionBase):
    def load_input(self, input: str):
        input = list(map(int, input.split()))
        self.left_list = sorted(input[0::2])
        self.right_list = sorted(input[1::2])

    def part1(self):
        return sum(
            map(
                lambda pair: abs(pair[0] - pair[1]),
                zip(self.left_list, self.right_list),
            )
        )

    def part2(self):
        counter = Counter(self.right_list)
        return sum(v * counter[v] for v in self.left_list)
