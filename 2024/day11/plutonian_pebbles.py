
class PlutonianPebbles:
    def __init__(self, filename:str):
        self.__filename = filename

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


    def cache(self):
        with open("./cache.dat", "w") as fptr:
            for pebble in self.__pebbles:
                fptr.write(f"{pebble} ")

            fptr.write("\n")


    def blink(self):
        """
        Blink

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



#
