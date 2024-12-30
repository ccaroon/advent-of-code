from shared.direction import Direction

class Location:
    def __init__(self, row:int, col:int):
        self.row = row
        self.col = col


    def copy(self):
        return Location(self.row, self.col)


    def move(self, direction:Direction):
        """
        Move in Direction, updating current Location.
        """
        self.row += direction.row_delta
        self.col += direction.col_delta


    def look(self, direction:Direction, grid:list[list]) -> any:
        """
        Take a quick peek in `direction`
        """
        peek_loc = self.copy()
        peek_loc.move(direction)

        sight = None
        if (
            peek_loc.row >= 0 and peek_loc.row < len(grid)
            and
            peek_loc.col >= 0 and peek_loc.col < len(grid[0])
        ):
            sight = grid[peek_loc.row][peek_loc.col]

        return sight


    def distance_to(self, other):
        """
        Distance between two Locations

        >>> loc1 = Location(1,1)
        >>> loc2 = Location(5,5)
        >>> loc1.distance_to(loc2)
        (4, 4)
        >>> loc2.distance_to(loc1)
        (4, 4)
        """
        row_dist = abs(self.row - other.row)
        col_dist = abs(self.col - other.col)

        return (row_dist, col_dist)


    def adjacent_to(self, other):
        """
        Are two Location Cardinally Adjacent?

        >>> loc1 = Location(1,1)
        >>> loc2 = Location(1,2)
        >>> loc3 = Location(2,2)
        >>> loc1.adjacent_to(loc2)
        True
        >>> loc2.adjacent_to(loc1)
        True
        >>> loc1.adjacent_to(loc3)
        False
        >>> loc2.adjacent_to(loc3)
        True
        """
        adjacent = False

        # Must be N, E, S or W of self
        for dcode in ("N", "E", "S", "W"):
            check_loc = self.copy()
            direction = Direction(dcode)
            check_loc.move(direction)
            if check_loc == other:
                adjacent = True
                break

        return adjacent


    def __add__(self, other):
        if isinstance(other, Direction):
            new_loc = self.copy()
            new_loc.move(other)
        else:
            raise TypeError(f"Can't add Location and {type(other)}")

        return new_loc


    def __lt__(self, other):
        """
        >>> loc1 = Location(0,0)
        >>> loc2 = Location(0,1)
        >>> loc1 < loc2
        True

        >>> loc1 = Location(0,0)
        >>> loc2 = Location(0,0)
        >>> loc1 < loc2
        False

        >>> loc1 = Location(2,5)
        >>> loc2 = Location(1,34)
        >>> loc1 < loc2
        False

        >>> loc1 = Location(2,2)
        >>> loc2 = Location(3,3)
        >>> loc1 < loc2
        True
        """
        self_idx = self.row * 1_000_000 + self.col
        other_idx = other.row * 1_000_000 + other.col

        return self_idx < other_idx


    def __gt__(self, other):
        """
        >>> loc1 = Location(0,0)
        >>> loc2 = Location(0,1)
        >>> loc1 > loc2
        False

        >>> loc1 = Location(0,0)
        >>> loc2 = Location(0,0)
        >>> loc1 > loc2
        False

        >>> loc1 = Location(2,5)
        >>> loc2 = Location(1,34)
        >>> loc1 > loc2
        True

        >>> loc1 = Location(2,2)
        >>> loc2 = Location(3,3)
        >>> loc1 > loc2
        False
        """
        self_idx = self.row * 1_000_000 + self.col
        other_idx = other.row * 1_000_000 + other.col

        return self_idx > other_idx


    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


    def __hash__(self):
        return hash((self.row, self.col))


    def __repr__(self):
        return str(self)


    def __str__(self):
        return f"({self.row:2},{self.col:2})"
