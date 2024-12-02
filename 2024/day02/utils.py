def comp_direction(level1, level2):
    """
    Compute if direction between level1 & level2 is...

    +1 -- increasing
     0 -- same
    -1 -- decreasing

    >>> comp_direction(12, 13)
    1

    >>> comp_direction(42, 42)
    0

    >>> comp_direction(77, 42)
    -1
    """
    direction = 0

    if level1 < level2:
        direction = +1
    elif level1 == level2:
        direction = 0
    elif level1 > level2:
        direction = -1

    return direction


def report_is_safe(report_data, enable_dampener=False):
    """
    The Report is Safe if...

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

    >>> report_is_safe("7 6 4 2 1")
    True

    >>> report_is_safe("1 2 7 8 9")
    False

    >>> report_is_safe("9 7 6 2 1")
    False

    >>> report_is_safe("1 3 2 4 5")
    False

    >>> report_is_safe("8 6 4 4 1")
    False

    >>> report_is_safe("1 3 6 7 9")
    True
    """
    is_safe = True
    # Convert data into array/list
    levels = report_data.split(" ")
    # Convert levels from str to int
    levels = [int(lvl) for lvl in levels]

    main_direction = comp_direction(levels[0], levels[1])

    for idx in range(len(levels) - 1):
        diff = abs(levels[idx] - levels[idx + 1])
        if diff < 1 or diff > 3:
            is_safe = False
            break

        report_direction = comp_direction(levels[idx], levels[idx + 1])
        if report_direction != main_direction:
            is_safe = False
            break

    return is_safe
