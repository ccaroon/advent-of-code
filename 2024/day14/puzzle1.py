#!/usr/bin/env python
import argparse
import pprint

from robot_security import RobotSecurity

def main(input_file:str, **kwargs) -> None:
    """Day 14 // Puzzle 02"""

    seconds = kwargs.get("seconds")

    rs = RobotSecurity(input_file)
    # print(rs)

    for _ in range(seconds):
        rs.tick()
        # print(rs)

    # print(rs)
    factor = rs.safety_factor()

    # pprint.pprint(rs.robots)

    print(f"""{main.__doc__}
-> Input File: {input_file}
-> Robot Count: {len(rs.robots)}
-> Seconds: {seconds}
-> Safety Factor: {factor}
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
