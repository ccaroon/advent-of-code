class LockSmith:

    EMPTY = "."
    SOLID = "#"

    LOCK = 1
    KEY = 2

    def __init__(self, input_file):
        self.__input_file = input_file

        self.__keys = []
        self.__locks = []
        self.__read_input_file()


    def __read_input_file(self):
        with open(self.__input_file, "r") as fptr:
            start_schm = True
            schematic = []
            schm_type = None
            while True:
                line = fptr.readline()
                # Blank - end current & start new schematic
                # EOF - end current schematic and END reading
                if line == "\n" or line == "":
                    if schm_type == self.KEY:
                        self.__keys.append(schematic)
                    elif schm_type == self.LOCK:
                        self.__locks.append(schematic)

                    start_schm = True
                    schematic = []

                    if line == "":
                        break
                    else:
                        continue

                data = line.strip()
                if start_schm:
                    start_schm = False

                    if data.startswith(self.EMPTY):
                        schm_type = self.KEY
                    elif data.startswith(self.SOLID):
                        schm_type = self.LOCK

                    schematic.append(list(data))
                else:
                    schematic.append(list(data))


    def display_schematic(self, schematic):
        output = ""
        for row in schematic:
            for col in row:
                output += f"{col:2}"
            print(output)
            output = ""


    def __schematic_to_heights(self, schematic) -> list:
        # fill with -1 b/c don't count first row
        heights = [-1 for _ in schematic[0]]
        for cidx in range(len(schematic[0])):
            for ridx in range(len(schematic)):
                if schematic[ridx][cidx] == self.SOLID:
                    heights[cidx] += 1

        return heights


    def find_key_lock_pairs(self):
        self.display_schematic(self.__keys[0])
        h = self.__schematic_to_heights(self.__keys[0])
        print(h)

        self.display_schematic(self.__locks[0])
        h = self.__schematic_to_heights(self.__locks[0])
        print(h)

        # print(self.__locks)

        # with open(self.__input_file, "r") as fptr:
        #     line = fptr.readline()
        #     while line:
        #         line = fptr.readline()
        #         print(f"[{line}]")














#
