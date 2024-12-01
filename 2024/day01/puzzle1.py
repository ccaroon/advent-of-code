#!/usr/bin/env python
import sys

import utils

def compute_dist(left:list[int], right:list[int]) -> int:
    """
    Find the total distance between the `left` list and the `right` list by
    adding up the distances between each pair of numbers (left[i], right[i]).

    Each list should have the same length.
    Each list will be sorted lowest to highest.

    >>> compute_dist([3,4,2,1,3,3], [4,3,5,3,9,3])
    11
    """
    total_dist = 0

    # ensure lists have same length
    assert(len(left) == len(right))

    # sort each list
    left.sort()
    right.sort()

    # iterate from 0 to LEN
    for idx in range(len(left)):
        # compute dist for each pair
        # ...absolute value of left - rigth
        dist = abs(left[idx] - right[idx])

        # add dist to total dist
        total_dist += dist

    return total_dist


def main(input_file:str) -> None:
    """ Entry Point """
    total_dist = 0

    # read the input file
    left, right = utils.read_input(input_file)

    total_dist = compute_dist(left, right)

    print(f"""--- Day 01 // Puzzle 01 ---
-> Input File: {input_file}
-> # of LocIds: {len(left)}
-> Total Distance: {total_dist}
""")


if __name__ == "__main__":
    input_file = "day1-input.dat"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
