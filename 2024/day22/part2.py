#!/usr/bin/env python
import argparse
import pprint

from monkey_market import MonkeyMarket

def main(args) -> None:
    """Day 22 // Part 02"""

    mm = MonkeyMarket(args.input_file)
    total = mm.hack()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> Secret Numbers: {mm.secret_number_count}
-> 2000th Sum: {total}
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./secret-numbers.txt"
    )
    args = parser.parse_args()

    main(args)
