# Parser of loaded lines
import os
from abc import abstractmethod
from enum import Enum
from pathlib import Path
from typing import List, Dict

from assembler.files import load_lines, strip_spaces
from assembler.instruction_maps import COMP_MAP, DEST_MAP, JUMP_MAP, PREDEFINED_SYMBOLS


class LineType(Enum):
    COMMENT_LINE = 1
    EMPTY_LINE = 2
    A_INSTRUCTION = 3
    C_INSTRUCTION = 4
    LABEL_SYMBOL = 5


class Instruction:
    @abstractmethod
    def make_machine_instruction(self) -> str:
        raise NotImplementedError


class CInstruction(Instruction):
    def __init__(self, comp: str, dest: str, jump: str):
        self.comp = comp
        self.dest = dest
        self.jump = jump

    def make_machine_instruction(self) -> str:
        comp_bits = COMP_MAP[self.comp]
        dest_bits = DEST_MAP[self.dest]
        jump_bits = JUMP_MAP[self.jump]
        return "111" + comp_bits + dest_bits + jump_bits + "\n"


def int_to_address(number: int) -> str:
    bin_string = bin(number)[2:]
    padded_bin_string = bin_string.zfill(15)
    return padded_bin_string


def int_to_a_instruction(number: int) -> str:
    return "0" + int_to_address(number=number) + "\n"


class AInstruction(Instruction):
    def __init__(self, address: str):
        self.address = address

    def make_machine_instruction(self) -> str:
        number = int(self.address)
        return int_to_a_instruction(number=number)


def get_line_type(line: str) -> LineType:
    """Determine line type of code line.

    :param line: code line with whitespace stripped on left and right
    :return: LineType of line
    """
    if not line:
        return LineType.EMPTY_LINE
    if line.startswith("//"):
        return LineType.COMMENT_LINE
    if line.startswith("@"):
        return LineType.A_INSTRUCTION
    if line.startswith("("):
        return LineType.LABEL_SYMBOL
    return LineType.C_INSTRUCTION


def get_label_symbols_dict(lines: List[str]) -> Dict[str, int]:
    symbols_dict = dict()
    cur_code_line = -1
    for line in lines:
        line_type = get_line_type(line=line)
        if line_type == LineType.A_INSTRUCTION:
            cur_code_line += 1
        elif line_type == LineType.C_INSTRUCTION:
            cur_code_line += 1
        elif line_type == LineType.LABEL_SYMBOL:
            symbol = line[1:-1]
            symbols_dict[symbol] = cur_code_line + 1
    return symbols_dict


def get_variable_symbols_dict(
    lines: List[str],
    symbols_dict: Dict[str, int],
) -> Dict[str, int]:
    """Add variable symbols to symbol dictionary.

    Need existing symbol dictionary to not treat predefined and label symbols as
    variable symbols."""
    cur_var_idx = 16
    for line in lines:
        line_type = get_line_type(line=line)
        if line_type == LineType.A_INSTRUCTION:
            symbol = line[1:]
            if not symbol.isnumeric() and symbol not in symbols_dict:
                symbols_dict[symbol] = cur_var_idx
                cur_var_idx += 1
    return symbols_dict


def parse_c_instruction(line: str) -> CInstruction:
    # Handle jump part
    line_split_for_jump = line.split(";")
    if len(line_split_for_jump) == 1:
        jump = ""
    else:
        jump = line_split_for_jump[-1]
    line = line_split_for_jump[0]

    # Handle destination and comp parts
    line_split_for_dest = line.split("=")
    if len(line_split_for_dest) == 1:
        dest = ""
        comp = line_split_for_dest[0]
    else:
        dest = line_split_for_dest[0]
        comp = line_split_for_dest[-1]

    # print(f"DEST: {dest}")
    # print(f"COMP: {comp}")
    # print(f"JUMP: {jump}")

    return CInstruction(dest=dest, comp=comp, jump=jump)


def parse_a_instruction(
    line: str,
    symbols_dict: Dict[str, int] = None,
) -> AInstruction:
    # Extract the number or symbol part of the A-instruction.
    num_part = line[1:]
    if num_part.isnumeric():
        return AInstruction(address=num_part)
    assert num_part in symbols_dict, f"Symbol {num_part} not found in symbols!"
    return AInstruction(address=str(symbols_dict[num_part]))


def remove_comment_after_instruction(line: str) -> str:
    """Remove comment after an instruction, if any."""
    return strip_spaces(line.split("//")[0])


def process_lines(lines: List[str]) -> List[str]:
    symbols_dict = PREDEFINED_SYMBOLS.copy()
    symbols_dict |= get_label_symbols_dict(lines=lines)
    symbols_dict |= get_variable_symbols_dict(lines=lines, symbols_dict=symbols_dict)
    instructions = []
    for line in lines:
        line_type = get_line_type(line=line)
        instruction = None
        if line_type == LineType.C_INSTRUCTION:
            instruction = parse_c_instruction(line=line)
        if line_type == LineType.A_INSTRUCTION:
            instruction = parse_a_instruction(
                line=line,
                symbols_dict=symbols_dict,
            )
        if instruction:
            instructions.append(instruction)

    out_lines = [i.make_machine_instruction() for i in instructions]
    return out_lines


def filter_lines(lines: List[str]) -> List[str]:
    """Only keep instruction lines, and remove comments in instruction lines."""
    clean_lines = []
    for line in lines:
        line_type = get_line_type(line=line)
        if line_type in [
            LineType.A_INSTRUCTION,
            LineType.C_INSTRUCTION,
            LineType.LABEL_SYMBOL,
        ]:
            line = remove_comment_after_instruction(line=line)
            clean_lines.append(line)
    return clean_lines


def process_file(path_to_file: Path) -> None:
    lines = load_lines(path=path_to_file)
    lines = filter_lines(lines=lines)
    out_lines = process_lines(lines=lines)

    in_fname = path_to_file.name
    dir_name = path_to_file.parent
    out_fname = in_fname.split(".")[0] + ".hack"
    out_path = dir_name / out_fname

    print(f"IN FNAME: {in_fname}")
    print(f"OUT FNAME: {out_fname}")
    print(f"DIR: {dir_name}")
    print(f"OUT PATH {out_path}")

    if out_path.exists():
        print(f"OUTPUT PATH '{out_path}' EXISTS!")
        print(f"DELETING '{out_path}'!")
        os.remove(out_path)

    with open(out_path, "w") as f:
        f.writelines(out_lines)
