import os

class PlutonianPebbles2:
    # def __init__(self, filename:str):
    #     self.__filename = filename
    #     self.__reformat_data_file()

    def __init__(self, pebble):
        self.__pebble = pebble

        self.__file_prefix = f"./tmp/iteration-p{pebble}"

        with open(f"{self.__file_prefix}-0.dat", "w") as fptr:
            fptr.write(f"{pebble}\n")

    # def __reformat_data_file(self):
    #     """
    #     Reformat data file as 1 number per line
    #     """
    #     pebbles = None
    #     with open(self.__filename, "r") as fptr:
    #         line = fptr.readline()
    #         pebbles = line.strip().split(" ")

    #     # dirname= os.path.dirname(self.__filename)
    #     # basename = os.path.basename(self.__filename)
    #     # (path, ext) = os.path.splitext(self.__filename)
    #     # with open(f"{path}-0{ext}", "w")as fptr:
    #     with open("./tmp/iteration-0.dat", "w")as fptr:
    #         for pebble in pebbles:
    #             fptr.write(f"{pebble.strip()}\n")


    def blink(self, count):
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
        pebble_count = 0
        for iteration in range(count):
            print(f"({self.__pebble}) #{iteration+1} - {pebble_count}")
            in_fptr = open(f"{self.__file_prefix}-{iteration}.dat", "r")
            out_fptr = open(f"{self.__file_prefix}-{iteration+1}.dat", "w")

            pebble_count = 0
            while line := in_fptr.readline():
                # Grab a Pebble
                pebble = line.strip()

                # Figure out new pebble(s) based on pebble
                new_pebbles = []

                if pebble == "0":
                    new_pebbles.append(1)
                elif len(pebble) % 2 == 0:
                    digits = list(pebble)
                    mid = (len(digits) // 2)
                    left = "".join(digits[0:mid])
                    right = "".join(digits[mid:])
                    new_pebbles.append(int(left))
                    new_pebbles.append(int(right))
                else:
                    new_pebbles.append(int(pebble) * 2024)

                # Write new pebble(s) to file for next iteration
                for np in new_pebbles:
                    pebble_count += 1
                    out_fptr.write(f"{np}\n")

            in_fptr.close()
            out_fptr.close()

        return pebble_count
