import os
from pathlib import Path

ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
SOLUTIONS_DIR = Path(os.path.join(ROOT_DIR, "solutions"))
RUNNING_ALL = False
RUNNING_BENCHMARKS = False
