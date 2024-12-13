#!/usr/bin/env python
import argparse

from garden import Garden

def main(input_file:str, **kwargs) -> None:
    """Day 12 // Puzzle 01"""

    garden = Garden(input_file)
    fencing_cost = garden.calculate_fencing()

    print(f"""{main.__doc__}
-> Input File: {input_file}
-> Plant Types: {garden.plant_types}
-> Regions: {len(garden.regions)}
-> Fencing Cost: ${fencing_cost}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default='./garden-plot.map'
    )
    args = parser.parse_args()

    main(args.input_file)
