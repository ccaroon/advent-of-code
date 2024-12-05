#!/usr/bin/env python
import sys

import utils

def main(input_file:str) -> None:
    rules, updates = utils.read_printer_data(input_file)

    correct, page_sum = utils.check_printer_data(rules, updates)

    print(f"""--- Day 05 // Puzzle 01 ---
-> Input File: {input_file}
-> Rule Count: {len(rules)} (collated)
-> Page Updates: {len(updates)}
-> Correct Updates: {len(correct)}
-> Middle Page Sum: {page_sum}
""")


if __name__ == "__main__":
    input_file = "safety-manual-printer.dat"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
