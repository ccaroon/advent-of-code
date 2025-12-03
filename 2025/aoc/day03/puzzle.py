from aoc.lib.puzzle import Puzzle


class Lobby(Puzzle):
    """ AOC-2025 // Day03 -- Lobby """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__data = []
        self._read_input(self.__parse_input)


    def __parse_input(self, line):
        if not line.startswith("#"):
            self.__data.append(line)


    def __find_largest_battery(self, bank:list[int]):
        found_idx = None
        max = 0
        for idx, battery in enumerate(bank):
            if battery > max:
                max = battery
                found_idx = idx

        return found_idx, max


    def _part1(self):
        total_joltage = 0

        # find the largest number in the bank starting at the beginning
        # ...but can't be the last number in the bank/list.
        # then find the largest number starting from the first num's position
        # concat, convert to int
        for bank in self.__data:
            # convert to a list of ints
            batteries = [int(chr) for chr in list(bank)]

            self._debug(f"=> {bank}")
            # find the largest battery in the bank, EXCLUDING the last one
            # ...since no battery can follow it
            (idx, batt1) = self.__find_largest_battery(batteries[:-1])
            self._debug(f"  -> #1 -> [{idx}] - {batt1}")

            # find the largest battery AFTER the position of the first largest
            (idx, batt2) = self.__find_largest_battery(batteries[idx+1:])
            self._debug(f"  -> #2 -> [{idx}] - {batt2}")

            joltage = int(f"{batt1}{batt2}")
            total_joltage += joltage
            self._debug(f"  -> {joltage}/{total_joltage}")

        return total_joltage


    def _part2(self):
        pass
