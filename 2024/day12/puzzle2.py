#!/usr/bin/env python
import argparse

from garden import Garden

def main(input_file:str, **kwargs) -> None:
    """Day 12 // Puzzle 02"""

    garden = Garden(input_file)
    print(garden)
    fencing_cost = garden.calculate_fencing(with_discount=True)

    import pprint
    pprint.pprint(garden.regions)
    region = garden.regions[2]
    print("-------")
    pprint.pprint(region.sorted_plots())
    print(region.sides)


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
