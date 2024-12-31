#!/usr/bin/env python
import argparse
import pprint

from ram import RAM

def main(args) -> None:
    """Day 18 // Part 01"""

    ram = RAM(args.input_file)
    ram.simulate_byte_fall(args.ticks, visual=args.visual)
    steps = ram.make_a_run_for_it()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> MemSpaceSize: ({ram.mem_width},{ram.mem_height})
-> Ticks: {args.ticks}/{ram.byte_count}
-> Steps: {steps}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./bytes.dat"
    )
    parser.add_argument("--ticks", "-t",
        type=int, default=10, help="Tick off X Nanoseconds")
    parser.add_argument("--visual", choices=("auto","manual"), default=None)
    args = parser.parse_args()

    main(args)
