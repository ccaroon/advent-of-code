#!/usr/bin/env python
import argparse
import pprint

from lock_smith import LockSmith

def main(args) -> None:
    """Day 25 // Part 02"""

    smith = LockSmith(args.input_file)
    count = smith.count_key_lock_pairs()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> Key/Lock Fits: {count}
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./lock-and-key.scm"
    )
    args = parser.parse_args()

    main(args)
