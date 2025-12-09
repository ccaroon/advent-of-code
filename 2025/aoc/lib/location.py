from aoc.lib.constants import Direction


class Location:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col

    @property
    def row(self):
        return self.__row

    @property
    def col(self):
        return self.__col

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Location({self.row},{self.col})"

    def move(self, direction: Direction):
        self.__row += direction.row_offset
        self.__col += direction.col_offset

    def peek(self, direction: Direction):
        return Location(
            self.__row + direction.row_offset,
            self.__col + direction.col_offset,
        )
