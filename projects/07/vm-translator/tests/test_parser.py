from pathlib import Path

from translator.parser import load_vm_lines
from main import PATHS_TO_PROCESS

TEST_PATH_1 = Path(
    "/Users/maxbrut/git/nand2tetris/projects/07/MemoryAccess/BasicTest/BasicTest.vm"
)

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
