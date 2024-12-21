#!/usr/bin/env python
import argparse
import pprint

from keycoder import KeyCoder

def main(args) -> None:
    """Day 21 // Puzzle 01"""

    coder = KeyCoder(args.input_file)
    coder.encode()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> Codes: {coder.codes}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./door-codes.txt"
    )
    args = parser.parse_args()

    main(args)
