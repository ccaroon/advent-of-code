#!/usr/bin/env python
import argparse
# import sys

from plutonian_pebbles import PlutonianPebbles

def main(input_file:str, blinks:int) -> None:
    pp = PlutonianPebbles(input_file)

    for cnt in range(blinks):
        print(f"-> #{cnt} [{pp.count}]")
        pp.blink()

    print(f"""--- Day 11 // Puzzle 01 ---
-> Input File: {input_file}
-> Blinks Count: {blinks}
-> Stone Count: {pp.count}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 11 - Plutonian Pebbles")

    parser.add_argument("input_file", nargs="?", default='./plutonian-stones.dat')
    parser.add_argument("--blinks", "-b", type=int, default=25)
    args = parser.parse_args()

    main(args.input_file, args.blinks)
