#!/usr/bin/env python
import argparse
import pprint

from remote_control import RemoteControl

def main(args) -> None:
    """Day 21 // Puzzle 02"""

    rc = RemoteControl(args.input_file)
    # rc.systems_test()
    # rc.enter_codes()
    rc.manual_mode()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> Remote: {rc}
-> Codes: {rc.codes}
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./door-codes.txt"
    )
    args = parser.parse_args()

    main(args)
