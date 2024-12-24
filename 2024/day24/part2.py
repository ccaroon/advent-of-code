#!/usr/bin/env python
import argparse
import pprint

from fruit_monitor import FruitMonitor

def main(args) -> None:
    """Day 24 // Part 02"""

    fm = FruitMonitor(args.input_file)
    result = fm.simulate()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> Result: {result}
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./gates.dat"
    )
    args = parser.parse_args()

    main(args)
