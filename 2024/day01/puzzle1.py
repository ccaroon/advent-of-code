#!/usr/bin/env python
import re
import sys

def read_input(filename):
    """
    Opens the input file & reads each column of numbers into two separate lists.
    """
    left = []
    right = []

    with open(filename) as fptr:
        line = fptr.readline()
        while line:
            # remove extra whitespace
            id_str = re.sub(r"\s+", " ", line)

            # split each line into the two numbers
            (lnum, rnum) = id_str.strip().split(" ", 2)

            # ...store left num in "left" list
            left.append(int(lnum))

            # ...store right num in "right" list
            right.append(int(rnum))

            # get next line
            line = fptr.readline()

    return (left, right)


def compute_dist(left:list, right:list) -> int:
    """
    Compute the total distance between two lists of ints.

    Each list should have the same length.

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


def main(input_file):
    total_dist = 0

    # read the input file
    left, right = read_input(input_file)

    total_dist = compute_dist(left, right)


    print(f"""--- Day 01 ---
-> Input File: {input_file}
-> # of Locations: {len(left)}
-> Total Distance: {total_dist}
""")


if __name__ == "__main__":
    input_file = "day1-input.dat"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
