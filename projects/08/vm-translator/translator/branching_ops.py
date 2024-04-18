from typing import List

from translator.label_ops import get_label
from translator.stack_ops import pop_from_stack


def goto_op(
    line: str,
    fname: str,
    line_num: int,
    cur_func: str,
) -> List[str]:
    """Generate assembly for goto op."""
    label = get_label(line=line)
    # store label in A and then jump to that label unconditionally
    asm: List[str] = [f"@{cur_func}${label}", "0;JMP"]
    return asm


def if_goto_op(
    line: str,
    fname: str,
    line_num: int,
    cur_func: str,
) -> List[str]:
    """Generate assembly for if-goto op."""
    label = get_label(line=line)
    asm: List[str] = pop_from_stack() + [  # pop the value from stack into D reg
        # store the label in A reg
        f"@{cur_func}${label}",
        # only jump to the label if value in D is not zero (if 'cond' is true)
        "D;JNE",
    ]
    return asm
