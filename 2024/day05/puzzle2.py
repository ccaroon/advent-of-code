#!/usr/bin/env python
import sys

import utils

def main(input_file:str) -> None:


    print(f"""--- Day 05 // Puzzle 02 ---
-> Input File: {input_file}

""")


if __name__ == "__main__":
    input_file = None

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
