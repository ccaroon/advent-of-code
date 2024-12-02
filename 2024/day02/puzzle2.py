#!/usr/bin/env python
import re
import sys

import utils

def main(report_file:str) -> None:
    safe_reports = 0
    report_count = 0

    with open(report_file, "r") as fptr:
        line = fptr.readline()
        while line:
            report_count += 1

            # strip out extra whitespace
            report_line = re.sub(r"\s+", " ", line.strip())
            # Convert data into array/list
            report_data = report_line.split(" ")
            # Convert levels from str to int
            report_data = [int(lvl) for lvl in report_data]

            (is_safe, failures) = utils.report_is_safe(report_data)
            if is_safe:
                safe_reports += 1
            else:
                # Dampening Enabled - Try to remove a single level to see if the
                # report then becomes safe.

                # print(f"{report_count} => {report_data}-> {failures} ({len(failures)})")

                # --------------------------------------------------------------
                # Brute force
                # Start at index 0 and remove every level from the report until
                # it becomes safe or we reach the end.
                # --------------------------------------------------------------
                # for idx in range(len(report_data)):
                #     new_data = report_data.copy()
                #     new_data.pop(idx)
                #     (is_safe, _) = utils.report_is_safe(new_data)

                #     if is_safe:
                #         safe_reports += 1
                #         break
                # --------------------------------------------------------------

                # --------------------------------------------------------------
                # Smarter? way
                # The level to remove **must** be around the index of the first
                # error.
                # Remove the level at the error index(0), the index before(-1)
                # and the index after(+1) it.
                # A single removal CAN fix multiple errors...
                # ...direction errors maybe?
                # --------------------------------------------------------------
                for mod in (-1, 0, 1):
                    new_data = report_data.copy()

                    # Remove the level at index of first failure + modifier
                    idx = failures[0] + mod

                    # don't go out of bounds
                    if idx < 0:
                        idx = 0
                    elif idx >= len(report_data):
                        idx = len(report_data) - 1

                    new_data.pop(idx)
                    # re-check, don't care about secondary failures
                    (is_safe, _) = utils.report_is_safe(new_data)
                    if is_safe:
                        safe_reports += 1
                        break
                # --------------------------------------------------------------

            line = fptr.readline()

    print(f"""--- Day 02 // Puzzle 02 ---
-> Input File: {report_file}
-> # of Reports: {report_count}
-> Safe Reports: {safe_reports} (Dampening Enabled)
""")


if __name__ == "__main__":
    input_file = "./red-nosed-reactor-reports.dat"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)

    # Benchmark the code
    # import timeit
    # count = 10
    # result = timeit.timeit(f"main('{input_file}')", setup='from __main__ import main', number=count)
    # average_result = result / count
    # print(f'Average time: {average_result:.3f} seconds')
