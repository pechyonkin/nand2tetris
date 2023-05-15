from pathlib import Path

import pytest

from translator.enums import VMCommandType, SegmentType
from translator.parser import load_vm_lines, get_command_type, VMCommand

TEST_PATH_1 = Path("../MemoryAccess/BasicTest/BasicTest.vm")

EXP_LINES_1 = [
    "push constant 10",
    "pop local 0",
    "push constant 21",
    "push constant 22",
    "pop argument 2",
    "pop argument 1",
    "push constant 36",
    "pop this 6",
    "push constant 42",
    "push constant 45",
    "pop that 5",
    "pop that 2",
    "push constant 510",
    "pop temp 6",
    "push local 0",
    "push that 5",
    "add",
    "push argument 1",
    "sub",
    "push this 6",
    "push this 6",
    "add",
    "sub",
    "push temp 6",
    "add",
]


def test_load_vm_lines() -> None:
    lines = load_vm_lines(path=TEST_PATH_1)
    assert lines == EXP_LINES_1


@pytest.mark.parametrize(
    "line,exp_type",
    (
        ("push constant 36", VMCommandType.PUSH),
        ("pop this 6", VMCommandType.POP),
        ("push constant 42", VMCommandType.PUSH),
        ("add", VMCommandType.ARITHMETIC),
        ("sub", VMCommandType.ARITHMETIC),
    ),
)
def test_command_type(line: str, exp_type: VMCommandType) -> None:
    assert get_command_type(line) == exp_type


@pytest.mark.parametrize(
    "line,exp_type,exp_segment",
    (
        ("push constant 36", VMCommandType.PUSH, SegmentType.CONSTANT),
        ("pop this 6", VMCommandType.POP, SegmentType.THIS),
        ("push constant 42", VMCommandType.PUSH, SegmentType.CONSTANT),
        ("add", VMCommandType.ARITHMETIC, None),
        ("sub", VMCommandType.ARITHMETIC, None),
    ),
)
def test_make_vm_command(
    line: str,
    exp_type: VMCommandType,
    exp_segment: SegmentType,
) -> None:
    command = VMCommand(line=line, vm_filename="Foo.vm")
    assert command.type == exp_type
    assert command.segment == exp_segment
    assert command.command == line
