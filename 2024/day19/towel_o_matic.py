import itertools
import re

class TowelOMatic:
    def __init__(self, input_file, **kwargs):
        self.__input_file = input_file
        self.__debug = kwargs.get("debug", False)

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
        return self.__towels


    @property
    def designs(self):
        return self.__designs


    def analyze(self):
        return self.analyze2()


    def __print_debug(self, msg):
        if self.__debug:
            print(msg)


    def __find_match(self, design, depth=1):
        """
        1. look for entire design in towels
        -> brwrr in (r, wr, b, g, bwu, rb, gb, br) => False

        2. remove last letter (r), look for match in towels again
        -> brwr in (r, wr, b, g, bwu, rb, gb, br) => False

        3. remove last letter (r), look again
        -> brw in (r, wr, b, g, bwu, rb, gb, br) => False

        4. remove last letter (w), look again
        -> br in (r, wr, b, g, bwu, rb, gb, br) => True

        5. remove found towel from design
        -> brwrr - br => wrr
        -> GOTO 1 with new design => wrr
        """
        found_match = False

        # for idx in range(len(design), 0, -1):
        idx = len(design)
        partial = design[0:idx]
        # print(f"...find_match('{design}', {depth})")
        self.__print_debug(f"Looking for {design}[{idx}]...")
        while idx > 0 and not found_match:
            # x = design.replace(partial, f"[{partial}]")
            self.__print_debug(f"...'{partial}' in towels? ")
            if partial in self.__towels:
                plen = len(partial)
                sub_design = design[plen:]
                self.__print_debug(f"...YES! ('{design}' - '{partial}') -> '{sub_design}'")
                if sub_design:
                    self.__print_debug(f"...ENTER: find_match('{sub_design}')")
                    found_match = self.__find_match(sub_design, depth=depth+1)
                    self.__print_debug(f"...EXIT: find_match('{sub_design}') -> {found_match}")
                else:
                    # End of design, must match
                    found_match = True
                    # print(f"...MATCH: {design} - {partial}")
                    # input()
                    self.__print_debug("...MATCH!")
            else:
                self.__print_debug(f"...NO!")

            idx -= 1
            partial = design[0:idx]
            self.__print_debug(f"...NEXT: [{idx}] '{partial}'")
            # input()

        return found_match


    def __check_design(self, design):
        width = 60 #len(design)
        for towel in self.__towels:
            if towel in design:
                prev_design = design
                design = design.replace(towel, "")
                self.__print_debug(f"[{prev_design:{width}}] - [{towel:5}] => [{design:{width}}]")
                self.__check_design(design)

        return design == ""


    def analyze3(self):
        possible_designs = 0
        # bwu, wr, rb, gb, br, r, b, g
        # Sort self.__towel by len, longests first
        self.__towels.sort(key=lambda ptrn: len(ptrn), reverse=True)
        # print(self.__towels.index("gu"))
        # print(self.__towels)

        # self.__designs = ["guubgbbuwwgwugbwuwrbbuggubuwbbburgwwuwbggugrggwbg"]
        # self.__designs = ["rbugwrbrgggbwbgrwwrrwrguuurbbuwwwgubrbwbrrrrgwggruurrbrg"]
        # self.__designs = ["ubwu"]

        for idx, design in enumerate(self.__designs):
            possible = self.__check_design(design)

            self.__print_debug(f"#{idx}) [{design}] -> {possible}")

            if possible:
                possible_designs += 1


        return possible_designs


    def analyze2(self):
        possible_designs = 0
        # no_match_count = 0
        # bwu, wr, rb, gb, br, r, b, g
        # Sort self.__towel by len, longests first
        self.__towels.sort(key=lambda ptrn: len(ptrn), reverse=True)
        # print(self.__towels.index("gu"))
        # print(self.__towels)

        # self.__designs = ["rbugwrbrgggbwbgrwwrrwrguuurbbuwwwgubrbwbrrrrgwggruurrbrg"]
        # self.__designs = ["ubwu"]

        for design in self.__designs:
            width = len(design)
            more_towels = True
            while design and more_towels:
                for idx, towel in enumerate(self.__towels):
                    if towel in design:
                        prev_design = design
                        design = design.replace(towel, "")
                        self.__print_debug(f"[{prev_design:{width}}] - [{towel:5}] => [{design:{width}}]")
                        break

                    if idx == len(self.__towels) - 1:
                        more_towels = False

            if len(design) == 0:
                possible_designs += 1


        return possible_designs

    def analyze1(self):
        possible_designs = 0

        # self.__designs = ["rbugwrbrgggbwbgrwwrrwrguuurbbuwwwgubrbwbrrrrgwggruurrbrg"]
        # self.__designs = ["ubwu", "bggr"]
        for idx, design in enumerate(self.__designs):
            # self.__print_debug(f"### {idx} - {design} ###")
            print(f"### {idx} - {design} ###")
            possible = self.__find_match(design)
            self.__print_debug(f"--> {possible}")
            if possible:
                possible_designs += 1


        return possible_designs


    # NOTE: Only works on small data sets
    # Larger towel patterns will cause TOO many combos and use much RAM
    def analyze0(self):
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
