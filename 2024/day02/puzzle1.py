#!/usr/bin/env python
import re
import sys

import utils

def main(report_file):
    safe_reports = 0
    report_count = 0

    with open(report_file, "r") as fptr:
        line = fptr.readline()
        while line:
            report_count += 1

            # strip out extra whitespace
            report_data = re.sub(r"\s+", " ", line.strip())

            if utils.report_is_safe(report_data):
                safe_reports += 1

            line = fptr.readline()

    print(f"""--- Day 02 // Puzzle 01 ---
-> Input File: {report_file}
-> # of Reports: {report_count}
-> Safe Reports: {safe_reports}
""")


if __name__ == "__main__":
    input_file = "./red-nosed-reactor-reports.dat"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
