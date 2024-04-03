import argparse
from pathlib import Path

from translator.parser import process_file, process_dir

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process files.")
    parser.add_argument("file_paths", nargs="+", help="File paths to process")

    args = parser.parse_args()

    print("VMTranslator has launched!\n")

    for path in args.file_paths:
        path = Path(path)
        print(f"Processing {path}: ")

        """
        Input: a fileName.vm : the name of a single source file, or
        a directoryName: the name of a directory containing one or more .vm source files

        Output: a fileName.asm file, or
        a directoryName.asm file
        """
        if path.exists() and path.is_file():
            process_file(path=path)
            print(f"\tDone processing file '{path.absolute()}'!\n")
        elif path.exists() and path.is_dir():
            process_dir(path=path)
            print(f"\tDone processing dir '{path.absolute()}'!\n")
        else:
            print(f"\tFile `{path}` doesn't exist! Skipping...\n")
