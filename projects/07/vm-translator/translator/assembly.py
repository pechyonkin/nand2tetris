"""
Methods for converting VM code to assembly instructions.
"""
from typing import List, Optional


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


def push_to_stack() -> List[str]:
    """Return assembly to push the value contained in register D to stack.

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


def push_constant(value: str) -> List[str]:
    """Push a constant 'value' onto the stack."""
    asm: List[str] = [
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
    return asm


def jump_op(
    jump_type: str,
    line_number: int,
    file_name: str,
) -> List[str]:
    true_label = f"TRUE_THEN_JUMP.{file_name}.{line_number}"
    false_label = f"FALSE_THEN_DONT_JUMP.{file_name}.{line_number}"
    asm = [
        f"@{true_label}",
        f"D; {jump_type}",
        "D = 0",
        f"{false_label}",
        "0; JMP",
        f"({true_label})",
        "D = 1",
        f"{false_label}",
    ]
    return asm


def arithmetic_op(
    operator: str,
    jump_type: Optional[str] = None,
) -> List[str]:
    """Return assembly to perform binary arithmetic operation on D and M and
    store result in D."""
    asm = (
        pop_from_stack(store_in_d=True)  # store first operand in D
        + pop_from_stack(store_in_d=False)  # point to second operand by A
        + [f"D = M {operator} D"]  # perform the operation
    )
    if jump_type:
        asm += jump_op(
            jump_type=jump_type,
            # TODO move this into function arguments and remove '0' value
            line_number=0,
            # TODO move this into function arguments and remove 'TestFile' value
            file_name="TestFile",
        )
    asm += push_to_stack()  # push D onto stack
    return asm


def add() -> List[str]:
    """Calculate A + B by pupping two operands from stack, performing addition,
    and pushing the result onto the stack."""
    asm = arithmetic_op(operator="+")  # add 1st and 2nd operands, store in D
    return asm


def eq() -> List[str]:
    """Calculate A eq B and push 1 onto the stack if they are equal, and 0
    otherwise."""
    return arithmetic_op(operator="-", jump_type="JEQ")
