"""
Methods for converting VM code to assembly instructions.
"""
from typing import List, Optional

from translator.enums import SegmentType, SEGMENT_TYPE_TO_LABEL_MAP


TEMP_SEGMENT_BASE_ADDRESS = "5"


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


def validate_offset_segment(segment_type: SegmentType) -> None:
    """Validate segment type is one of supported segments, raise otherwise."""
    msg = f"Segment type {segment_type.name} is not supported!"
    assert segment_type in (
        SegmentType.LOCAL,
        SegmentType.ARGUMENT,
        SegmentType.THIS,
        SegmentType.THAT,
        SegmentType.TEMP,
    ), msg


def push_offset(segment_type: SegmentType, index: str) -> List[str]:
    """Implement assembly for `push <segment> i` where `i` represents an offset
    from the segment's base address stored at @segment_label in RAM.

    Where <segment> is one of ("local", "argument", "this", "that", "temp")

    Take value at index i in <segment> and push it onto the stack.

    :param segment_type: only LOCAL, ARGUMENT, THIS, THAT are supported
    :param index: index at which to get the value from the segment
    :return: list of assembly lines to achieve this operation
    """
    validate_offset_segment(segment_type=segment_type)
    segment = SEGMENT_TYPE_TO_LABEL_MAP[segment_type]
    asm = [
        f"@{index}",
        "D = A",  # store i in D
        f"@{segment}",
        # calculate target address = <segment> + i and select that address
        f"AD = D + {'A' if segment_type == SegmentType.TEMP else 'M'}",
        "D = M",  # store value from the selected address in D
    ] + push_to_stack()  # push the value in D onto stack and increment SP
    return asm


def pop_offset(segment_type: SegmentType, index: str) -> List[str]:
    """Implement assembly for `pop <segment> i` where `i` represents an offset
    from the segment's base address stored at @segment_label in RAM.

    Where <segment> is one of ("local", "argument", "this", "that", "temp")

    Pop value from the stack and store it at index i in <segment>.

    :param segment_type: only LOCAL, ARGUMENT, THIS, THAT are supported
    :param index: index at which to get the value from the segment
    :return: list of assembly lines to achieve this operation
    """
    validate_offset_segment(segment_type=segment_type)
    segment = SEGMENT_TYPE_TO_LABEL_MAP[segment_type]
    asm = pop_from_stack() + [  # stores popped value in D
        "@13",
        "M = D",  # store popped value in R13
        f"@{index}",
        "D = A",  # store i in D
        f"@{segment}",
        # calculate target address = <segment> + i
        f"AD = D + {'A' if segment_type == SegmentType.TEMP else 'M'}",
        "@14",
        "M = D",  # store target address in R14
        "@13",
        "D = M",  # load popped value from R13 into D
        "@14",
        "A = M",  # select target address stored in R14
        "M = D",  # load popped value from D into the selected address
    ]
    return asm


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
