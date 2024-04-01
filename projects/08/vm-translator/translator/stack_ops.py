from typing import List


def pop_from_stack(store_in_d: bool = True) -> List[str]:
    """Return assembly to pop the value from top of stack and optionally store
    in register D. Popping is done via decrementing stack pointer SP by 1 and
    setting address register A to point to the decremented value of stack
    pointer. So, after pop is done, SP essentially points at the popped value,
    so the value can be accessed by calling register M.

    By default, this will also store the value in register D.

    :param store_in_d: whether to store in register D.
    :return: list of assembly commands to achieve "pop from stack" operation.
    """
    asm = [
        "@SP",
        "M = M - 1",
        "A = M",
    ]
    if store_in_d:
        asm.append("D = M")
    return asm


def push_reg_d_to_stack() -> List[str]:
    """Return assembly to push the value contained in register D to stack.

    SP is incremented after the push to D.

    :return: list of assembly commands to achieve "push to stack" operation.
    """
    asm = [
        "@SP",
        "A = M",
        "M = D",
        "@SP",
        "M = M + 1",
    ]
    return asm
