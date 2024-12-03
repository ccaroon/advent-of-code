#!/usr/bin/env python
import sys

import utils

def main(input_file:str) -> None:
    memory_dump = utils.load_memory_dump(input_file)

    total = 0
    for mem_loc in memory_dump:
        total += utils.scan_memory_location(mem_loc)


    print(f"""--- Day 03 // Puzzle 01 ---
-> Input File: {input_file}
-> Memory Locs: {len(memory_dump)}
-> Mul(l) Total: {total}
""")


if __name__ == "__main__":
    input_file = "./corrupt-memory.dump"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
