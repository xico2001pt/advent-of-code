from solutions.solution_base import SolutionBase


def check_increase(v1, v2) -> bool:
    return v1 < v2


def check_decrease(v1, v2) -> bool:
    return v1 > v2


class Day02(SolutionBase):
    def load_input(self, input: str):
        input = input.split("\n")
        input = [s.split() for s in input]
        self.reports = [list(map(int, s)) for s in input]

    def part1(self):
        safe_reports = 0
        for report in self.reports:
            safe_reports += 1 if self.check_report(report) else 0

        return safe_reports

    def part2(self):
        safe_reports = 0
        for report in self.reports:
            safe_reports += (
                1
                if any(
                    [
                        self.check_report(report[:i] + report[i + 1 :])
                        for i in range(len(report))
                    ]
                )
                else 0
            )

        return safe_reports

    def check_report(self, report: list[int]) -> bool:
        check_func = check_increase if (report[0] < report[1]) else check_decrease
        curr = report[0]
        for i in range(1, len(report)):
            prev = curr
            curr = report[i]
            dist = abs(prev - curr)
            if dist < 1 or dist > 3 or not check_func(prev, curr):
                return False
        return True
