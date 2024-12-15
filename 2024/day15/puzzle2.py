#!/usr/bin/env python
import argparse
import pprint

from warehouse import Warehouse

def main(input_file:str, **kwargs) -> None:
    """Day 15 // Puzzle 02"""

    whaus = Warehouse(input_file, super_size=True)
    print(whaus)
    # whaus.activate_robot()

    checksum = None
    # checksum = whaus.checksum()


    print(f"""{main.__doc__}
-> Input File: {input_file}
-> Box Count: {len(whaus.boxes)}
-> GPS Checksum: {checksum}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./warehouse.dat"
    )
    args = parser.parse_args()

    main(args.input_file)
