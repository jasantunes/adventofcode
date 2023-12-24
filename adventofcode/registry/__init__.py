import os.path
from collections.abc import Callable
from importlib import import_module
from typing import Any

from config import SOLUTIONS_DIR

registry: dict[str, Callable[[Any], Any]] = {}


def autodetect():
    """Automatically detects all solutions in the project"""
    days = sorted(SOLUTIONS_DIR.rglob("year_*/day_*.py"))

    for day in days:
        import_module(f"solutions.{day.parent.name}.{os.path.splitext(day.name)[0]}")
