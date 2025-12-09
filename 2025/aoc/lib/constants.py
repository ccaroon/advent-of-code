from collections import namedtuple

Direction = namedtuple("Direction", ["row_offset", "col_offset"])

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
