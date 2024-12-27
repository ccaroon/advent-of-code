#!/usr/bin/env python
import pprint
import sys

import utils

def main(input_file:str) -> None:
    # load the patrol map
    patrol_map = utils.load_map(input_file)
    width = len(patrol_map[0])
    height = len(patrol_map)

    count = utils.find_loops(patrol_map)

    print(f"""--- Day 06 // Part 02 ---
-> Input File: {input_file}
-> Map Size: {width}x{height}
-> Obstacle Pos: {count}
""")

if __name__ == "__main__":
    input_file = "patrol.map"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
