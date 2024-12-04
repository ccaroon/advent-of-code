# Directions in the form NAME = (row_delta, col_delta)
NORTH = (-1, 0)
EAST  = (0,  1)
SOUTH = (1,  0)
WEST  = (0, -1)
NE    = (-1, 1)
NW    = (-1, -1)
SE    = (1,  1)
SW    = (1, -1)


def create_word_grid(filename:str) -> list[list]:
    """
    Read `filename` into a list of lists of letters.

    Returns:
        list[list]: List of Lists. Each sub-list is a list of letters.

    Example:
        abcd
        efgh
        ijkl

        ...becomes...

        [
            [a,b,c,d]
            [e,f,g,h]
            [e,j,k,l]
        ]
    """
    grid = []
    with open(filename, "r") as fptr:
        line = fptr.readline()
        while line:
            grid.append(list(line.strip()))
            line = fptr.readline()

    return grid


def find_by_dir(grid:list[list], row:int, col:int, word:str, direction:tuple) -> bool:
    """
    Look for `word` in `grid` starting at `row`,`col` and looking in the
    compass `direction`.

    Returns:
        bool: Was `word` found?

    >>> find_by_dir([['.','.','X','M','A','S','.','.']], 0, 2, "XMAS", EAST)
    True

    >>> find_by_dir([['.','.','X','M','A','S','.','.']], 0, 4, "XMAS", WEST)
    False

    >>> find_by_dir([
    ... [' ',' ',' ',' ',' ',' '],
    ... [' ','X',' ',' ',' ',' '],
    ... [' ',' ','M',' ',' ',' '],
    ... [' ',' ',' ','A',' ',' '],
    ... [' ',' ',' ',' ','S',' ']
    ... ],
    ... 1, 1, "XMAS", SE)
    True
    """
    found = True
    num_rows = len(grid)
    num_cols = len(grid[0])

    curr_row = row
    curr_col = col
    for letter in word:
        # Still looking, but next row|col index is out of bounds
        # i.e. no more letters in that direction ... can't be found
        if  (
                curr_row < 0 or curr_row >= num_rows
                or
                curr_col < 0 or curr_col >= num_cols
            ):
            found = False
            break

        if letter == grid[curr_row][curr_col]:
            curr_row += direction[0]
            curr_col += direction[1]
        else:
            found = False
            break

    return found

def count_word(grid:list[list], word:str) -> int:
    """
    Count how many times the given `word` appears in the `grid`.

    Words can appear horizontal, vertical, diagonal, forwards or backwards.

    >>> count_word([['X','M','A','S','A','M','X','A','M','M']], "XMAS")
    2

    >>> count_word(
    ... [
    ... ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'], ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']
    ... ],
    ... "XMAS")
    18
    """
    count = 0

    # Assume each row has same number of cols
    num_rows = len(grid)
    num_cols = len(grid[0])

    for row in range(num_rows):
        for col in range(num_cols):
            # is the current letter the start of `word`
            if grid[row][col] == word[0]:
                # NOTE: word can exist in multiple directions from the same
                #       starting location
                for direction in (NORTH, EAST, SOUTH, WEST, NE, NW, SE, SW):
                    if find_by_dir(grid, row, col, word, direction):
                        count += 1

    return count


def count_x_mas(grid:list[list]) -> int:
    """
    Count the number of times `MAS` appears in the grid in an `X` pattern.

    M S
     A
    M S

    >>> count_x_mas(
    ... [
    ... ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'], ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']
    ... ])
    9
    """
    count = 0
    # Assume each row has same number of cols
    num_rows = len(grid)
    num_cols = len(grid[0])
    word = "MAS"

    for row in range(num_rows):
        for col in range(num_cols):
            # Look for an 'A', that's a possible middle/axis point
            if grid[row][col] == 'A':
                x_count = 0
                # Look for "MAS" starting a each "corner"
                for corner, direction in ((NW,SE), (NE,SW), (SW,NE), (SE,NW)):
                    if find_by_dir(grid, row+corner[0], col+corner[1], word, direction):
                        x_count += 1

                if x_count == 2:
                    count += 1

    return count
