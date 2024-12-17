import os
import importlib
from solutions.solution_base import SolutionBase
from utils.constants import INPUTS_FOLDER_PATH, SOLUTIONS_FOLDER_NAME


def load_module(module_path: str):
    return importlib.import_module(module_path)


def load_solution_class(year: str, day: str) -> SolutionBase:
    return getattr(
        load_module(f"{SOLUTIONS_FOLDER_NAME}.year{year}.day{day}"), f"Day{day}"
    )


def read_file(file_path: str) -> str:
    return open(os.path.join(INPUTS_FOLDER_PATH, file_path)).read().strip()


def load_input_file(year: str, day: str, input_type: str) -> str:
    return read_file(os.path.join(year, f"day{day}_{input_type}.txt"))
