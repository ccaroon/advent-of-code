#!/usr/bin/env python
import sys

from topo_map import TopoMap

def main(input_file:str) -> None:
    topo_map = TopoMap(input_file)
    _, rating = topo_map.map_trails()

    print(f"""--- Day 10 // Puzzle 02 ---
-> Input File: {input_file}
-> Trail Rating: {rating}
""")


if __name__ == "__main__":
    input_file = "./trail.map"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
