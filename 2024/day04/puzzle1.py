#!/usr/bin/env python
import sys

import utils

def main(input_file:str) -> None:
    grid = utils.create_word_grid(input_file)
    print(grid)
    cols = len(grid[0])
    rows = len(grid)
    count = utils.count_word(grid, "XMAS")

    print(f"""--- Day 04 // Puzzle 01 ---
-> Input File: {input_file}
-> Grid Size: {cols}x{rows}
-> XMAS Found: {count} times
""")


if __name__ == "__main__":
    input_file = "xmas-search.dat"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
