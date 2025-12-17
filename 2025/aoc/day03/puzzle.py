from functools import cache
from aoc.lib.puzzle import Puzzle


class Lobby(Puzzle):
    """AOC-2025 // Day03 -- Lobby"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__data = []
        self._read_input(self.__parse_input)

    def __parse_input(self, line):
        if not line.startswith("#"):
            self.__data.append(line)

    def __find_largest_battery(self, bank: list[int], start=0):
        found_idx = None
        max_value = 0
        for idx, battery in enumerate(bank[start:]):
            if battery > max_value:
                max_value = battery
                found_idx = start + idx

        return found_idx, max_value

    def _part1(self):
        total_joltage = 0

        # find the largest number in the bank starting at the beginning
        # ...but can't be the last number in the bank/list.
        # then find the largest number starting from the first num's position
        # concat, convert to int
        for bank in self.__data:
            # convert to a list of ints
            batteries = [int(b) for b in list(bank)]

            self._debug(f"=> {bank}")
            # find the largest battery in the bank, EXCLUDING the last one
            # ...since no battery can follow it
            (b1_idx, batt1) = self.__find_largest_battery(batteries[:-1])
            self._debug(f"  -> #1 -> [{b1_idx}] - {batt1}")

            # find the largest battery AFTER the position of the first largest
            (b2_idx, batt2) = self.__find_largest_battery(batteries, start=b1_idx + 1)
            self._debug(f"  -> #2 -> [{b2_idx}] - {batt2}")

            joltage = (batt1 * 10) + batt2
            total_joltage += joltage
            self._debug(f"  -> {joltage}/{total_joltage}")

        return total_joltage

    @cache
    def __compute_joltage(self, bank, conn_len):
        joltage = 0
        bank_len = len(bank)

        # find the largest battery excluding last
        idx, batt = self.__find_largest_battery(bank[:-1], start=0)

        # update joltage => battery * index found
        joltage += (conn_len - idx**10) + batt

        # recurse
        if bank_len > 1:
            joltage += self.__compute_joltage(bank[:what:])

        return joltage

        # bank:234234234234278 => 434234234278
        # found:.............7.
        # -> batt + 10**1 | => 70
        # -> why 1? => (len(bank) - 1) - idx => (15-1)-13 = 1
        # -> recurse: start at bank[idx]
        # bank:8
        # found:8
        # -> batt + 10**0 | => 8
        # -> why 0? => (len(bank) - 1) - idx => (1-1)-0 = 0
        # ->


    def _part2(self):
        total_joltage = 0
        # find the twelve highest numbers & remember their idx
        # create a 12 digit number from those twelve w/ each digit
        # in it's relative position to the other based on idx.
        for bank in self.__data:
            self._debug(f"=> {bank}")
            # convert to a list of ints
            batteries = [int(b) for b in list(bank)]

            joltage = self.__compute_joltage(bank, 12)


        return total_joltage













#
