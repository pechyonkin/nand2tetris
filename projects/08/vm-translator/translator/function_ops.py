"""Function ops: function, call, return."""
from typing import List

from translator.stack_ops import push_to_stack


def function_op(line: str, fname: str, line_num: int) -> List[str]:
    """Generate assembly for function vm command."""
    asm: List[str] = []
    words = line.split(" ")
    assert len(words) == 3, f"Function command {line} must have exactly 3 words"
    fname, nvars = words[1], int(words[2])
    # Declare function as label in assembly
    asm += [f"({fname})"]
    # Push 0 to stack nvars times
    for _ in range(nvars):
        # Store 0 in D, then push it to stack
        asm += ["D = 0"] + push_to_stack()
    return asm
