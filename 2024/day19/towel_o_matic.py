import itertools
import re

class TowelOMatic:
    def __init__(self, input_file):
        self.__input_file = input_file

        self.__towels = []
        self.__designs = []

        self.__read_input()


    def __read_input(self):
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                data = line.strip()
                if "," in data:
                    data = re.sub(r"\s+", "", data)
                    self.__towels = data.split(",")
                elif data:
                    self.__designs.append(data)


    @property
    def towels(self):
        return str(self.__towels)


    @property
    def designs(self):
        return str(self.__designs)


    # NOTE: Only works on small data sets
    # Larger towel patterns will cause TOO many combos and use much RAM
    def analyze(self):
        possible_designs = 0

        for design in self.__designs:
            dlength = len(design)
            combos = itertools.product(self.__towels, repeat=dlength)

            for pattern in combos:
                patt_str = "".join(pattern)
                if patt_str.startswith(design):
                    possible_designs += 1
                    break

        return possible_designs














#
