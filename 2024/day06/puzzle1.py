#!/usr/bin/env python
import pprint
import sys

import utils

def main(input_file:str) -> None:
    # load the patrol map
    patrol_map = utils.load_map(input_file)
    width = len(patrol_map[0])
    height = len(patrol_map)

    # scan the map to mark out the route
    marked_map = utils.analyze_map(patrol_map, utils.puzzle1_handler)

    # count each unique location
    pos_cnt = utils.count(marked_map, utils.POSITION_MARK)

    print(f"""--- Day 06 // Puzzle 01 ---
-> Input File: {input_file}
-> Map Size: {width}x{height}
-> Guard Positions: {pos_cnt}
""")


if __name__ == "__main__":
    input_file = "patrol.map"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
