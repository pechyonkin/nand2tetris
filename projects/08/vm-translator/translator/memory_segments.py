from typing import List

from translator.stack_ops import push_reg_d_to_stack, pop_from_stack
from translator.enums import SegmentType, SEGMENT_TYPE_TO_LABEL_MAP

TEMP_SEGMENT_BASE_ADDRESS = "5"


def push_constant(
    value: str,
    fname: str,
    line_num: int,
) -> List[str]:
    """Push a constant 'value' onto the stack."""
    del fname, line_num  # unused
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


def push_offset(
    segment_type: SegmentType,
    index: str,
    fname: str,
    line_num: int,
) -> List[str]:
    """Implement assembly for `push <segment> i` where `i` represents an offset
    from the segment's base address stored at @segment_label in RAM.

    Where <segment> is one of ("local", "argument", "this", "that", "temp")

    Take value at index i in <segment> and push it onto the stack.

    :param segment_type: only LOCAL, ARGUMENT, THIS, THAT are supported
    :param index: index at which to get the value from the segment
    :param line_num: unused
    :param fname: unused
    :return: list of assembly lines to achieve this operation
    """
    del fname, line_num  # unused
    validate_offset_segment(segment_type=segment_type)
    segment = SEGMENT_TYPE_TO_LABEL_MAP[segment_type]
    asm = [
        f"@{index}",
        "D = A",  # store i in D
        f"@{segment}",
        # calculate target address = <segment> + i and select that address
        f"AD = D + {'A' if segment_type == SegmentType.TEMP else 'M'}",
        "D = M",  # store value from the selected address in D
    ] + push_reg_d_to_stack()
    return asm


def pop_offset(
    segment_type: SegmentType,
    index: str,
    fname: str,
    line_num: int,
) -> List[str]:
    """Implement assembly for `pop <segment> i` where `i` represents an offset
    from the segment's base address stored at @segment_label in RAM.

    Where <segment> is one of ("local", "argument", "this", "that", "temp")

    Pop value from the stack and store it at index i in <segment>.

    :param segment_type: only LOCAL, ARGUMENT, THIS, THAT are supported
    :param index: index at which to get the value from the segment
    :param line_num: unused
    :param fname: unused
    :return: list of assembly lines to achieve this operation
    """
    del fname, line_num  # unused
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


def push_static(index: str, fname: str, line_num: int) -> List[str]:
    del line_num  # unused
    asm = [
        f"@{fname}.{index}",
        "D = M",
    ] + push_reg_d_to_stack()
    return asm


def pop_static(index: str, fname: str, line_num: int) -> List[str]:
    del line_num  # unused
    asm = pop_from_stack() + [  # pop from stack and store in D
        f"@{fname}.{index}",
        "M = D",
    ]
    return asm


def push_pointer(index: str, fname: str, line_num: int) -> List[str]:
    """Get base address of THIS or THAT and push it onto stack."""
    assert index in ["0", "1"]
    label = "THIS" if index == "0" else "THAT"
    asm = [
        f"@{label}",
        "D = M",
    ] + push_reg_d_to_stack()
    return asm


def pop_pointer(index: str, fname: str, line_num: int) -> List[str]:
    """Pop value from stack and store it as base address of THIS or THAT."""
    assert index in ["0", "1"]
    label = "THIS" if index == "0" else "THAT"
    asm = pop_from_stack() + [
        f"@{label}",
        "M = D",
    ]
    return asm
