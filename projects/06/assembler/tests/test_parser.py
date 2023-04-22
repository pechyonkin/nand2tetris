import pytest
from snapshottest import snapshot

from assembler.parser import (
    get_line_type,
    LineType,
    parse_c_instruction,
    parse_a_instruction,
    AInstruction,
    process_file,
    process_lines,
)
from main import PATHS_TO_PROCESS


TEST_LINES_NO_SYMBOLS_1 = [
    "// This file is part of www.nand2tetris.org",
    '// and the book "The Elements of Computing Systems"',
    "// by Nisan and Schocken, MIT Press.",
    "// File name: projects/06/add/Add.asm",
    "",
    "// Computes R0 = 2 + 3  (R0 refers to RAM[0])",
    "",
    "@2",
    "D=A",
    "@3",
    "D=D+A",
    "@0",
    "M=D",
]

TEST_LINES_NO_SYMBOLS_1_EXP = [
    "0000000000000010\n",
    "1110110000010000\n",
    "0000000000000011\n",
    "1110000010010000\n",
    "0000000000000000\n",
    "1110001100001000\n",
]


@pytest.mark.parametrize(
    "line,expected_line_type",
    [
        ("// This file is part of www.nand2tetris.org", LineType.COMMENT_LINE),
        ('// and the book "The Elements of Computing Systems"', LineType.COMMENT_LINE),
        ("// by Nisan and Schocken, MIT Press.", LineType.COMMENT_LINE),
        ("// File name: projects/06/add/Add.asm", LineType.COMMENT_LINE),
        ("", LineType.EMPTY_LINE),
        ("// Computes R0 = 2 + 3  (R0 refers to RAM[0])", LineType.COMMENT_LINE),
        ("@2", LineType.A_INSTRUCTION),
        ("D=A", LineType.C_INSTRUCTION),
        ("@3", LineType.A_INSTRUCTION),
        ("D=D+A", LineType.C_INSTRUCTION),
        ("@0", LineType.A_INSTRUCTION),
        ("M=D", LineType.C_INSTRUCTION),
    ],
)
def test_get_line_type(line: str, expected_line_type: LineType) -> None:
    assert get_line_type(line=line) == expected_line_type


@pytest.mark.parametrize(
    "line,exp_dest,exp_comp,exp_jump",
    [
        ("D", "", "D", ""),
        ("D=A", "D", "A", ""),
        ("D=D+A", "D", "D+A", ""),
        ("M=D", "M", "D", ""),
        ("0;JMP", "", "0", "JMP"),
        ("D-1;JEQ", "", "D-1", "JEQ"),
        ("AMD=D-1;JEQ", "AMD", "D-1", "JEQ"),
    ],
)
def test_parse_c_instruction(
    line: str, exp_comp: str, exp_dest: str, exp_jump: str
) -> None:
    print("START THIS!!! " * 7)
    print(f"LINE: {line}")
    instr = parse_c_instruction(line=line)
    assert instr.dest == exp_dest
    assert instr.comp == exp_comp
    assert instr.jump == exp_jump


@pytest.mark.parametrize(
    "line, expected_instruction",
    [
        ("@0", "0000000000000000"),
        ("@1", "0000000000000001"),
        ("@10", "0000000000001010"),
        ("@32767", "0111111111111111"),
    ],
)
def test_parse_a_instruction(line, expected_instruction):
    assert len(expected_instruction) == 16
    instruction = parse_a_instruction(line)
    assert isinstance(instruction, AInstruction)
    assert instruction.make_machine_instruction() == expected_instruction


def test_process_lines():
    instr_lines = process_lines(lines=TEST_LINES_NO_SYMBOLS_1)
    assert instr_lines == TEST_LINES_NO_SYMBOLS_1_EXP


@pytest.mark.skip("Don't process files for now.")
def test_process_file():
    print("THIS! " * 42)
    for path in PATHS_TO_PROCESS:
        process_file(path_to_file=path)
