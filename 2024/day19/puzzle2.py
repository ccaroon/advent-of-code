#!/usr/bin/env python
import argparse
import pprint

from tri_bit_computer import TriBitComputer

def main(args) -> None:
    """Day 17 // Puzzle 02"""

    tri_pc = TriBitComputer(args.input_file, debug=args.debug)
    # print(tri_pc.registers)

    output = None
    stdout = None
    reg_a = args.start - 1
    desired_output = str(tri_pc.program).replace(" ","")
    # print(desired_output)
    while output != desired_output and reg_a <= args.start + args.max:
        tri_pc.reset()
        # print(tri_pc.registers)

        reg_a += 1
        if reg_a % 1_000_000 == 0:
            print(f"RegA: [{reg_a}]")
        tri_pc.registers.set("A", reg_a)

        stdout = tri_pc.execute()
        output = f"[{stdout}]"
        # print(output)
        # input()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> Program: {tri_pc.program}
-> Begin/End: {args.start} / {args.start + args.max}
-> Registers: {tri_pc.registers}
-> Register A: {reg_a}
-> Output: {stdout}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./program.dump"
    )
    args = parser.add_argument("--debug", "-d", action="store_true", default=False)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--max", type=int, default=1_000_000)
    args = parser.parse_args()

    main(args)
