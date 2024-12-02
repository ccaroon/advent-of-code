def comp_direction(level1:int, level2:int) -> int:
    """
    Compute if direction between level1 & level2 is...

    Returns:
        int: -1 | 0 | +1 (dec, same, inc)

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


def report_is_safe(report:list[int]) -> tuple[bool, int]:
    """
    The Report is Safe if...

    - The levels are either all increasing or all decreasing.
    - Any two adjacent levels differ by at least one and at most three.

    Returns:
        tuple: (is_safe, failure_list)

    >>> report_is_safe([7,6,4,2,1])
    (True, [])

    >>> report_is_safe([1,2,7,8,9])
    (False, [1])

    >>> report_is_safe([9,7,6,2,1])
    (False, [2])

    >>> report_is_safe([1,3,2,4,5])
    (False, [1])

    >>> report_is_safe([8,6,4,4,1])
    (False, [2])

    >>> report_is_safe([1,3,6,7,9])
    (True, [])
    """
    # Assume it's safe
    is_safe = True
    failed_levels = []

    main_direction = None

    for idx in range(len(report) - 1):
        diff = abs(report[idx] - report[idx + 1])
        rep_dir = comp_direction(report[idx], report[idx + 1])

        # use first non-zero direction as main_direction of levels
        if rep_dir != 0 and main_direction is None:
            main_direction = rep_dir

        if (diff < 1 or diff > 3) or (rep_dir != main_direction):
            is_safe = False
            failed_levels.append(idx)
            # break

    return (is_safe, failed_levels)
