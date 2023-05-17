from pathlib import Path
from typing import List, Optional, Callable, Dict

from translator.assemby import push_constant, add
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


PUSH_SEGMENT_FN_MAP: Dict[SegmentType, Callable[[str], List[str]]] = {
    SegmentType.CONSTANT: push_constant,
}


ARITHMETIC_FN_MAP: Dict[str, Callable[[], List[str]]] = {
    "add": add,
}


def get_command_type(line: str) -> VMCommandType:
    if line.startswith("push"):
        return VMCommandType.PUSH
    if line.startswith("pop"):
        return VMCommandType.POP
    if line in SUPPORTED_ARITHMETIC_OPERATIONS:
        return VMCommandType.ARITHMETIC
    raise ValueError(f"VM command '{line}' is not supported!")


def get_vm_filename(path: Path) -> str:
    return path.name


def get_value(line: str) -> str:
    return line.split(" ")[-1]


class VMCommand:
    def __init__(self, line: str, vm_filename: str):
        self.command_type = get_command_type(line=line)
        self.command = line
        self.vm_filename = vm_filename
        self.segment_type: Optional[SegmentType] = self.get_segment_type()

    def get_segment_type(self) -> Optional[SegmentType]:
        if self.command_type == VMCommandType.ARITHMETIC:
            return None
        segment_str = self.command.split(" ")[1]
        if segment_str in SEGMENT_MAP:
            return SEGMENT_MAP[segment_str]
        else:
            msg = f"Segment '{segment_str}' is not in supported segments!"
            raise ValueError(msg)

    def __str__(self):
        segment = "None" if not self.segment_type else self.segment_type.name
        str_repr = (
            f"VMCommand('{self.command}', '{self.command_type.name}', "
            f"'{segment}', '{self.vm_filename}')"
        )
        return str_repr

    def to_assembly(self) -> List[str]:
        """Produce a list of assembly commands for this VM command."""
        if (
            self.command_type == VMCommandType.PUSH
            and self.segment_type in PUSH_SEGMENT_FN_MAP
        ):
            push_value = get_value(self.command)
            return PUSH_SEGMENT_FN_MAP[self.segment_type](push_value)
        if (
            self.command_type == VMCommandType.ARITHMETIC
            and self.command in ARITHMETIC_FN_MAP
        ):
            return ARITHMETIC_FN_MAP[self.command]()
        msg = f"Couldn't assemble VM Command '{self.__str__()}'"
        raise NotImplementedError(msg)


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


def load_vm_commands(path: Path) -> List[VMCommand]:
    lines = load_vm_lines(path=path)
    fname = get_vm_filename(path=path)
    commands = [VMCommand(line=line, vm_filename=fname) for line in lines]
    return commands
