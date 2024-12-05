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
        rules:dict, page_updates:list[int]) -> tuple[list[int], int]:
    """
    Check the correctness of each of the `page_updates` using the given `rules`.

    Returns:
        tuple:(
            list: List of the index in `page_updates` to each correct page set
            int: The sum of the middle page numbers from each correct page set.
        )

    >>> check_printer_data({1: [2], 2: [3], 3: [4], 4: [5]}, [[1,2,3,4,5]])
    ([0], 3)

    >>> check_printer_data(
    ... {47: [53, 13, 61, 29], 97: [13, 61, 47, 29, 53, 75], 75: [29, 53, 47, 61, 13], 61: [13, 53, 29], 29: [13], 53: [29, 13]},
    ... [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13], [75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]]
    ... )
    ([0, 1, 2], 143)
    """
    mid_page_sum = 0
    correct_indexes = []

    for idx, page_set in enumerate(page_updates):
        is_correct = True
        for px_idx, page_x in enumerate(page_set):
            if is_correct == False:
                # This page set has already been determined to be incorrect
                # ...move on
                break

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

        if is_correct:
            correct_indexes.append(idx)
            mid_page_idx = len(page_set) // 2
            mid_page_sum += page_set[mid_page_idx]

    return correct_indexes, mid_page_sum
