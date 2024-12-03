import re

def load_memory_dump(filename:str) -> list[str]:
    """ Load Memory Dump """
    data = []

    with open(filename, "r") as fptr:
        data = fptr.readlines()

    return data


def scan_memory_dump(memory:str, enable_conditions:bool=False) -> int:
    """
    Scan a memory dump looking for `mul(x,y)` instructions and
    sum the result of each.

    Args:
        memory (str): Memory dump
        enable_conditions (bool): Enable the `do` and `don't` instructions

    Return:
        int: Summation of all enabled `mul()` instructions

    >>> scan_memory_dump("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    161

    >>> scan_memory_dump("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", True)
    48
    """
    total = 0

    # Base Instruction Set
    instruction_set = [
        r"mul\(\d{1,3},\d{1,3}\)"
    ]

    # Add do() & don't() instructions
    if enable_conditions:
        instruction_set.append(r"do\(\)")
        instruction_set.append(r"don't\(\)")

    pattern = "|".join(instruction_set)
    # print(pattern)
    instructions = re.findall(pattern, memory)
    # print(instructions)

    do_mul = True
    for inst in instructions:
        if inst == "do()":
            do_mul = True
        elif inst == "don't()":
            do_mul = False
        elif inst.startswith("mul("):
            if do_mul:
                operands = re.match(r"mul\((\d+),(\d+)\)", inst)
                total += int(operands.group(1)) * int(operands.group(2))
        else:
            raise RuntimeError(f"Invalid Instruction [{inst}]")

    return total
