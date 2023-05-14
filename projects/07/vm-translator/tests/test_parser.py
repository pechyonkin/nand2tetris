from pathlib import Path

from translator.parser import load_vm_lines
from main import PATHS_TO_PROCESS


def test_load_vm_lines() -> None:
    lines = load_vm_lines(path=Path(PATHS_TO_PROCESS[0]))
    assert lines == []
