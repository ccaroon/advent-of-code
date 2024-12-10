class Location:
    def __init__(self, row, col):
        self.row = row
        self.col = col


    def copy(self):
        return Location(self.row, self.col)


    def move(self, direction):
        self.row += direction.rdelta
        self.col += direction.cdelta


    # TODO: Maybe this method belongs on TopoMap instead?
    def look(self, direction, area_map:list[list]) -> any:
        peek_loc = self.copy()
        peek_loc.move(direction)

        sight = None
        if (
            peek_loc.row >= 0 and peek_loc.row < len(area_map)
            and
            peek_loc.col >= 0 and peek_loc.col < len(area_map[0])
        ):
            sight = area_map[peek_loc.row][peek_loc.col]

        return sight


    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


    def __hash__(self):
        return hash((self.row, self.col))


    def __repr__(self):
        return str(self)


    def __str__(self):
        return f"({self.row},{self.col})"
