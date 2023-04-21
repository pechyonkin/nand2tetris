# Parser of loaded lines
from abc import abstractmethod
from enum import Enum

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
        address_bits = ...  # 15-bit representation of address
        return "0" + address_bits


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

    print(f"DEST: {dest}")
    print(f"COMP: {comp}")
    print(f"JUMP: {jump}")

    return CInstruction(dest=dest, comp=comp, jump=jump)


def parse_a_instruction(line: str) -> AInstruction:
    """
    Parses an A-instruction in Hack assembly language and returns its binary representation.

    :param line: A string representing an A-instruction, in the format "@number".
    :return: An AInstruction object, containing the binary representation of the address.
    """
    number_string = line[1:]  # Extract the number part of the A-instruction.
    number = int(number_string)  # Convert the number string to an integer.
    bin_string = bin(number)[2:]  # Convert the integer to a binary string.
    padded_bin_string = bin_string.zfill(
        15
    )  # Pad the binary string with zeroes to make it 15 characters long.
    instruction = (
        "0" + padded_bin_string
    )  # Prepend the instruction type (0) to the binary address.
    return AInstruction(
        address=instruction
    )  # Return an AInstruction object with the binary address.
