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
    get_label_symbols_dict,
)
from main import PATHS_TO_PROCESS


TEST_LINES_SYMBOLS_1 = [
    "// This file is part of www.nand2tetris.org",
    '// and the book "The Elements of Computing Systems"',
    "// by Nisan and Schocken, MIT Press.",
    "// File name: projects/06/max/Max.asm",
    "",
    "// Computes R2 = max(R0, R1)  (R0,R1,R2 refer to RAM[0],RAM[1],RAM[2])",
    "",
    "   @R0",
    "   D=M              // D = first number",
    "   @R1",
    "   D=D-M            // D = first number - second number",
    "   @OUTPUT_FIRST",
    "   D;JGT            // if D>0 (first is greater) goto output_first",
    "   @R1",
    "   D=M              // D = second number",
    "   @OUTPUT_D",
    "   0;JMP            // goto output_d",
    "// Some other comment here",
    "(OUTPUT_FIRST)",
    "   @R0             ",
    "   D=M              // D = first number",
    "(OUTPUT_D)",
    "   @R2",
    "   M=D              // M[2] = D (greatest number)",
    "(INFINITE_LOOP)",
    "   @INFINITE_LOOP",
    "   0;JMP            // infinite loop",
]

TEST_LINES_NO_SYMBOLS_1_EXP = []


@pytest.mark.parametrize(
    "line,expected_line_type",
    [
        ("(OUTPUT_FIRST)", LineType.LABEL_SYMBOL),
    ],
)
def test_get_symbol_line_type(line: str, expected_line_type: LineType) -> None:
    assert get_line_type(line=line) == expected_line_type


def test_get_label_symbols():
    result = get_label_symbols_dict(lines=TEST_LINES_SYMBOLS_1)
    print("RESULT!!! " * 42)
    print(result)
    assert result == {
        "OUTPUT_FIRST": 10,
        "OUTPUT_D": 12,
        "INFINITE_LOOP": 14,
    }
