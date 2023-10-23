from enum import Enum


class VMCommandType(Enum):
    # Type of VM code line
    PUSH = 1
    POP = 2
    ARITHMETIC = 3
    LABEL = 4
    GOTO = 5
    IF_GOTO = 6
    FUNCTION = 7
    CALL = 8
    RETURN = 9


class SegmentType(Enum):
    LOCAL = 1
    ARGUMENT = 2
    THIS = 3
    THAT = 4
    CONSTANT = 5
    STATIC = 6
    POINTER = 7
    TEMP = 8


SEGMENT_TO_TYPE_MAP = {
    "local": SegmentType.LOCAL,
    "argument": SegmentType.ARGUMENT,
    "this": SegmentType.THIS,
    "that": SegmentType.THAT,
    "constant": SegmentType.CONSTANT,
    "static": SegmentType.STATIC,
    "pointer": SegmentType.POINTER,
    "temp": SegmentType.TEMP,
}

# .values() and .keys() are returned in insertion order, so this correctly
# reverses the map from (key: value) to (value: key)
# https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
TYPE_TO_SEGMENT_MAP = dict(
    zip(SEGMENT_TO_TYPE_MAP.values(), SEGMENT_TO_TYPE_MAP.keys())
)


SEGMENT_TYPE_TO_LABEL_MAP = {
    SegmentType.LOCAL: "LCL",
    SegmentType.ARGUMENT: "ARG",
    SegmentType.THIS: "THIS",
    SegmentType.THAT: "THAT",
    SegmentType.TEMP: "5",  # not label but base address of the temp segment
    # SegmentType.CONSTANT: "",
    # SegmentType.STATIC: "",
    # SegmentType.POINTER: "",
}
