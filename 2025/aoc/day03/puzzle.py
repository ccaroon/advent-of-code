from aoc.lib.puzzle import Puzzle


class TODODay03(Puzzle):
    """ AOC-2025 // Day03 -- ????? """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__data = []
        self._read_input(self.__parse_input)


    def __parse_input(self, line):
        if not line.startswith("#"):
            prd_id_rng = line.split(",")
            self.__data.extend(prd_id_rng)


    def _part1(self):
        pass


    def _part2(self):
        pass
