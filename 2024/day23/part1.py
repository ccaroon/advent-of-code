#!/usr/bin/env python
import argparse
import pprint

from network_analyzer import NetworkAnalyzer

def main(args) -> None:
    """Day 23 // Part 01"""

    net = NetworkAnalyzer(args.input_file)
    count = net.analyze()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
->T-Count: {count}
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./network.dat"
    )
    args = parser.parse_args()

    main(args)
