import ast
import os
import re

from config import ROOT_DIR, SOLUTIONS_DIR


def get_full_year_paths() -> list[str]:
    """
    Retrieves all directories in the ROOT_DIR that start with 'year_'
    """
    paths = [os.path.join(SOLUTIONS_DIR, val) for val in os.listdir(SOLUTIONS_DIR) if re.match(r"^year_\d{4}$", val)]
    return sorted(paths)


def get_full_day_paths(year_path: str) -> list[str]:
    """
    Retrieves all files in the ROOT_DIR/year_{year} directory that start with 'day_'
    """
    paths = [os.path.join(year_path, val) for val in os.listdir(year_path) if re.match(r"^day_\d{2}\.py$", val)]
    return sorted(paths)


def get_functions_from_day_file(day: str):
    """
    Uses ast to retrieve all top level functions in the provided day file
    """
    with open(day) as f:
        parsed = ast.parse(f.read(), filename=day)

    return [func.name for func in parsed.body if isinstance(func, ast.FunctionDef)]


def clean_year(year_path: str) -> int:
    """
    Removes the 'year_' prefix from the year directory
    """
    year_segment = year_dir_from_path(year_path)
    return int(year_segment[len("year_") :])


def clean_day(day_file: str) -> int:
    """
    Removes the 'day_' prefix, _year suffix and .py extension from the day file
    """
    segments = day_file.split(os.sep)
    day_segment = segments[-1].replace(".py", "")

    return int(day_segment[-2:])


def year_dir_from_path(year_dir: str) -> str:
    """
    Retrieves the module part from the year directory path
    Example: year_2020
    """
    segments = year_dir.split(os.sep)
    return segments[-1]


def get_full_module_from_day_file(day_file: str) -> str:
    """
    Returns the full module for the given day file
    Example: adventofcode.year_2020.day_01
    """
    segments = day_file.split(os.sep)
    segments = ["solutions"] + segments[-2:]
    module = ".".join(segments).replace(".py", "")
    return module
