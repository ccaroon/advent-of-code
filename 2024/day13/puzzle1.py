#!/usr/bin/env python
import argparse

from claw_machine import ClawMachine

def main(input_file:str, **kwargs) -> None:
    """Day 13 // Puzzle 01"""

    tokens_used = 0
    prize_count = 0

    machines = ClawMachine.create(input_file)

    m = machines[0]
    print(m)
    # prize = m.run_hack(80, 40)
    # print(prize)

    m.reverse_engineer()


    # for mch in machines:
    #     print(mch)
        # a_pushes, b_pushes = mch.reverse_engineer()
        # tokens_used = a_pushes*3 + b_pushes*1
        # prize = mch.run_hack(a_pushes, b_pushes)
        # if prize:
        #     prize_count += 1


    print(f"""{main.__doc__}
-> Input File: {input_file}
-> Machines: {len(machines)}
-> Tokens Used: {tokens_used}:
-> Prized Won: {prize_count}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./claw-machine.dat"
    )
    args = parser.parse_args()

    main(args.input_file)
