from pathlib import Path
from typing import List, Optional, Callable, Dict

from translator.assembly import push_constant, add
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


ARITHMETIC_FN_MAP: Dict[str, Callable[[str, int], List[str]]] = {
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

    def to_assembly(self, fname: str, line_num: int) -> List[str]:
        """Produce a list of assembly commands for this VM command."""
        result = [f"// {self.command}"]
        if (
            self.command_type == VMCommandType.PUSH
            and self.segment_type in PUSH_SEGMENT_FN_MAP
        ):
            push_value = get_value(self.command)
            assembly_lines = PUSH_SEGMENT_FN_MAP[self.segment_type](push_value)
        elif (
            self.command_type == VMCommandType.ARITHMETIC
            and self.command in ARITHMETIC_FN_MAP
        ):
            assembly_lines = ARITHMETIC_FN_MAP[self.command](fname, line_num)
        else:
            msg = f"Couldn't assemble VM Command '{self.__str__()}'"
            raise NotImplementedError(msg)
        result.extend(assembly_lines)
        return result


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


def get_assembly_lines(path: Path) -> List[str]:
    vm_commands = load_vm_commands(path=path)
    assembly_lines = []
    fname = path.stem
    for line_number, vm_command in enumerate(vm_commands):
        assembly_lines.extend(
            vm_command.to_assembly(
                fname=fname,
                line_num=line_number,
            )
        )
    return assembly_lines


def get_output_path(path: Path) -> Path:
    """Create output path in same directory with same name but .asm extension"""
    file_dir = path.parent
    fname_no_extension = path.stem
    fname_asm = fname_no_extension + ".asm"
    out_path = file_dir / fname_asm
    return out_path


def process_file(path: Path) -> None:
    assembly_lines = get_assembly_lines(path=path)
    assembly_lines = [line + "\n" for line in assembly_lines]
    out_path = get_output_path(path=path)
    with open(out_path, "w") as out_f:
        out_f.writelines(assembly_lines)
