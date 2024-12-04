#!/usr/bin/env python
import sys

import utils

def main(input_file:str) -> None:
    grid = utils.create_word_grid(input_file)
    cols = len(grid[0])
    rows = len(grid)
    count = utils.count_x_mas(grid)

    print(f"""--- Day 04 // Puzzle 02 ---
-> Input File: {input_file}
-> Grid Size: {cols}x{rows}
-> X-MAS Found: {count} times
""")


if __name__ == "__main__":
    input_file = "xmas-search.dat"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
