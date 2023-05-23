"""
Methods for converting VM code to assembly instructions.
"""
from typing import List


def pop_from_stack(store_in_d: bool = True) -> List[str]:
    """Pop the value from top of stack and optionally store in register D.
    Popping is done via decrementing stack pointer SP by 1 and setting address
    register A to point to the decremented value of stack pointer. So, after pop
    is done, SP essentially points at the popped value, so the value can be
    accessed by calling register M.

    By default, this will also store the value in register D.

    :param store_in_d: whether to store in register D.
    :return: list of assembly to achieve "pop from stack" operation.
    """
    assembly = [
        "@SP",
        "M=M-1",
        "A=M",
    ]
    if store_in_d:
        assembly.append("D=M")
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
    """Calculate A + B and put it in place of A."""
    assembly: List[str] = [
        # select register right before SP, where B is, and store B into D
        "@SP",
        "A = M - 1",
        "D = M",
        # select register SP-2, where A is stored
        "A = A - 1",
        # add B to A
        "M = M + D",
        # store memory location of A + B in register D
        "D = A",
        # update SP to point to next register after A + B
        "@SP",
        "M = D + 1",
    ]
    return assembly
