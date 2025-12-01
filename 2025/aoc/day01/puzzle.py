from aoc.lib.puzzle import Puzzle

class SecretEntrance(Puzzle):
    """ AOC-2025 // Day01 -- Secret Entrance """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__dial_pos = 50
        self.__data = []
        self._read_input(self.__parse_input)


    def __parse_input(self, line):
        self.__data.append(line)


    def _part1(self):
        zero_count = 0
        for rot_code in self.__data:
            code = rot_code[0] # "L" or "R"
            count = int(rot_code[1:]) # 0 ... INF

            # count // 100
            # => How many times around & back to same number
            # => I.e. How many times it passes 0
            # times_past_zero = count // 100

            # count % 100
            # ==> How many actual clicks/positions the dial moves
            clicks = count % 100

            # ------------------------------------------------------------------
            # LEFT -> lower number -> subtract
            # 0 ->wraps-> 99
            # ------------------------------------------------------------------
            if code == "L":
                new_pos = self.__dial_pos - clicks
                if new_pos < 0:
                    new_pos = new_pos + 100
                self._debug(f"{self.__dial_pos}+{rot_code} => {new_pos}")
                self.__dial_pos = new_pos
            # ------------------------------------------------------------------
            # RIGHT -> higher number -> add
            # 99 ->wraps-> 0
            # ------------------------------------------------------------------
            elif code == "R":
                new_pos = self.__dial_pos + clicks
                if new_pos >= 100:
                    new_pos = new_pos - 100
                self._debug(f"{self.__dial_pos}+{rot_code} => {new_pos}")
                self.__dial_pos = new_pos
            else:
                raise ValueError(f"Invalid Rotation Code [{rot_code}]")

            if self.__dial_pos == 0:
                zero_count += 1

        return zero_count


    def _part2(self):
        pass







#
