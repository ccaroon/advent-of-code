from collections import namedtuple

Direction = namedtuple("Direction", ["row_offset", "col_offset"])
Position = namedtuple("Position", ["row", "col"])

# Row,Col
N = Direction(-1, +0)
NE = Direction(-1, +1)
E = Direction(+0, +1)
SE = Direction(+1, +1)
S = Direction(+1, +0)
SW = Direction(+1, -1)
W = Direction(+0, -1)
NW = Direction(-1, -1)

DIRECTIONS = (N, NE, E, SE, S, SW, W, NW)


# TODO: Probably doesn't belong here in this file
def move(pos: Position, direction: Direction):
    new_row = pos.row + direction.row_offset
    new_col = pos.col + direction.col_offset

    return Position(new_row, new_col)
