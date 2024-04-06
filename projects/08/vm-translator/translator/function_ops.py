"""Function ops: function, call, return."""
from typing import List, NamedTuple, Optional

from translator.stack_ops import push_reg_d_to_stack, pop_from_stack


class ParsedFunctionLine(NamedTuple):
    filename: str
    func_name: str
    nvars: int

    @property
    def full_function_name(self) -> str:
        return f"{self.filename}.{self.func_name}"


def parse_function_line(line: str) -> ParsedFunctionLine:
    words = line.split(" ")
    assert len(words) == 3, f"Function command {line} must have exactly 3 words"
    assert words[0] == "function", f"First line should be `function`"
    filename, func_name = words[1].split(".")
    return ParsedFunctionLine(
        filename=filename,
        func_name=func_name,
        nvars=int(words[2]),
    )


def function_op(line: str, fname: str, line_num: int) -> List[str]:
    """Generate assembly for function vm command."""
    asm: List[str] = []
    parsed_func_line = parse_function_line(line=line)
    func_name = parsed_func_line.full_function_name
    nvars = parsed_func_line.nvars
    # Declare function as label in assembly
    asm += [f"({func_name})"]
    # Push 0 to stack nvars times
    for _ in range(nvars):
        # Store 0 in D, then push it to stack
        asm += ["D = 0"] + push_reg_d_to_stack()
    return asm


def _end_frame_minus(offset: int, eof: str) -> List[str]:
    """Return assembly for getting value at memory address of end of frame minus
    given offset and storing it in register D."""
    return [
        f"@{eof}",
        "D = M",
        f"@{offset}",
        "D = D - A",  # register address of `eof - offset`
        "A = D",  # select register at `eof - offset`
        "D = M",  # store value from that register in D
    ]


def return_op(line: str, fname: str, line_num: int) -> List[str]:
    """Generate assembly for `return` command."""
    # TODO add tests for this
    asm: List[str] = []
    # store the end of function frame in R13, end of frame is LCL
    eof = "R13"  # end of frame
    ret_addr = "R14"
    asm += [
        "@LCL",
        "D = M",
        f"@{eof}",
        "M = D",
    ]
    # store return address in R14, return address is at end frame - 5
    asm += _end_frame_minus(offset=5, eof=eof) + [
        f"@{ret_addr}",
        "M = D",
    ]
    # pop return value into D register
    asm += pop_from_stack()
    # store return value into memory pointed at by ARG
    asm += [
        "@ARG",
        "A = M",  # select register pointed to by ARG
        "M = D",
    ]
    # reposition SP olf caller to ARG + 1
    asm += [
        "@ARG",
        "D = M",
        "@SP",
        "M = D + 1",
    ]
    # TODO refactor the below
    # set THAT = *(eof - 1)
    asm += _end_frame_minus(offset=1, eof=eof) + [
        "@THAT",
        "M = D",
    ]
    # set THIS = *(eof - 2)
    asm += _end_frame_minus(offset=2, eof=eof) + [
        "@THIS",
        "M = D",
    ]
    # set ARG = *(eof - 3)
    asm += _end_frame_minus(offset=3, eof=eof) + [
        "@ARG",
        "M = D",
    ]
    # set LCL = *(eof - 4)
    asm += _end_frame_minus(offset=4, eof=eof) + [
        "@LCL",
        "M = D",
    ]
    # goto return address
    asm += [
        f"@{ret_addr}",
        "A = M",
        "0;JMP",
    ]

    return asm


def call_op(
    line: str,
    fname: str,
    line_num: int,
    cur_function: str,
    return_counter: Optional[int],
) -> List[str]:
    assert return_counter, "Call command must have a return counter!"
    asm: List[str] = []
    # TODO: implement
    return asm
