import aoc.lib.constants as const
from aoc.lib.puzzle import Puzzle


class PrintingDepartment(Puzzle):
    """ AOC-2025 // Day04 -- Printing Department """

    PAPER_ROLL = "@"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__data = []
        self._read_input(self.__parse_input)

        self.__row_cnt = len(self.__data)
        self.__col_cnt = len(self.__data[0])


    def __parse_input(self, line):
        row = list(line)
        self.__data.append(row)


    def __print_grid(self):
        for row in self.__data:
            for col in row:
                print(f"{col} ", end="")
            print("")


    def __count_rolls(self, row:int, col:int):
        """ Count the number of paper rolls around a given location """
        count = 0
        for offset in const.DIRECTIONS:
            row_idx = row + offset[0]
            col_idx = col + offset[1]

            if (
                    (row_idx >= 0 and row_idx < self.__row_cnt)
                    and
                    (col_idx >= 0 and col_idx < self.__col_cnt)
               ):
                if self.__data[row_idx][col_idx] == self.PAPER_ROLL:
                    count += 1

        return count


    def _part1(self):
        # number of paper rolls that are accessible
        count = 0
        for ridx, row in enumerate(self.__data):
            for cidx, item in enumerate(row):
                if item == self.PAPER_ROLL:
                    num_rolls = self.__count_rolls(ridx, cidx)
                    if num_rolls < 4:
                        count += 1

        return count


    def _part2(self):
        pass



#
