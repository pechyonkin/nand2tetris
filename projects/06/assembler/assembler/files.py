from pathlib import Path
from typing import List


def strip_spaces(line: str) -> str:
    return line.lstrip().rstrip()


def load_lines(path: Path) -> List[str]:
    """Load lines and drop whitespaces at the beginning and end of each file.

    :param path: path to input .asm file
    :return: list of lines in the file
    """
    with open(path) as f:
        lines = f.readlines()
    lines = [strip_spaces(line) for line in lines]
    return lines
