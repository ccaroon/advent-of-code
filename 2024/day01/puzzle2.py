#!/usr/bin/env python
import sys

import utils

def sim_score(left:list[int], right:list[int]) -> int:
    """
    Calculate a total similarity score by adding up each number in the left
    list after multiplying it by the number of times that number appears in the
    right list.

    >>> sim_score([3,4,2,1,3,3], [4,3,5,3,9,3])
    31
    """
    score = 0
    counts = {}

    # Count the number of times a number in the `left` list appears in the
    # `right` list.
    for idx in range(len(left)):
        lnum = left[idx]
        # does the number appear in the `right` list?
        # have we already counted it?
        # Yes & No -> add it to `counts`
        if lnum in right and lnum not in counts:
            # update `counts`
            counts[lnum] = right.count(lnum)

    # Calculate score
    for idx in range(len(left)):
        lnum = left[idx]
        score += lnum * counts.get(lnum, 0)

    return score


def main(input_file:str) -> None:
    """ Entry Point """
    # read the input file
    left, right = utils.read_input(input_file)

    # get simularity score
    score = sim_score(left, right)

    print(f"""--- Day 01 // Puzzle 02 ---
-> Input File: {input_file}
-> # of LocIds: {len(left)}
-> Sim Score: {score}
""")


if __name__ == "__main__":
    input_file = "day1-input.dat"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
