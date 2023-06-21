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

        if path.exists():
            process_file(path=path)
            print("\tDone processing!\n")
        else:
            print(f"\tFile `{path}` doesn't exist! Skipping...\n")
