from aoc.lib.puzzle import Puzzle


class SecretEntrance(Puzzle):
    """AOC-2025 // Day01 -- Secret Entrance"""

    DIAL_POSITIONS = 100

    def __init__(self, input_file, **kwargs):
        super().__init__(input_file, **kwargs)

        self.__dial_pos = 50
        self.__data = []
        self._read_input(self.__parse_input)

    def __parse_input(self, line):
        self.__data.append(line)

    def __rotate(self):
        zero_stats = {"during_rotation": 0, "end_of_rotation": 0}

        for rot_code in self.__data:
            code = rot_code[0]  # "L" or "R"
            count = int(rot_code[1:])  # 0 ... INF

            # => How many times around & back to same number
            # => I.e. How many times it passes 0
            times_past_zero = count // self.DIAL_POSITIONS

            # => How many actual clicks/positions the dial moves
            clicks = count % self.DIAL_POSITIONS

            # ------------------------------------------------------------------
            # LEFT -> lower number -> subtract
            # 0 ->wraps-> 99
            # ------------------------------------------------------------------
            if code == "L":
                new_pos = self.__dial_pos - clicks
                if new_pos < 0:
                    # wrap
                    new_pos = new_pos + self.DIAL_POSITIONS

                    # Did the dial go past zero when...
                    # ...it did NOT start on ZERO (did not pass it)
                    # ...it did NOT end on ZERO (counted in `clicks`)
                    # ...then count as pointing to zero during the rotation
                    # NOTE: I guess instead of this code you could just subtract
                    # the number of end_of_rotation zeros from the overall total
                    # so they don't get counted twice
                    # b/c if the dial is on ZERO at the end of a rotation it's
                    # also on ZERO at the start of the next rotation
                    if self.__dial_pos != 0 and new_pos != 0:
                        times_past_zero += 1

                self._debug(f"=> {self.__dial_pos} -> {rot_code}: {new_pos}")

                self.__dial_pos = new_pos
            # ------------------------------------------------------------------
            # RIGHT -> higher number -> add
            # 99 ->wraps-> 0
            # ------------------------------------------------------------------
            elif code == "R":
                new_pos = self.__dial_pos + clicks
                if new_pos >= self.DIAL_POSITIONS:
                    # wrap
                    new_pos = new_pos - self.DIAL_POSITIONS

                    # Did the dial go past zero when...
                    # ...it did NOT start on ZERO (did not pass it)
                    # ...it did NOT end on ZERO (counted in `clicks`)
                    # ...then count as pointing to zero during the rotation
                    # NOTE: I guess instead of this code you could just subtract
                    # the number of end_of_rotation zeros from the overall total
                    # so they don't get counted twice
                    # b/c if the dial is on ZERO at the end of a rotation it's
                    # also on ZERO at the start of the next rotation
                    if self.__dial_pos != 0 and new_pos != 0:
                        times_past_zero += 1

                self._debug(f"=> {self.__dial_pos} -> {rot_code}: {new_pos}")

                self.__dial_pos = new_pos
            else:
                err = f"Invalid Rotation Code [{rot_code}]"
                raise ValueError(err)

            zero_stats["during_rotation"] += times_past_zero
            if self.__dial_pos == 0:
                zero_stats["end_of_rotation"] += 1

        return zero_stats

    def _part1(self):
        stats = self.__rotate()
        return stats["end_of_rotation"]

    def _part2(self):
        stats = self.__rotate()
        return stats["during_rotation"] + stats["end_of_rotation"]
