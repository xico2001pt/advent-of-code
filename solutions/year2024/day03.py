from solutions.solution_base import SolutionBase
import re


def extract_numbers(s: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", s)))


class Day03(SolutionBase):
    def load_input(self, input: str):
        self.memory = input

    def part1(self):
        ops = self.find_operations()

        result = 0
        for op in ops:
            a, b = extract_numbers(op)
            result += a * b

        return result

    def part2(self):
        ops = self.find_operations_with_enablers()

        result = 0
        is_mul_enabled = True
        for op in ops:
            if self.is_mul_op(op):
                if is_mul_enabled:
                    a, b = extract_numbers(op[2])
                    result += a * b
            else:
                is_mul_enabled = self.is_do_op(op)

        return result

    def find_operations(self) -> list[str]:
        return re.findall("mul\([0-9]?[0-9]?[0-9]?,[0-9]?[0-9]?[0-9]?\)", self.memory)

    def find_operations_with_enablers(self) -> list[str]:
        return re.findall(
            "(do\(\))|(don't\(\))|(mul\([0-9]?[0-9]?[0-9]?,[0-9]?[0-9]?[0-9]?\))",
            self.memory,
        )

    def is_mul_op(self, t: tuple[str]) -> bool:
        return len(t[2]) > 0

    def is_do_op(self, t: tuple[str]) -> bool:
        return len(t[0]) > 0
