from pathlib import Path
from typing import List, Optional

from translator.enums import VMCommandType, SegmentType, SEGMENT_MAP

SUPPORTED_ARITHMETIC_OPERATIONS = (
    "add",
    "sub",
    "neg",
    "eq",
    "gt",
    "lt",
    "and",
    "or",
    "not",
)


def get_command_type(line: str) -> VMCommandType:
    if line.startswith("push"):
        return VMCommandType.PUSH
    if line.startswith("pop"):
        return VMCommandType.POP
    if line in SUPPORTED_ARITHMETIC_OPERATIONS:
        return VMCommandType.ARITHMETIC
    raise ValueError(f"VM command '{line}' is not supported!")


class VMCommand:
    def __init__(self, line: str, vm_filename: str):
        self.type = get_command_type(line=line)
        self.command = line
        self.vm_filename = vm_filename
        self.segment: Optional[SegmentType] = self.get_segment_type()

    def get_segment_type(self) -> Optional[SegmentType]:
        segment_str = self.command.split(" ")[1]
        if segment_str in SEGMENT_MAP:
            return SEGMENT_MAP[segment_str]
        else:
            msg = f"Segment '{segment_str}' is not in supported segments!"
            raise ValueError(msg)


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
