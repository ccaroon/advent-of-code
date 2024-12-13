#!/usr/bin/env python
import argparse

from claw_machine import ClawMachine

def main(input_file:str, **kwargs) -> None:
    """Day 13 // Puzzle 02"""

    machines = ClawMachine.create(input_file)
    for m in machines:
        print(m)

    print(f"""{main.__doc__}
-> Input File: {input_file}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./claw-machine.dat"
    )
    args = parser.parse_args()

    main(args.input_file)
