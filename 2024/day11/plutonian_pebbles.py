# from functools import cache
import time

class PlutonianPebbles:
    def __init__(self, filename:str):
        self.__filename = filename

        # Call Cache / Memoize Cache for __measure_growth() recursive calls.
        # Does the same thing as `functools.cache`, just wanted to implement it
        # myself.
        self.__cache = {}

        self.__pebbles = None
        self.__read_pebble_data()


    def __read_pebble_data(self):
        with open(self.__filename, "r") as fptr:
            line = fptr.readline()

            self.__pebbles = line.strip().split(" ")
            self.__pebbles = [int(item) for item in self.__pebbles]


    @property
    def count(self):
        return len(self.__pebbles)


    @property
    def pebbles(self):
        return self.__pebbles


    def blink(self):
        """
        Blink - Can't be used for a blink counts over 30'ish

        Rules (Verbose):
            - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
            - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
              The left half of the digits are engraved on the new left stone,
              and the right half of the digits are engraved on the new right stone.
            - If none of the other rules apply, the stone is replaced by a new stone;
              The old stone's number multiplied by 2024 is engraved on the new stone.

        Rules (simplified):
            - 0 -> 1
            - Even Digits, split into two stones. Half digits on right, half on left. 1234 -> 12 | 34
            - Else. Odd Digits. Replace with Number * 2024. 2 -> 4028; 100 -> 202400
        """
        new_layout = []

        for pebble in self.__pebbles:
            engraving = str(pebble)
            if pebble == 0:
                new_layout.append(1)
            elif len(engraving) % 2 == 0:
                digits = list(engraving)
                mid = (len(digits) // 2)
                left = "".join(digits[0:mid])
                right = "".join(digits[mid:])
                new_layout.append(int(left))
                new_layout.append(int(right))
            else:
                new_layout.append(pebble * 2024)

        self.__pebbles = new_layout


    def __str__(self):
        output = ""
        for pb in self.__pebbles:
            output += f"({pb}) "

        return output.strip()


    def __repr__(self):
        output = ""
        for pb in self.__pebbles:
            output += f"{pb} "

        return output.strip()


    def blink2(self, blinks:int):
        """
        Optimized version of blink that just **counts** the number of Pebbles
        after a certain number of `blinks`.
        """
        # Reset Memoize Cache
        self.__cache = {}

        count = len(self.__pebbles)
        for pebble in self.__pebbles:
            # --- UNCOMMENT for perf data ---
            # print(f"({pebble}) - {count} pebbles")
            # start = time.perf_counter()

            count += self.__measure_growth(pebble, blinks)

            # end = time.perf_counter()
            # bench = end - start
            # print(f"...-> {count} pebbles {bench:0.2f}s")

        return count


    # @cache
    def __measure_growth(self, pebble:int, blinks:int):
        """
        Measures the growth of a single Pebble over X `blinks`.

        Without caching/memoization (@cache) it will take toooo long for values
        of `blinks` over 40'ish.
        """
        add_count = 0

        # My own `functools.cache`
        key = f"{pebble}|{blinks}"
        result = self.__cache.get(key, None)

        if result is not None:
            return result

        if blinks > 0:
            blinks -= 1
            engraving = str(pebble)
            if pebble == 0:
                add_count += self.__measure_growth(1, blinks)
            elif len(engraving) % 2 == 0:
                digits = list(engraving)
                mid = (len(digits) // 2)
                left = "".join(digits[0:mid])
                right = "".join(digits[mid:])

                add_count = 1
                add_count += self.__measure_growth(int(left), blinks)
                add_count += self.__measure_growth(int(right), blinks)
            else:
                add_count += self.__measure_growth(pebble * 2024, blinks)

        # Cache a known result
        self.__cache[key] = add_count

        return add_count
