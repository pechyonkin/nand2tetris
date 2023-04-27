import pytest

from assembler.parser import (
    get_line_type,
    LineType,
    process_lines,
    get_label_symbols_dict,
    int_to_a_instruction,
    remove_comment_after_instruction,
)

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
    assert result == {
        "OUTPUT_FIRST": 10,
        "OUTPUT_D": 12,
        "INFINITE_LOOP": 14,
    }


@pytest.mark.parametrize(
    "raw_line,clean_line",
    (
        ("D=D-M            // D = first number - second number", "D=D-M"),
        ("M=D              // M[2] = D (greatest number)", "M=D"),
        ("@R0              // M[2] = D (greatest number)", "@R0"),
    ),
)
def test_remove_comment_after_instruction(raw_line: str, clean_line: str):
    assert remove_comment_after_instruction(raw_line) == clean_line


def test_process_lines_with_symbols():
    lines = [line.lstrip().rstrip() for line in TEST_LINES_SYMBOLS_1]
    instr_lines = process_lines(lines=lines)
    assert instr_lines[0] == int_to_a_instruction(0)  # @R0
    assert instr_lines[2] == int_to_a_instruction(1)  # @R1
    assert instr_lines[4] == int_to_a_instruction(10)  # @OUTPUT_FIRST -> 10
    assert instr_lines[6] == int_to_a_instruction(1)  # @R1
    assert instr_lines[8] == int_to_a_instruction(12)  # @OUTPUT_D -> 12
    assert instr_lines[10] == int_to_a_instruction(0)  # @R0
    assert instr_lines[12] == int_to_a_instruction(2)  # @R2
    assert instr_lines[14] == int_to_a_instruction(14)  # @INFINITE_LOOP -> 14
