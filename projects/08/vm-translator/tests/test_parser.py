from pathlib import Path

import pytest
from snapshottest.pytest import PyTestSnapshotTest  # type: ignore

from translator.arithmetic_ops import eq
from translator.enums import VMCommandType, SegmentType, TYPE_TO_SEGMENT_MAP
from translator.function_ops import function_op
from translator.memory_segments import push_offset, pop_offset
from translator.parser import (
    load_vm_lines,
    get_cmd_type,
    VMCommand,
    get_vm_filename,
    load_vm_commands,
    get_file_assembly_lines,
    process_file,
    vm_commands_to_assembly,
    get_output_path,
    process_dir,
)

# Project 7
SIMPLE_ADD_PATH = Path("../../07/StackArithmetic/SimpleAdd/SimpleAdd.vm")
STACK_TEST_PATH = Path("../../07/StackArithmetic/StackTest/StackTest.vm")
BASIC_TEST_PATH = Path("../../07/MemoryAccess/BasicTest/BasicTest.vm")
STATIC_TEST_PATH = Path("../../07/MemoryAccess/StaticTest/StaticTest.vm")
POINTER_TEST_PATH = Path("../../07/MemoryAccess/PointerTest/PointerTest.vm")

# Project 8
BASIC_LOOP_PATH = Path("../../08/ProgramFlow/BasicLoop/BasicLoop.vm")
FIB_SERIES_PATH = Path("../../08/ProgramFlow/FibonacciSeries/FibonacciSeries.vm")
SIMPLE_FUNC_PATH = Path("../../08/FunctionCalls/SimpleFunction/SimpleFunction.vm")
NESTED_CALL_DIR_PATH = Path("../../08/FunctionCalls/NestedCall")
FIB_ELEM_DIR_PATH = Path("../../08/FunctionCalls/FibonacciElement")
STATICS_TEST_DIR_PATH = Path("../../08/FunctionCalls/StaticsTest")

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
    lines = load_vm_lines(path=BASIC_TEST_PATH)
    assert lines == EXP_LINES_1


@pytest.mark.parametrize(
    "line,exp_type",
    (
        ("push constant 36", VMCommandType.PUSH),
        ("pop this 6", VMCommandType.POP),
        ("push constant 42", VMCommandType.PUSH),
        ("add", VMCommandType.ARITHMETIC),
        ("sub", VMCommandType.ARITHMETIC),
        ("label NEW_LABEL", VMCommandType.LABEL),
        ("goto NEW_LABEL", VMCommandType.GOTO),
        ("if-goto NEW_LABEL", VMCommandType.IF_GOTO),
        ("function Foo.bar 3", VMCommandType.FUNCTION),
        ("call Foo.bar 2", VMCommandType.CALL),
        ("return", VMCommandType.RETURN),
    ),
)
def test_command_type(line: str, exp_type: VMCommandType) -> None:
    assert get_cmd_type(line) == exp_type


@pytest.mark.parametrize(
    "line,exp_type,exp_segment",
    (
        ("push constant 36", VMCommandType.PUSH, SegmentType.CONSTANT),
        ("pop this 6", VMCommandType.POP, SegmentType.THIS),
        ("push constant 42", VMCommandType.PUSH, SegmentType.CONSTANT),
        ("add", VMCommandType.ARITHMETIC, None),
        ("sub", VMCommandType.ARITHMETIC, None),
        ("label NEW_LABEL", VMCommandType.LABEL, None),
        ("goto NEW_LABEL", VMCommandType.GOTO, None),
        ("if-goto NEW_LABEL", VMCommandType.IF_GOTO, None),
        ("function Foo.bar 3", VMCommandType.FUNCTION, None),
        ("call Foo.bar 2", VMCommandType.CALL, None),
        ("return", VMCommandType.RETURN, None),
    ),
)
def test_make_vm_command(
    line: str,
    exp_type: VMCommandType,
    exp_segment: SegmentType,
) -> None:
    command = VMCommand(line=line, vm_filename="Foo.vm")
    assert command.cmd_type == exp_type
    assert command.segment_type == exp_segment
    assert command.command == line


@pytest.mark.parametrize(
    "path_str, exp_fname",
    (
        ("../MemoryAccess/BasicTest/BasicTest.vm", "BasicTest"),
        ("../MemoryAccess/PointerTest/PointerTest.vm", "PointerTest"),
        ("../MemoryAccess/StaticTest/StaticTest.vm", "StaticTest"),
    ),
)
def test_get_vm_filename(path_str: str, exp_fname: str) -> None:
    path = Path(path_str)
    fname = get_vm_filename(path=path)
    assert fname == exp_fname


def test_load_vm_commands(snapshot: PyTestSnapshotTest) -> None:
    path = Path("../../07/MemoryAccess/BasicTest/BasicTest.vm")
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
    assembly = command.to_assembly(line_num=0)
    assert assembly == ASSEMBLY_PUSH_CONSTANT_17


def test_add_assembly() -> None:
    command = VMCommand(line="add", vm_filename="Foo.vm")
    assembly = command.to_assembly(line_num=0)
    assert assembly == ASSEMBLY_ADD


@pytest.mark.skip("Everything is now implemented!")
def test_not_implemented() -> None:
    command = VMCommand(line="not", vm_filename="Foo.vm")
    with pytest.raises(NotImplementedError):
        _ = command.to_assembly(line_num=0)


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
    result = get_file_assembly_lines(path=path)
    snapshot.assert_match(result)


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
        (SegmentType.TEMP, "69"),
    ),
)
def test_push_offset(
    segment_type: SegmentType,
    index: str,
    snapshot: PyTestSnapshotTest,
) -> None:
    snapshot.assert_match(
        push_offset(
            segment_type=segment_type,
            index=index,
            fname="Foo",
            line_num=42,
        )
    )


@pytest.mark.parametrize(
    "segment_type,index",
    (
        (SegmentType.CONSTANT, "42"),
        (SegmentType.STATIC, "1"),
        (SegmentType.POINTER, "9"),
    ),
)
def test_push_offset_fails(
    segment_type: SegmentType,
    index: str,
) -> None:
    with pytest.raises(AssertionError):
        push_offset(
            segment_type=segment_type,
            index=index,
            fname="Foo",
            line_num=42,
        )


@pytest.mark.parametrize(
    "segment_type,index",
    (
        (SegmentType.LOCAL, "42"),
        (SegmentType.ARGUMENT, "1"),
        (SegmentType.THIS, "9"),
        (SegmentType.THAT, "69"),
        (SegmentType.TEMP, "69"),
    ),
)
def test_pop_offset(
    segment_type: SegmentType,
    index: str,
    snapshot: PyTestSnapshotTest,
) -> None:
    snapshot.assert_match(
        pop_offset(
            segment_type=segment_type,
            index=index,
            fname="Foo",
            line_num=42,
        )
    )


@pytest.mark.parametrize(
    "segment_type,index",
    (
        (SegmentType.CONSTANT, "42"),
        (SegmentType.STATIC, "1"),
        (SegmentType.POINTER, "9"),
    ),
)
def test_pop_offset_fails(
    segment_type: SegmentType,
    index: str,
) -> None:
    with pytest.raises(AssertionError):
        pop_offset(
            segment_type=segment_type,
            index=index,
            fname="Foo",
            line_num=42,
        )


@pytest.mark.parametrize(
    "path",
    (
        BASIC_TEST_PATH,
        POINTER_TEST_PATH,
        STATIC_TEST_PATH,
    ),
)
def test_to_assembly_with_offset(path: Path):
    """Test assembly generation passes for all lines except lines related to
    segments static, pointer and temp."""
    vm_lines = load_vm_commands(path=path)
    unsupported_segments = [
        SegmentType.POINTER,
    ]
    vm_lines = [
        vm_line
        for vm_line in vm_lines
        if (
            (vm_line.cmd_type in [VMCommandType.PUSH, VMCommandType.POP])
            and (vm_line.segment_type not in unsupported_segments)
        )
    ]
    _ = vm_commands_to_assembly(vm_commands=vm_lines)


def test_static(snapshot: PyTestSnapshotTest) -> None:
    vm_lines = [
        VMCommand("push static 42", "Foo"),
        VMCommand("pop static 69", "Foo"),
    ]
    asm = vm_commands_to_assembly(vm_commands=vm_lines)
    snapshot.assert_match(asm)


@pytest.mark.parametrize(
    "path",
    (
        # Project 7
        SIMPLE_ADD_PATH,
        STACK_TEST_PATH,
        BASIC_TEST_PATH,
        STATIC_TEST_PATH,
        POINTER_TEST_PATH,
        # Project 8
        BASIC_LOOP_PATH,
        FIB_SERIES_PATH,
        SIMPLE_FUNC_PATH,
        # TODO: make these work
        # NESTED_CALL_DIR_PATH,
        # FIB_ELEM_DIR_PATH,
        # STATICS_TEST_DIR_PATH,
    ),
)
def test_outfile_simple_add(path: Path) -> None:
    if path.is_file():
        process_file(path=path)
    elif path.is_dir():
        process_dir(path=path)


def test_function_op(snapshot: PyTestSnapshotTest):
    line = "function SimpleFunction.test 2"
    asm = function_op(line, "fname", 0)
    snapshot.assert_match(asm)


@pytest.mark.parametrize("path", (BASIC_LOOP_PATH, FIB_SERIES_PATH))
def test_label_ops(path: Path, snapshot: PyTestSnapshotTest):
    vm_lines = load_vm_commands(path=path)
    asm = vm_commands_to_assembly(vm_commands=vm_lines)
    snapshot.assert_match(asm)


def test_project8_paths():
    assert BASIC_LOOP_PATH.exists()
    assert FIB_SERIES_PATH.exists()
    assert SIMPLE_FUNC_PATH.exists()
    assert NESTED_CALL_DIR_PATH.exists()
    assert FIB_ELEM_DIR_PATH.exists()
    assert STATICS_TEST_DIR_PATH.exists()


@pytest.mark.parametrize(
    "path,expected_out_path",
    (
        (SIMPLE_ADD_PATH, Path("../../07/StackArithmetic/SimpleAdd/SimpleAdd.asm")),
        (
            NESTED_CALL_DIR_PATH,
            Path("../../08/FunctionCalls/NestedCall/NestedCall.asm"),
        ),
    ),
)
def test_get_output_path(path: Path, expected_out_path: Path) -> None:
    out_path = get_output_path(path)
    assert out_path == expected_out_path
