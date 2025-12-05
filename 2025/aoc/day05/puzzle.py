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
        processed_ranges = []
        fresh_iids = 0
        for irng in self.__iid_ranges:
            count = (irng[1] - irng[0]) + 1
            overlap_count = self.__find_overlap(irng, processed_ranges)
            count -= overlap_count

            fresh_iids += count
            processed_ranges.append(irng)
            # ------------------
            # 1655071119701-2036139951240
            # 282420790922884-290825089106666
            # find where ranges overlay
            #
            # 3-5   => 5-3+1   => 3
            # is 3-5 covered by any previous range? NO +3

            # 10-14 => 14-10+1 => 5
            # is 10-15 covered by any previous range? NO +5

            # 16-20 => 20-16+1 => 5
            # is 16-20 covered by any previous range? NO +5

            # 12-18 => 18-12+1 => 7
            # is 12-18 covered by any previous range? YES

            # 12-18 (12,13,14,15,16,17,18) | 10-14 (10,11,12,13,14)
            # -> check start and end for overlap in any previous ranges
            # overlap: my start to other end
            # overlap: 12 to 14
            # overlap: 14-12+1 = 3
            # 7(range) - 3(overlap) => 4

            # 12-18 (12,13,14,15,16,17,18) | 16-20 (16,17,18,19,20)
            # overlap: my end to other end
            # overlap: 18 to 20
            # overlap: 20-18+1 = 3
            # 4(overlap1) - 3(overlap) => 1
            # +1


        return fresh_iids


#
