#!/usr/bin/env python
import argparse
import pprint

from robot_security import RobotSecurity

def main(input_file:str, **kwargs) -> None:
    """Day 14 // Puzzle 02"""

    max_secs = kwargs.get("seconds")

    rs = RobotSecurity(input_file)

    # Run for max of `max_secs` looking for the easter egg,
    # if not found exit anyway.
    tick_count = 0
    while not rs.easter_egg() and tick_count < max_secs:
        rs.tick()
        tick_count += 1
        if tick_count % 100 == 0:
            print(f"Tick Count: {tick_count}\r", end="")

    print(rs)

    print(f"""{main.__doc__}
-> Input File: {input_file}
-> Robot Count: {len(rs.robots)}
-> Seconds: {tick_count}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./robot.dat"
    )
    parser.add_argument("--secs", type=int, default=100, help="Elapsed Time in Seconds")
    args = parser.parse_args()

    main(args.input_file, seconds=args.secs)
