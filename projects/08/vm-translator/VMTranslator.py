import argparse
from pathlib import Path

from translator.parser import process_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process files.")
    parser.add_argument("file_paths", nargs="+", help="File paths to process")

    args = parser.parse_args()

    print("VMTranslator has launched!\n")

    for path in args.file_paths:
        path = Path(path)
        print(f"Processing {path}: ")

        # TODO check and process if input is a directory
        # currently, it assumes the input is a valid filename
        """
        Input: a fileName.vm : the name of a single source file, or
        a directoryName: the name of a directory containing one or more .vm source files

        Output: a fileName.asm file, or
        a directoryName.asm file
        """
        if path.exists():
            process_file(path=path)
            print("\tDone processing!\n")
        else:
            print(f"\tFile `{path}` doesn't exist! Skipping...\n")
