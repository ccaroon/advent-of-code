#!/usr/bin/env python
import argparse
import pprint

from towel_o_matic import TowelOMatic

def main(args) -> None:
    """Day 19 // Puzzle 01"""

    omatic = TowelOMatic(args.input_file, debug=args.debug)

    # print(omatic.towels)
    # print(omatic.designs)

    count = omatic.analyze()

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> Towels: {len(omatic.towels)}
-> Designs: {len(omatic.designs)}
-> Possible Designs: {count}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./towel.lst"
    )
    parser.add_argument("--debug", action="store_true", default=False)
    args = parser.parse_args()

    main(args)
