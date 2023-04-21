# Parser of loaded lines
import os
from abc import abstractmethod
from enum import Enum
from pathlib import Path

from assembler.files import load_lines
from assembler.instruction_maps import COMP_MAP, DEST_MAP, JUMP_MAP


class LineType(Enum):
    COMMENT_LINE = 1
    EMPTY_LINE = 2
    A_INSTRUCTION = 3
    C_INSTRUCTION = 4


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
        return "111" + comp_bits + dest_bits + jump_bits


class AInstruction(Instruction):
    def __init__(self, address: str):
        self.address = address

    def make_machine_instruction(self) -> str:
        number = int(self.address)
        bin_string = bin(number)[2:]
        padded_bin_string = bin_string.zfill(15)
        return "0" + padded_bin_string


def get_line_type(line: str) -> LineType:
    """Determine line type of code line.

    :param line: code line with whitespace stripped on left and right
    :return: LineType of line
    """
    if not line:
        return LineType.EMPTY_LINE
    if "//" in line:
        return LineType.COMMENT_LINE
    if "@" in line:
        return LineType.A_INSTRUCTION
    return LineType.C_INSTRUCTION


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


def parse_a_instruction(line: str) -> AInstruction:
    address_string = line[1:]  # Extract the number part of the A-instruction.
    return AInstruction(address=address_string)


def process_file(path_to_file: Path) -> None:
    lines = load_lines(path=path_to_file)
    instructions = []
    for line in lines:
        line_type = get_line_type(line=line)
        if line_type == LineType.C_INSTRUCTION:
            instructions.append(parse_c_instruction(line=line))
        if line_type == LineType.A_INSTRUCTION:
            instructions.append(parse_a_instruction(line=line))

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

    out_lines = [instr.make_machine_instruction() + "\n" for instr in instructions]

    with open(out_path, "w") as f:
        f.writelines(out_lines)
