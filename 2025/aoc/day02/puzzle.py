import re
from aoc.lib.puzzle import Puzzle

class GiftShop(Puzzle):
    """ AOC-2025 // Day02 -- Gift Shop """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__data = []
        self._read_input(self.__parse_input)


    def __parse_input(self, line):
        if not line.startswith("#"):
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

                # To Be INvalid...
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
        invalid_ids = []
        for id_range in self.__data:
            (start,end) = id_range.split("-", 2)
            sid = int(start)
            eid = int(end)

            # Examine each PrdId in the Id Range
            for id in range(sid, eid+1):
                id_str = str(id)
                id_len = len(id_str)

                self._debug(f"=> {id_str}({id_len})")

                # Starting with the first N digits as a pattern (N=1)...
                # ...#1 - does the pattern exist 2 or more times in the id_str?
                # ...YES?
                # ......stop -> INVALID
                # ...NO?
                # ......N++
                # ......create a new pattern composed of the first N digits
                # ......GOTO #1
                # Example: id_str = "123123"
                # pattern = "1"
                # "^(1){2,}$" ~= "123123" -> Nope
                # pattern = "12"
                # "^(12){2,}$" ~= "123123" -> Nope
                # pattern = "123"
                # "^(123){2,}$" ~= "123123" -> Yup. Invalid! Stop!
                for idx in range(id_len):
                    # 1, 12, 123, etc.
                    pattern = id_str[0:idx+1]

                    # Must match against whole string
                    regex = fr"^({pattern}){{2,}}$"
                    self._debug(f"  -> Checking {id_str} =~ /{regex}/")
                    # If pattern/regex matches (two or more times)
                    # then it's invalid
                    if re.match(regex, id_str):
                        self._debug(f"  -> MATCH: {id_str} =~ /{regex}/")
                        invalid_ids.append(id)
                        break

        self._debug(invalid_ids)
        return sum(invalid_ids)
