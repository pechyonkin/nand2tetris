from enum import Enum


class VMCommandType(Enum):
    # Type of VM code line
    PUSH = 1
    POP = 2
    ARITHMETIC = 3


class SegmentType(Enum):
    LOCAL = 1
    ARGUMENT = 2
    THIS = 3
    THAT = 4
    CONSTANT = 5
    STATIC = 6
    POINTER = 7
    TEMP = 8


SEGMENT_MAP = {
    "local": SegmentType.LOCAL,
    "argument": SegmentType.ARGUMENT,
    "this": SegmentType.THIS,
    "that": SegmentType.THAT,
    "constant": SegmentType.CONSTANT,
    "static": SegmentType.STATIC,
    "pointer": SegmentType.POINTER,
    "temp": SegmentType.TEMP,
}
