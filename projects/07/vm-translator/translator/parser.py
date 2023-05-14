from pathlib import Path
from typing import List


def cleanse_lines(lines: List[str]) -> List[str]:
    out_lines = []
    for line in lines:
        if line.startswith("/"):
            # ignore full comment lines
            continue
        if "//" in line:
            # remove comments after code
            line = line.split("//")[0]
        # remove whitespace including new line chars
        line = line.lstrip().rstrip()
        if line:
            # will ignore empty lines
            out_lines.append(line)
    return out_lines


def load_vm_lines(path: Path) -> List[str]:
    with open(path) as f:
        raw_lines = f.readlines()
    clean_lines = cleanse_lines(lines=raw_lines)
    return clean_lines
