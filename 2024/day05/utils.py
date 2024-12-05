def read_printer_data(filename:str) -> tuple[dict, list[int]]:
    """
    Read Printer Data into usable format.

    Returns:
        tuple: (
                rules (dict): page_x => [page_y1, page_y2 ... page_yN]
                page_updates (list): list of page numbers
               )

    """
    rules = {}
    updates = []
    with open(filename, "r") as fptr:
        line = fptr.readline()
        # ignores invalid lines ... including blank lines, etc
        while line:
            if "|" in line:
                # treat as rule
                (p1,p2) = line.strip().split("|", 2)
                pagex = int(p1)
                pagey = int(p2)
                if pagex in rules:
                    rules[pagex].append(pagey)
                else:
                    rules[pagex] = [pagey]
            elif "," in line:
                # treat as page update
                page_nums = line.strip().split(",")
                # convert to ints
                page_nums = [int(num) for num in page_nums]
                updates.append(page_nums)

            line = fptr.readline()

    return rules, updates


def check_printer_data(
        rules:dict,
        page_updates:list[int],
        auto_correct=False
) -> dict:
    """
    Check the correctness of each of the `page_updates` using the given `rules`.

    If `auto_correct` is enabled, then fix the incorrect page sets and include
    the `incorrect` count and middle page sum in the return value.

    Returns:
        dict: {
            "correct_idxs":   list, # Index in `page_updates` to each correct page set
            "correct_sum":    int,  # Sum of the middle page numbers from each correct page set
            "incorrect_idxs": list  # Index in `page_updates` to each incorrect page set,
            "incorrect_sum":  int   # Sum of the middle page numbers from each incorrect page set
        }

    >>> check_printer_data({1: [2], 2: [3], 3: [4], 4: [5]}, [[1,2,3,4,5]])
    {'correct_idxs': [0], 'correct_sum': 3, 'incorrect_idxs': [], 'incorrect_sum': 0}

    >>> check_printer_data(
    ... {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]},
    ... [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13], [75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]]
    ... )
    {'correct_idxs': [0, 1, 2], 'correct_sum': 143, 'incorrect_idxs': [], 'incorrect_sum': 0}

    >>> check_printer_data(
    ... {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]},
    ... [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13], [75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]],
    ... auto_correct=True
    ... )
    {'correct_idxs': [0, 1, 2], 'correct_sum': 143, 'incorrect_idxs': [3, 4, 5], 'incorrect_sum': 123}
    """
    correct_sum = 0
    correct_indexes = []

    incorrect_sum = 0
    incorrect_indexes = []

    for idx, page_set in enumerate(page_updates):
        is_correct = check_page_set(rules, page_set)

        if is_correct:
            correct_indexes.append(idx)
            mid_page_idx = len(page_set) // 2
            correct_sum += page_set[mid_page_idx]
        else:
            if auto_correct:
                corrected_page_set = correct_page_set(rules, page_set)
                incorrect_indexes.append(idx)
                mid_page_idx = len(corrected_page_set) // 2
                incorrect_sum += corrected_page_set[mid_page_idx]

    return {
        "correct_idxs": correct_indexes,
        "correct_sum": correct_sum,
        "incorrect_idxs": incorrect_indexes,
        "incorrect_sum": incorrect_sum
    }


def check_page_set(rules:dict, page_set:list[int]) -> bool:
    """
    Check the correctness of `page_set` according to the printer `rules`

    Params:
        rules (dict): Printer Rules
        page_set (list): List of page numbers (ints)

    Returns:
        bool: Is the page set correct?

    >>> check_page_set(
    ... {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]},
    ... [75,97,47,61,53]
    ... )
    False

    >>> check_page_set(
    ... {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]},
    ... [97,75,47,61,53]
    ... )
    True

    >>> check_page_set(
    ... {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]},
    ... [75,47,61,53,29]
    ... )
    True

    >>> check_page_set(
    ... {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]},
    ... [61,13,29]
    ... )
    False
    """
    is_correct = True

    for px_idx, page_x in enumerate(page_set):
        rule = rules.get(page_x)
        if rule:
            for page_y in rule:
                try:
                    py_idx = page_set.index(page_y)
                    if px_idx >= py_idx:
                        is_correct = False
                        break
                except ValueError:
                    # page_y is not in the page_set
                    # That's ok...move on.
                    pass

        if is_correct == False:
            # This page set has already been determined to be incorrect
            # ...move on
            break

    return is_correct


def correct_page_set(rules:dict, page_set:list[int]) -> list[int]:
    """
    Correct the given `page_set` according to the printer `rules`

    Returns:
        list: The page set in correct order

    >>> correct_page_set(
    ... {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]},
    ... [75,97,47,61,53]
    ... )
    [97, 75, 47, 61, 53]

    >>> correct_page_set(
    ... {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]},
    ... [61,13,29]
    ... )
    [61, 29, 13]

    >>> correct_page_set(
    ... {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]},
    ... [97,13,75,29,47]
    ... )
    [97, 75, 47, 29, 13]
    """
    corrected_set = []

    # Build new list from scratch
    # page_x must be before all page_y's in rule_set
    for page_x in page_set:
        insert_idx = 999_999_999
        rule_set = rules.get(page_x)
        if rule_set:
            # Find lowest index of all page_y's in rule set
            for page_y in rule_set:
                if page_y in corrected_set:
                    py_idx = corrected_set.index(page_y)
                    if py_idx < insert_idx:
                        insert_idx = py_idx

        # print(f"Insert [{page_x}] @ [{insert_idx}]")
        corrected_set.insert(insert_idx, page_x)

    return corrected_set
