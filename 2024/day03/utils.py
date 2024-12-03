import re

def load_memory_dump(filename:str) -> list[str]:
    data = []

    with open(filename, "r") as fptr:
        data = fptr.readlines()

    return data


def scan_memory_location(memory:str) -> int:
    """
    Scan a memory location (string) looking for `mul(x,y)` instructions and
    sum the result of each.

    >>> scan_memory_location("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    161
    """
    total = 0

    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)
    # print(instructions)
    for inst in instructions:
        operands = re.match(r"mul\((\d+),(\d+)\)", inst)
        total += int(operands.group(1)) * int(operands.group(2))

    return total
