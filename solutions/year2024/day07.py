from solutions.solution_base import SolutionBase


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


class Day07(SolutionBase):
    def load_input(self, input: str):
        input = input.split("\n")
        input = [tuple(s.split(":")) for s in input]
        for i, (res, eq) in enumerate(input):
            input[i] = (int(res), list(map(int, eq.strip().split())))
        self.equations = input

    def part1(self):
        result = 0
        for target, equation in self.equations:
            if test_equation(equation, target, 0, True):
                result += target

        return result

    def part2(self):
        result = 0
        for target, equation in self.equations:
            if test_equation_with_concat(equation, target, 0, True):
                result += target

        return result
