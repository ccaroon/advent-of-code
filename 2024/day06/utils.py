import copy

UP = (-1,0)
RT = (0,1)
DN = (1,0)
LF = (0,-1)

TURN = {
    UP: RT,
    RT: DN,
    DN: LF,
    LF: UP
}

GUARD = "^"
MARK  = "X"
OBSTACLE = "#"

def load_map(filename:str) -> list[list[str]]:
    """
    Load the Patrol Map into a useable format.
    """
    map_data = []
    with open(filename, "r") as fptr:
        line = fptr.readline()
        while line:
            map_data.append(list(line.strip()))
            line = fptr.readline()

    return map_data


def lidar_scan(area_map:list[list[str]]) -> list[list[str]]:
    """
    Scan the `area_map` to map out the Guard's route using the rules:

    - If there is something directly in front of you, turn right 90 degrees.
    - Otherwise, take a step forward.

    Params:
        area_map (list): Map data loaded using `load_map()`

    Returns:
        list: A copy of the `area_map` with the Guard's route marked.

    >>> lidar_scan(
    ... [['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ...  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ...  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ...  ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ...  ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
    ...  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ...  ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
    ...  ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ...  ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ...  ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']]
    ... )
    [['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '#'], ['.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.'], ['.', '.', '#', '.', 'X', '.', '.', '.', 'X', '.'], ['.', '.', 'X', 'X', 'X', 'X', 'X', '#', 'X', '.'], ['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'], ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '#', '.'], ['#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'], ['.', '.', '.', '.', '.', '.', '#', 'X', '.', '.']]
    """
    marked_map = copy.deepcopy(area_map)

    width = len(marked_map[0])
    height = len(marked_map)

    # find starting position
    curr_row = None
    curr_col = None
    curr_dir = UP
    for row, scan_line in enumerate(marked_map):
        if GUARD in scan_line:
            curr_row = row
            curr_col = scan_line.index(GUARD)
            break

    # scan
    while True:
        # mark
        marked_map[curr_row][curr_col] = MARK

        # move
        new_row = curr_row + curr_dir[0]
        new_col = curr_col + curr_dir[1]

        # check if guard has exited the area
        if new_row < 0 or new_row >= height or new_col < 0 or new_col >= width :
            break

        # check for obstacle
        if marked_map[new_row][new_col] == OBSTACLE:
            # turn
            curr_dir = TURN[curr_dir]
            # update pos
            curr_row += curr_dir[0]
            curr_col += curr_dir[1]
        else:
            # update pos -- keep moving in same dir
            curr_row = new_row
            curr_col = new_col

    return marked_map


def count_unique_positions(marked_map:list[list[str]]) -> int:
    """
    Count the number of unique positions that are marked on the `marked_map`

    >>> count_unique_positions([['^',' ','#','.','.',]])
    0

    >>> count_unique_positions(
    ... [
    ...     ['.','#','X','^','X'],
    ...     ['.','X','.','.','.'],
    ...     ['.','X','X','.','.'],
    ...     ['.','.','X','X','.'],
    ...     ['.','X','X','X','.']
    ... ]
    ... )
    10
    """
    unique_pos = 0

    for row in marked_map:
        unique_pos += row.count(MARK)

    return unique_pos
