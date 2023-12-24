import argparse
import os
import sys

from adventofcode.util.console import console
from config import SOLUTIONS_DIR


def clean_repo():
    dry_run = _parser(sys.argv[1:])
    _clean_solutions(dry_run)


def _parser(args: list[str]) -> bool:
    parser = argparse.ArgumentParser(description="Clean repository")
    parser.add_argument(
        "--dry-run",
        type=str,
        default="true",
        help="Specify if it should be run as dry run. Default is True",
    )
    parsed = parser.parse_args(args)
    return parsed.dry_run != "false"  # type: ignore


def _clean_solutions(dry_run: bool = True):
    for directory in sorted(os.listdir(SOLUTIONS_DIR)):
        if directory.startswith("year_"):
            dir_path = os.path.join(SOLUTIONS_DIR, directory)
            for file in sorted(os.listdir(dir_path)):
                file_path = os.path.join(dir_path, file)

                if not dry_run:
                    console.print(f"[red]deleting[/red] file {file_path}")
                    os.remove(file_path)
                else:
                    console.print(f"deleting file {file_path} (dry run)")


if __name__ == "__main__":
    clean_repo()
