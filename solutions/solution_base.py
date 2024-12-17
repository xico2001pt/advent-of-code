from abc import ABC, abstractmethod


class SolutionBase(ABC):
    """
    Base class for all Advent of Code solutions.
    Provides a common interface for solutions.
    """

    @abstractmethod
    def load_input(self, input: str):
        """Load the input content."""
        pass

    @abstractmethod
    def part1(self):
        """Solve part 1 of the day's challenge."""
        pass

    @abstractmethod
    def part2(self):
        """Solve part 2 of the day's challenge."""
        pass
