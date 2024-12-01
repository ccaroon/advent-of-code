import re

def read_input(filename:str) -> tuple[list,list]:
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

            # ...store left num in `left` list
            left.append(int(lnum))

            # ...store right num in `right` list
            right.append(int(rnum))

            # get next line
            line = fptr.readline()

    return (left, right)
