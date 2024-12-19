#!/usr/bin/env python
import argparse
import pprint

def main(args) -> None:
    """Day 18 // Puzzle 01"""

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default=None
    )
    args = parser.parse_args()

    main(args)
