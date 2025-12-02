from aoc.lib.puzzle import Puzzle

class GiftShop(Puzzle):
    """ AOC-2025 // Day02 -- Gift Shop """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__data = []
        self._read_input(self.__parse_input)


    def __parse_input(self, line):
        prd_id_rng = line.split(",")
        self.__data.extend(prd_id_rng)


    def _part1(self):
        invalid_ids = []
        for id_range in self.__data:
            (start,end) = id_range.split("-", 2)
            sid = int(start)
            eid = int(end)

            # Examine each PrdId in the Id Range
            for id in range(sid, eid+1):
                id_str = str(id)
                id_len = len(id_str)

                # To Be Invalid...
                # ...must have even length
                # ...first half and last half must match
                if len(id_str) % 2 == 0:
                    # split in half, do both sides match?
                    first_half = id_str[0:id_len // 2]
                    last_half = id_str[id_len // 2:]
                    if first_half == last_half:
                        invalid_ids.append(id)

        return sum(invalid_ids)


    def _part2(self):
        pass
