#!/usr/bin/env python
import argparse
import pprint

from ram import RAM

def main(args) -> None:
    """Day 18 // Part 01"""

    ram = RAM(args.input_file)
    ram.simulate_byte_fall(args.ticks)

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./bytes.dat"
    )
    parser.add_argument("--ticks", "-t", type=int, default=10, help="Tick off X Nanoseconds")
    args = parser.parse_args()

    main(args)
