import argparse
from utils.logger import log_title, log_solution
from utils.storage import load_solution_class, load_input_file
from utils.timer import measure_time


def run_solution(year: str, day: str, input_type: str):
    """
    Dynamically run the solution for a specified year, day, and input type.

    Args:
        year (str): Year of the challenge (e.g., "2024").
        day (str): Day/Level of the challenge (e.g., "03").
        input_type (str): Input type ('small' or 'large').
    """
    try:
        solution_class = load_solution_class(year, day)()
        input = load_input_file(year, day, input_type)

        solution_class.load_input(input)

        log_title(year, day)
        solution, time = measure_time(solution_class.part1)
        log_solution(1, solution, time)
        solution, time = measure_time(solution_class.part2)
        log_solution(2, solution, time)

    except (ModuleNotFoundError, AttributeError):
        print(f"Solution for Year {year}, Day {day} not found.")
    except FileNotFoundError:
        print(f"Input file not found")
    except Exception as e:
        import traceback

        print(traceback.format_exc())


def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("year", type=str, help="Year of the challenge (e.g., '2024').")
    parser.add_argument("day", type=str, help="Day/Level of the challenge (e.g., '3').")
    parser.add_argument(
        "input_type",
        type=str,
        choices=["small", "large"],
        help="Input type ('small' or 'large').",
    )

    args = parser.parse_args()

    # Ensure day is zero-padded
    day = args.day.zfill(2)

    run_solution(args.year, day, args.input_type)


if __name__ == "__main__":
    main()
