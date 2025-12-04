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

            joltage = int(f"{batt1}{batt2}")
            total_joltage += joltage
            self._debug(f"  -> {joltage}/{total_joltage}")

        return total_joltage

    def _part2(self):
        # find the twelve highest numbers & remember their idx
        # create a 12 digit number from those twelve w/ each digit
        # in it's relative position to the other based on idx.
        for bank in self.__data:
            bank_len = len(bank)
            found_batts = []
            # convert to a list of ints
            batteries = [int(b) for b in list(bank)]

            self._debug(f"=> {bank}")

            for _ in range(12):
                if found_batts:
                    lowest_idx = found_batts[0] // 1000
                    start = lowest_idx + 1 if lowest_idx < (bank_len - 12) else 0
                else:
                    lowest_idx = 0
                    start = 0

                self._debug(f"  -> LiDX [{lowest_idx}] | Start [{start}]")

                (idx, batt) = self.__find_largest_battery(batteries, start=start)
                found_batts.append(idx * 1000 + batt)
                found_batts.sort()

                # remove/mark the found battery
                # batteries.pop(idx)
                batteries[idx] = 0
                self._debug(f"  -> {batteries}")

                # 234234234234278
                # 434 234 234 278

            self._debug(f"  -> {found_batts}")
