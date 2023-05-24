"""
Methods for converting VM code to assembly instructions.
"""
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
    assembly = [
        "@SP",
        "M = M - 1",
        "A = M",
    ]
    if store_in_d:
        assembly.append("D = M")
    return assembly


def push_to_stack() -> List[str]:
    """Return assembly to push the value contained in register D to stack.

    :return: list of assembly commands to achieve "push to stack" operation.
    """
    assembly = [
        "@SP",
        "A = M",
        "M = D",
        "@SP",
        "M = M + 1",
    ]
    return assembly


def push_constant(value: str) -> List[str]:
    """Push a constant 'value' onto the stack."""
    assembly: List[str] = [
        # D = value
        f"@{value}",
        "D = A",
        # *SP = value
        "@SP",
        "A = M",
        "M = D",
        # SP += 1
        "@SP",
        "M = M + 1",
    ]
    return assembly


def add() -> List[str]:
    """Calculate A + B by pupping two operands from stack, performing addition,
    and pushing the result onto the stack."""
    assembly = (
        pop_from_stack(store_in_d=True)  # store first operand in D
        + pop_from_stack(store_in_d=False)  # point to second operand by A
        + ["D = M + D"]  # add first and second operands, store in D
        + push_to_stack()  # push D onto stack
    )
    return assembly
