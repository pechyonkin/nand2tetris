from pathlib import Path

import pytest

from assembler.files import load_lines

PROJECT_PATH = Path("/Users/maxbrut/git/nand2tetris/projects/06")

ADD_PATH = PROJECT_PATH / "add" / "Add.asm"

EXPECTED_ADD_LINES = [
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


def test_load_lines():
    with pytest.raises(IsADirectoryError):
        load_lines(path=Path("/"))


def test_load_add():
    lines = load_lines(path=ADD_PATH)
    assert lines == EXPECTED_ADD_LINES
