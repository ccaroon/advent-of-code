#!/usr/bin/env python
import sys

from antenna_map import AntennaMap

def main(input_file:str) -> None:
    antenna_map = AntennaMap(input_file)
    antenna_map.antinode_scan()
    antinode_count = len(antenna_map.antinodes)

    print(f"""--- Day 08 // Puzzle 01 ---
-> Input File: {input_file}
-> AntiNodes: {antinode_count}
""")


if __name__ == "__main__":
    input_file = "./antenna.map"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
