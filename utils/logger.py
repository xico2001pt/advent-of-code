def log_title(year: str, day: str):
    """
    Prints a formatted title for a specific year and day.

    Args:
        year (str): The year of the problem.
        day (str): The day of the challenge.

    Prints:
        A formatted title displaying the year and day.
    """
    print(f"--- Year {year}, Day {day} ---")


def log_solution(part: int, solution, elapsed_time: float):
    """
    Log the solution for a given part and the time taken.

    Args:
        part (int): Part number (1 or 2).
        solution: The solution result.
        elapsed_time (float): Time taken to compute the solution.
    """
    print(f"Part {part}: {solution} (executed in {elapsed_time:.6f} seconds.)")
