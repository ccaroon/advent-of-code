#!/usr/bin/env python
import argparse

from claw_machine import ClawMachine

def main(input_file:str, **kwargs) -> None:
    """Day 13 // Puzzle 02"""
    machines = ClawMachine.create(input_file, correct_units=True)

    prizes = []
    tokens = 0
    for mid, mch in enumerate(machines):
        (a, b) = mch.reverse_engineer()
        prize = mch.run_hack(a, b)
        # print(f"Machine #{mid+1}: {prize}")
        if prize:
            tokens += (a*3) + (b*1)
            prizes.append(prize)


    print(f"""{main.__doc__}
-> Input File: {input_file}
-> Machines: {len(machines)}
-> Tokens Used: {tokens}
-> Prized Won: {len(prizes)}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./claw-machine.dat"
    )
    args = parser.parse_args()

    main(args.input_file)
