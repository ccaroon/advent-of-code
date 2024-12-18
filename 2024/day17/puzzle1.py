#!/usr/bin/env python
import argparse
import pprint

from tri_bit_computer import TriBitComputer

def main(args) -> None:
    """Day 17 // Puzzle 01"""

    tri_pc = TriBitComputer(args.input_file, debug=args.debug)
    output = tri_pc.execute()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> Registers: {tri_pc.registers}
-> Output: {output}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./program.dump"
    )
    args = parser.add_argument("--debug", "-d", action="store_true", default=False)
    args = parser.parse_args()

    main(args)
