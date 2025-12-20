from aoc.day05.ingredient_range import IngredientRange
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
            self.__iid_ranges.append(IngredientRange(int(start), int(end)))
        elif line:
            self.__iids.append(int(line))

    def _part1(self):
        fresh_count = 0
        # Check to see if each iid is in any of the Fresh Ranges
        # ...if so, count as fresh & move to next ingredient
        # ...each ingredient only has be be in one range to be noted as fresh
        for iid in self.__iids:
            for irng in self.__iid_ranges:
                self._debug(f"[{iid}] in {irng}...")
                if irng.is_fresh(iid):
                    fresh_count += 1
                    break

        return fresh_count

    def __largest_range(self):
        max_size = 0
        found_irng = None

        for idx, irng in enumerate(self.__iid_ranges):
            size = len(irng)
            if size > max_size:
                max_size = size
                found_irng = self.__iid_ranges[idx]

        return found_irng

    def __find_overlap(self, irng, other_ranges):
        # 12-18 (12,13,14,15,16,17,18) | 10-14 (10,11,12,13,14)
        # -> check start and end for overlap in any previous ranges
        # overlap: my start to other end
        # overlap: 12 to 14
        # overlap: 14-12+1 = 3
        # 7(range) - 3(overlap) => 4
        # ---
        # 12-18 (12,13,14,15,16,17,18) | 16-20 (16,17,18,19,20)
        overlap_count = 0
        start = irng[0]
        end = irng[1]

        for other_rng in other_ranges:
            if start >= other_rng[0] and start <= other_rng[1]:
                overlap_count += (other_rng[1] - start) + 1
                self._debug(f"{irng} overlaps {other_rng} @ start[{start}]: {overlap_count}")
            elif end >= other_rng[0] and end <= other_rng[1]:
                self._debug(f"{irng} overlaps {other_rng} @ end[{end}]: {overlap_count}")
                overlap_count += (end - other_rng[0]) + 1

        return overlap_count

    def _part2(self):
        fresh_iids = 0

        # rng1 = self.__iid_ranges[2]
        # rng2 = self.__largest_range()

        rng2 = IngredientRange(1, 5)
        rng1 = IngredientRange(3, 7)

        print(rng1, rng2)
        print(rng1.unique_iids(rng2))

        # r1 = IngredientRange(1,5)
        # r2 = IngredientRange(3,7)

        # print(r1.compare(r2)) # -1
        # print(r2.compare(r1)) # 1

        # for irng in self.__iid_ranges:
        #     cmp = irng.compare(max_rng)
        #     if cmp is not None:
        #         print(f"{irng} <=> {max_rng} => [{cmp}]")

        return fresh_iids


#
