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

    def __compute_area(self, l1, l2):
        rows = abs(l1.row - l2.row) + 1
        cols = abs(l1.col - l2.col) + 1

        return rows * cols

    def _part1(self):
        # For every combination of 2 red-tiles, compute the
        # area and find the max
        combos = itertools.combinations(self.__data, 2)
        max_area = 0
        for pair in combos:
            max_area = max(max_area, self.__compute_area(pair[0], pair[1]))

        return max_area

    # def __find_

    def _part2(self):
        # map out the corners of the Loop
        # for each location
        # find all locs on same row
        #   - before it that are RED
        #   - after it that are RED
        # find all locs on same col
        #   - above it that are RED
        #   - below it that are RED
        # keep track of each end point in a set
        #   - can a run of red.green+.red be contained in another run?
        bbox_corners = set()
        for loc in self.__data:
            self._debug(f"=> {loc}...")
            same_row = list(filter(lambda oloc: oloc.row == loc.row, self.__data))
            same_col = list(filter(lambda oloc: oloc.col == loc.col, self.__data))

            bbox_corners.update(same_row)
            bbox_corners.update(same_col)

            # if len(same_row) != 2:
            #     self._debug(f"  -> Row: {same_row}")

            # if len(same_col) != 2:
            #     self._debug(f"  -> Col: {same_col}")

        # print(bbox_corners)
