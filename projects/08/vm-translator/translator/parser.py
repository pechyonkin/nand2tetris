from functools import partial
from pathlib import Path
from typing import List, Optional, Callable, Dict

from translator.arithmetic_ops import (
    not_op,
    neg_op,
    add,
    sub,
    or_op,
    and_op,
    eq,
    lt,
    gt,
)
from translator.enums import VMCommandType, SegmentType, SEGMENT_TO_TYPE_MAP
from translator.memory_segments import (
    push_constant,
    push_offset,
    pop_offset,
    push_static,
    pop_static,
    push_pointer,
    pop_pointer,
)
from translator.label_ops import label_op, goto_op, if_goto_op

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


PUSH_SEGMENT_FN_MAP: Dict[SegmentType, Callable[[str, str, int], List[str]]] = {
    SegmentType.CONSTANT: push_constant,
    SegmentType.LOCAL: partial(push_offset, SegmentType.LOCAL),
    SegmentType.ARGUMENT: partial(push_offset, SegmentType.ARGUMENT),
    SegmentType.THIS: partial(push_offset, SegmentType.THIS),
    SegmentType.THAT: partial(push_offset, SegmentType.THAT),
    SegmentType.TEMP: partial(push_offset, SegmentType.TEMP),
    SegmentType.STATIC: push_static,
    SegmentType.POINTER: push_pointer,
}


POP_SEGMENT_FN_MAP: Dict[SegmentType, Callable[[str, str, int], List[str]]] = {
    SegmentType.LOCAL: partial(pop_offset, SegmentType.LOCAL),
    SegmentType.ARGUMENT: partial(pop_offset, SegmentType.ARGUMENT),
    SegmentType.THIS: partial(pop_offset, SegmentType.THIS),
    SegmentType.THAT: partial(pop_offset, SegmentType.THAT),
    SegmentType.TEMP: partial(pop_offset, SegmentType.TEMP),
    SegmentType.STATIC: pop_static,
    SegmentType.POINTER: pop_pointer,
}


LABEL_OP_FN_MAP: Dict[VMCommandType, Callable[[str, str, int], List[str]]] = {
    VMCommandType.LABEL: label_op,
    VMCommandType.GOTO: goto_op,
    VMCommandType.IF_GOTO: if_goto_op,
}


ARITHMETIC_FN_MAP: Dict[str, Callable[[str, int], List[str]]] = {
    "add": add,
    "eq": eq,
    "lt": lt,
    "gt": gt,
    "sub": sub,
    "or": or_op,
    "not": not_op,
    "neg": neg_op,
    "and": and_op,
}


def get_cmd_type(line: str) -> VMCommandType:
    """Get VM command type from code line.
    Code line is assumed to be stripped of comments and spaces."""
    if line.startswith("push"):
        return VMCommandType.PUSH
    if line.startswith("pop"):
        return VMCommandType.POP
    if line in SUPPORTED_ARITHMETIC_OPERATIONS:
        return VMCommandType.ARITHMETIC
    if line.startswith("label"):
        return VMCommandType.LABEL
    if line.startswith("goto"):
        return VMCommandType.GOTO
    if line.startswith("if-goto"):
        return VMCommandType.IF_GOTO
    if line.startswith("function"):
        return VMCommandType.FUNCTION
    if line.startswith("call"):
        return VMCommandType.CALL
    if line.startswith("return"):
        return VMCommandType.RETURN
    raise ValueError(f"VM command '{line}' is not supported!")


def get_vm_filename(path: Path) -> str:
    return path.stem


def get_value(line: str) -> str:
    return line.split(" ")[-1]


class VMCommand:
    def __init__(self, line: str, vm_filename: str):
        self.cmd_type = get_cmd_type(line=line)
        self.command = line
        self.vm_filename = vm_filename
        self.segment_type: Optional[SegmentType] = self.get_segment_type()

    def get_segment_type(self) -> Optional[SegmentType]:
        if self.cmd_type not in (VMCommandType.POP, VMCommandType.PUSH):
            return None
        segment_str = self.command.split(" ")[1]
        if segment_str in SEGMENT_TO_TYPE_MAP:
            return SEGMENT_TO_TYPE_MAP[segment_str]
        else:
            msg = f"Segment '{segment_str}' is not in supported segments!"
            raise ValueError(msg)

    def __str__(self):
        segment = "None" if not self.segment_type else self.segment_type.name
        str_repr = (
            f"VMCommand('{self.command}', '{self.cmd_type.name}', "
            f"'{segment}', '{self.vm_filename}')"
        )
        return str_repr

    def to_assembly(self, line_num: int) -> List[str]:
        """Produce a list of assembly commands for this VM command."""
        fname = self.vm_filename
        result = [f"// {self.command}"]
        if (
            self.cmd_type == VMCommandType.PUSH
            and self.segment_type in PUSH_SEGMENT_FN_MAP
        ):
            push_value = get_value(self.command)
            assembly_lines = PUSH_SEGMENT_FN_MAP[self.segment_type](
                push_value, fname, line_num
            )
        elif (
            self.cmd_type == VMCommandType.POP
            and self.segment_type in POP_SEGMENT_FN_MAP
        ):
            pop_value = get_value(self.command)
            assembly_lines = POP_SEGMENT_FN_MAP[self.segment_type](
                pop_value, fname, line_num
            )
        elif (
            self.cmd_type == VMCommandType.ARITHMETIC
            and self.command in ARITHMETIC_FN_MAP
        ):
            assembly_lines = ARITHMETIC_FN_MAP[self.command](fname, line_num)
        elif self.cmd_type in (
            VMCommandType.LABEL,
            VMCommandType.GOTO,
            VMCommandType.IF_GOTO,
        ):
            assembly_lines = LABEL_OP_FN_MAP[self.cmd_type](
                self.command, fname, line_num
            )
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


def vm_commands_to_assembly(
    vm_commands: List[VMCommand],
) -> List[str]:
    assembly_lines = []
    for line_number, vm_command in enumerate(vm_commands):
        assembly_lines.extend(
            vm_command.to_assembly(
                line_num=line_number,
            )
        )
    return assembly_lines


def get_assembly_lines(path: Path) -> List[str]:
    vm_commands = load_vm_commands(path=path)
    asm = vm_commands_to_assembly(vm_commands=vm_commands)
    return asm


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
