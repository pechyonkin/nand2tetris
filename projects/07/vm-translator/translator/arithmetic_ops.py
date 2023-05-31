from typing import List, Optional

from translator.stack_ops import pop_from_stack, push_to_stack


def jump_op(
    jump_type: str,
    line_num: int,
    fname: str,
) -> List[str]:
    true_label = f"TRUE_THEN_JUMP.{fname}.{line_num}"
    false_label = f"FALSE_THEN_DONT_JUMP.{fname}.{line_num}"
    asm = [
        f"@{true_label}",
        f"D; {jump_type}",
        "D = 0",
        f"@{false_label}",
        "0; JMP",
        f"({true_label})",
        # True result should produce -1 (which is all 1s in 2's complement
        # http://nand2tetris-questions-and-answers-forum.52.s1.nabble.com/Logical-operations-tp72625p73856.html
        "D = -1",
        f"({false_label})",
    ]
    return asm


def arithmetic_op(
    operator: str,
    fname: str,
    line_num: int,
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
            line_num=line_num,
            fname=fname,
        )
    asm += push_to_stack()  # push D onto stack
    return asm


def unary_arithmetic_op(
    operator: str,
) -> List[str]:
    """Return assembly to perform unary arithmetic operation on D and store
    result in D."""
    asm = (
        pop_from_stack(store_in_d=True)  # store the operand in D
        + [f"D = {operator} D"]  # perform the operation
        + push_to_stack()  # push D onto stack
    )
    return asm


def not_op(fname: str, line_num: int) -> List[str]:
    return unary_arithmetic_op(operator="!")


def neg_op(fname: str, line_num: int) -> List[str]:
    return unary_arithmetic_op(operator="-")


def add(fname: str, line_num: int) -> List[str]:
    """Calculate A + B by pupping two operands from stack, performing addition,
    and pushing the result onto the stack."""
    asm = arithmetic_op(
        operator="+",
        fname=fname,
        line_num=line_num,
    )  # add 1st and 2nd operands, store in D
    return asm


def sub(fname: str, line_num: int) -> List[str]:
    """Calculate A - B by pupping two operands from stack, performing
    subtraction, and pushing the result onto the stack."""
    asm = arithmetic_op(
        operator="-",
        fname=fname,
        line_num=line_num,
    )  # add 1st and 2nd operands, store in D
    return asm


def or_op(fname: str, line_num: int) -> List[str]:
    """Calculate bitwise A or B by pupping two operands from stack, performing
    bitwise or, and pushing the result onto the stack."""
    return arithmetic_op(
        operator="|",
        fname=fname,
        line_num=line_num,
    )


def and_op(fname: str, line_num: int) -> List[str]:
    """Calculate bitwise A and B by pupping two operands from stack, performing
    bitwise or, and pushing the result onto the stack."""
    return arithmetic_op(
        operator="&",
        fname=fname,
        line_num=line_num,
    )


def eq(fname: str, line_num: int) -> List[str]:
    """Calculate A eq B and push -1 onto the stack if they are equal, and 0
    otherwise."""
    return arithmetic_op(
        operator="-",
        fname=fname,
        line_num=line_num,
        jump_type="JEQ",
    )


def lt(fname: str, line_num: int) -> List[str]:
    """Calculate A lt B and push -1 onto the stack if true, and 0 if false."""
    return arithmetic_op(
        operator="-",
        fname=fname,
        line_num=line_num,
        jump_type="JLT",
    )


def gt(fname: str, line_num: int) -> List[str]:
    """Calculate A gt B and push -1 onto the stack if true, and 0 if false."""
    return arithmetic_op(
        operator="-",
        fname=fname,
        line_num=line_num,
        jump_type="JGT",
    )
