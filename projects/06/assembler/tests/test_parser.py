import pytest

from assembler.parser import get_line_type, LineType, parse_c_instruction


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
