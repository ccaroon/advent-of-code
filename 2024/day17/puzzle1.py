#!/usr/bin/env python
import argparse
import pprint

from tri_bit_computer import TriBitComputer

def main(args) -> None:
    """Day 17 // Puzzle 01"""

    tri_pc = TriBitComputer(args.input_file)
    print(tri_pc)
    tri_pc.execute()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./program.dump"
    )
    args = parser.parse_args()

    main(args)
