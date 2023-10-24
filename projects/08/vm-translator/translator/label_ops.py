"""Generate assembly for label, goto, if-goto commands."""
from typing import List
from translator.stack_ops import push_to_stack, pop_from_stack


def get_label(line: str) -> str:
    """Extract label from a label VM command. Label is second word."""
    words = line.split(" ")
    assert len(words) == 2, f"Label command {line} must only have two words!"
    return words[1]


def label_op(line: str, fname: str, line_num: int) -> List[str]:
    """Generate assembly for label op."""
    label = get_label(line=line)
    asm: List[str] = [
        f"({label})",
    ]
    return asm


def goto_op(line: str, fname: str, line_num: int) -> List[str]:
    """Generate assembly for goto op."""
    label = get_label(line=line)
    # store label in A and then jump to that label unconditionally
    asm: List[str] = [f"@{label}", "0;JMP"]
    return asm


def if_goto_op(line: str, fname: str, line_num: int) -> List[str]:
    """Generate assembly for if-goto op."""
    label = get_label(line=line)
    asm: List[str] = pop_from_stack() + [  # pop the value from stack into D reg
        # store the label in A reg
        f"@{label}",
        # only jump to the label if value in D is not zero (if 'cond' is true)
        "D;JNE",
    ]
    return asm
