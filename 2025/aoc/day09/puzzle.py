import itertools

from aoc.lib.location import Location
from aoc.lib.puzzle import Puzzle


class MovieTheater(Puzzle):
    """AOC-2025 // Day09 -- MovieTheater"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__data = []
        self._read_input(self.__parse_input)

    def __parse_input(self, line):
        (row, col) = line.split(",", 2)
        self.__data.append(Location(int(row), int(col)))

    def __compute_area(self, p1, p2):
        rows = abs(p1.row - p2.row) + 1
        cols = abs(p1.col - p2.col) + 1

        return rows * cols

    def _part1(self):
        # For every combination of 2 red-tiles, compute the
        # area and find the max
        combos = itertools.combinations(self.__data, 2)
        max_area = 0
        for pair in combos:
            max_area = max(max_area, self.__compute_area(pair[0], pair[1]))

        return max_area

    def _part2(self):
        pass
