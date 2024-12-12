#!/usr/bin/env python
import argparse
# import sys

from plutonian_pebbles2 import PlutonianPebbles2

def main(input_file:str, blinks:int) -> None:
    total_pebbles = 0

    pebbles = None
    with open(input_file, "r") as fptr:
        line = fptr.readline()
        pebbles = line.strip().split()

    for pb in pebbles:
        pp = PlutonianPebbles2(pb)
        total_pebbles += pp.blink(blinks)

    print(f"""--- Day 11 // Puzzle 02 ---
-> Input File: {input_file}
-> Blinks Count: {blinks}
-> Stone Count: {total_pebbles}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 11 - Plutonian Pebbles")

    parser.add_argument("input_file", nargs="?", default='./plutonian-stones.dat')
    parser.add_argument("--blinks", "-b", type=int, default=25)
    args = parser.parse_args()

    main(args.input_file, args.blinks)
