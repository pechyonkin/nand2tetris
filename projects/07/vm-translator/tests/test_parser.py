from pathlib import Path

import pytest
from snapshottest.pytest import PyTestSnapshotTest  # type: ignore

from translator.assembly import eq, push_offset
from translator.enums import VMCommandType, SegmentType, TYPE_TO_SEGMENT_MAP
from translator.parser import (
    load_vm_lines,
    get_command_type,
    VMCommand,
    get_vm_filename,
    load_vm_commands,
    get_assembly_lines,
    process_file,
)

TEST_PATH_1 = Path("../MemoryAccess/BasicTest/BasicTest.vm")
SIMPLE_ADD_PATH = Path("../StackArithmetic/SimpleAdd/SimpleAdd.vm")
STACK_TEST_PATH = Path("../StackArithmetic/StackTest/StackTest.vm")

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
    assert command.command_type == exp_type
    assert command.segment_type == exp_segment
    assert command.command == line


@pytest.mark.parametrize(
    "path_str, exp_fname",
    (
        ("../MemoryAccess/BasicTest/BasicTest.vm", "BasicTest.vm"),
        ("../MemoryAccess/PointerTest/PointerTest.vm", "PointerTest.vm"),
        ("../MemoryAccess/StaticTest/StaticTest.vm", "StaticTest.vm"),
    ),
)
def test_get_vm_filename(path_str: str, exp_fname: str) -> None:
    path = Path(path_str)
    fname = get_vm_filename(path=path)
    assert fname == exp_fname


def test_load_vm_commands(snapshot: PyTestSnapshotTest) -> None:
    path = Path("../MemoryAccess/BasicTest/BasicTest.vm")
    commands = load_vm_commands(path=path)
    commands_str = [str(command) for command in commands]
    snapshot.assert_match(commands_str)


ASSEMBLY_PUSH_CONSTANT_17 = [
    "// push constant 17",
    "@17",
    "D = A",
    "@SP",
    "A = M",
    "M = D",
    "@SP",
    "M = M + 1",
]

ASSEMBLY_ADD = [
    "// add",
    # store first operand in D
    "@SP",
    "M = M - 1",
    "A = M",
    "D = M",
    # point to second operand by A
    "@SP",
    "M = M - 1",
    "A = M",
    # add first and second operands, store in D
    "D = M + D",
    # push D onto stack
    "@SP",
    "A = M",
    "M = D",
    "@SP",
    "M = M + 1",
]


def test_push_constant_assembly() -> None:
    command = VMCommand(line="push constant 17", vm_filename="Foo.vm")
    assembly = command.to_assembly(fname="Foo", line_num=0)
    assert assembly == ASSEMBLY_PUSH_CONSTANT_17


def test_add_assembly() -> None:
    command = VMCommand(line="add", vm_filename="Foo.vm")
    assembly = command.to_assembly(fname="Foo", line_num=0)
    assert assembly == ASSEMBLY_ADD


@pytest.mark.skip("Everything is now implemented!")
def test_not_implemented() -> None:
    command = VMCommand(line="not", vm_filename="Foo.vm")
    with pytest.raises(NotImplementedError):
        _ = command.to_assembly(fname="Foo", line_num=0)


@pytest.mark.parametrize(
    "path",
    (
        SIMPLE_ADD_PATH,
        STACK_TEST_PATH,
    ),
)
def test_stack_arithmetic(
    path: Path,
    snapshot: PyTestSnapshotTest,
) -> None:
    """Test the two StackArithmetic .vm files."""
    result = get_assembly_lines(path=path)
    snapshot.assert_match(result)


@pytest.mark.parametrize(
    "path",
    (
        SIMPLE_ADD_PATH,
        STACK_TEST_PATH,
    ),
)
def test_outfile_simple_add(path: Path) -> None:
    process_file(path=path)


def test_eq(snapshot: PyTestSnapshotTest) -> None:
    result = eq(fname="Foo", line_num=0)
    snapshot.assert_match(result)


def test_type_to_segment_map():
    """Test that map was reversed correctly."""
    assert TYPE_TO_SEGMENT_MAP == {
        SegmentType.LOCAL: "local",
        SegmentType.ARGUMENT: "argument",
        SegmentType.THIS: "this",
        SegmentType.THAT: "that",
        SegmentType.CONSTANT: "constant",
        SegmentType.STATIC: "static",
        SegmentType.POINTER: "pointer",
        SegmentType.TEMP: "temp",
    }


@pytest.mark.parametrize(
    "segment_type,index",
    (
        (SegmentType.LOCAL, "42"),
        (SegmentType.ARGUMENT, "1"),
        (SegmentType.THIS, "9"),
        (SegmentType.THAT, "69"),
    ),
)
def test_push_offset(
    segment_type: SegmentType,
    index: str,
    snapshot: PyTestSnapshotTest,
) -> None:
    snapshot.assert_match(push_offset(segment_type=segment_type, index=index))


@pytest.mark.parametrize(
    "segment_type,index",
    (
        (SegmentType.CONSTANT, "42"),
        (SegmentType.STATIC, "1"),
        (SegmentType.POINTER, "9"),
        (SegmentType.TEMP, "69"),
    ),
)
def test_push_offset_fails(
    segment_type: SegmentType,
    index: str,
) -> None:
    with pytest.raises(AssertionError):
        push_offset(segment_type=segment_type, index=index)
