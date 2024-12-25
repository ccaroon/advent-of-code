#!/usr/bin/env python
import argparse
import pprint

from network_analyzer import NetworkAnalyzer

def main(args) -> None:
    """Day 23 // Part 02"""

    net = NetworkAnalyzer(args.input_file)
    passwd = net.decode_passwd()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> LAN Passwd: {passwd}
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./network.dat"
    )
    args = parser.parse_args()

    main(args)
