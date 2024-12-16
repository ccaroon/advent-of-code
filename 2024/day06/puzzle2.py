#!/usr/bin/env python
import pprint
import sys

import utils

def main(input_file:str) -> None:
    # load the patrol map
    patrol_map = utils.load_map(input_file)
    width = len(patrol_map[0])
    height = len(patrol_map)

    marked_map = utils.place_obstacles(patrol_map)
    count = utils.count(marked_map, utils.LOOP_OBSTACLE)

    # count = 0
    # for section in patrol_map:
    #     count += section.count("#")

    # print(f"Total Obstacles: {count}")

    # scan the map to mark out the route
    # count = utils.stupid_solution(patrol_map)

    # pprint.pprint(patrol_map)
    # print("----------------------------------------------------")
    # pprint.pprint(marked_map)

    # loop_cnt = utils.count(marked_map, utils.LOOP_OBSTACLE)

    print(f"""--- Day 06 // Puzzle 02 ---
-> Input File: {input_file}
-> Map Size: {width}x{height}
-> Obstacle Pos: {count}
""")


if __name__ == "__main__":
    input_file = "patrol.map"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
