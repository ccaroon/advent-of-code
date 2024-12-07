#!/usr/bin/env python
import sys

from bridge_repair import BridgeRepair

def main(input_file:str) -> None:

    br = BridgeRepair(input_file)
    result = br.calibration_result()

    print(f"""--- Day 07 // Puzzle 01 ---
-> Input File: {input_file}
-> Equation Count: {len(br.equations)}
-> Calibration Result: {result}
""")


if __name__ == "__main__":
    input_file = "calibration-equations.dat"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
