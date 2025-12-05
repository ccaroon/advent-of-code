from aoc.lib.puzzle import Puzzle


class Cafeteria(Puzzle):
    """AOC-2025 // Day05 -- Cafeteria"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__iid_ranges = []
        self.__iids = []
        self._read_input(self.__parse_input)

    def __parse_input(self, line):
        # id ranges 1 per line
        # blank line
        # ingredient ids 1 per line
        if "-" in line:
            start, end = line.split("-", 2)
            self.__iid_ranges.append((int(start), int(end)))
        elif line:
            self.__iids.append(int(line))

    def __check_freshness(self, iid, irng):
        """
        Is `iid` in the `irng` range with start and end being inclusive

        Args:
            iid (int): Ingredient ID
            irng (tuple(int,int)): Start and End of Fresh Ingredient Range
        """
        is_fresh = False
        if iid >= irng[0] and iid <= irng[1]:
            is_fresh = True
        return is_fresh

    def _part1(self):
        fresh_count = 0
        # Check to see if each iid is in any of the Fresh Ranges
        # ...if so, count as fresh & move to next ingredient
        # ...each ingredient only has be be in one range to be noted as fresh
        for iid in self.__iids:
            for irng in self.__iid_ranges:
                self._debug(f"[{iid}] in [{irng}]...")
                if self.__check_freshness(iid, irng):
                    fresh_count += 1
                    break

        return fresh_count

    def _part2(self):
        pass
