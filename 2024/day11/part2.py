#!/usr/bin/env python
import argparse

from plutonian_pebbles import PlutonianPebbles

def main(input_file:str, blinks:int) -> None:
    total_pebbles = 0

    pp = PlutonianPebbles(input_file)
    total_pebbles = pp.blink2(blinks)

    print(f"""--- Day 11 // Part 02 ---
-> Input File: {input_file}
-> Blinks Count: {blinks}
-> Stone Count: {total_pebbles}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Day 11 - Plutonian Pebbles")

    parser.add_argument("input_file", nargs="?", default='./plutonian-stones.dat')
    parser.add_argument("--blinks", "-b", type=int, default=75, help="Number of Times to Blink. Default: 75")
    args = parser.parse_args()

    main(args.input_file, args.blinks)
