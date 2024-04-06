from typing import Optional, List


def jump_line(
    string: str = "",
    comment: str = "",
    label: str = "",
    set_line_number: bool = False,
    line_number: Optional[int] = None,
    set_file_name: bool = False,
    file_name: Optional[str] = None,
) -> str:
    """
    Function to write to a file.

    Args:
    string: The string to be written.
    set_line_number: A boolean to determine if the line number should be added to the string.
    comment: A string to add comments in the line.
    set_file_name: A boolean to determine if the file name should be added to the string.
    label: A string to determine the type of label to add.
    line_number: Line number to add to the string if set_line_number is True.
    file_name: The name of the file to add to the string if set_file_name is True.
    """
    ln = line_number
    set_ln = set_line_number
    fname = None
    if set_file_name:
        assert file_name
        fname = file_name.upper()
    if set_line_number:
        assert line_number
    if not set_file_name:
        result = (
            f"{string}{ln if set_ln else ''}"
            + f"{comment if not comment else '//' + comment}"
        )
    elif label == "@":
        result = (
            f"{string}.{fname}.{ln}{comment if not comment else '//' + comment}"
        )
    else:
        result = (
            f"{string}.{fname}.{ln}{comment if not comment else ')'}//{comment}"
        )
    return result


def old_jump(
    jump_type: str,
    line_number: int = 0,
    file_name: str = "",
) -> List[str]:
    """
    Function to write jump instructions.

    Args:
    jump_type: The type of jump to be performed.
    line_number: Line number to add to the string if set_line_number is True.
    file_name: The name of the file to add to the string if set_file_name is True.
    """
    assembly = [
        jump_line(
            string="@TRUE_JUMP",
            label="@",
            line_number=line_number,
            set_file_name=True,
            file_name=file_name,
        ),
        jump_line(
            string=f"D; {jump_type}\nD=0",
            line_number=line_number,
            file_name=file_name,
        ),
        jump_line(
            string="@FALSE_NO_JUMP",
            label="@",
            line_number=line_number,
            set_file_name=True,
            file_name=file_name,
        ),
        jump_line(
            string="0;JMP",
            line_number=line_number,
            file_name=file_name,
        ),
        jump_line(
            string="(TRUE_JUMP",
            label="(",
            line_number=line_number,
            set_file_name=True,
            file_name=file_name,
        ),
        jump_line(string="D=-1", line_number=line_number, file_name=file_name),
        jump_line(
            string="(FALSE_NO_JUMP",
            label="(",
            line_number=line_number,
            set_file_name=True,
            file_name=file_name,
        ),
    ]
    return assembly
