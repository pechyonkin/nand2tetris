from pathlib import Path

from assembler.parser import process_file


FILES_TO_PROCESS = [
    "/Users/maxbrut/git/nand2tetris/projects/06/add/Add.asm",
    "/Users/maxbrut/git/nand2tetris/projects/06/pong/PongL.asm",
    "/Users/maxbrut/git/nand2tetris/projects/06/pong/Pong.asm",
]

PATHS_TO_PROCESS = [Path(f) for f in FILES_TO_PROCESS]


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    for path in PATHS_TO_PROCESS:
        process_file(path_to_file=path)
