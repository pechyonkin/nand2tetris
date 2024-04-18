"""Generate assembly for label, goto, if-goto commands."""
from typing import List


def get_label(line: str) -> str:
    """Extract label from a label VM command. Label is second word."""
    words = line.split(" ")
    assert len(words) == 2, f"Label command {line} must have exactly 2 words"
    return words[1]


def label_op(
    line: str,
    fname: str,
    line_num: int,
    cur_func: str,
) -> List[str]:
    """Generate assembly for label op."""
    label = get_label(line=line)
    asm: List[str] = [
        f"({cur_func}${label})",
    ]
    return asm
