import copy

class RAM:

    FREE_BLOCK = "."
    CORRUPTED_BLOCK = "#"

    def __init__(self, input_file):
        self.__input_file = input_file

        self.__width = 0
        self.__height = 0
        self.__memory_space = []

        self.__bytes = []
        self.__read_input_file()
        self.__create_memory_space()


    def __read_input_file(self):
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                (col, row) = line.split(",", 2)
                row = int(row)
                col = int(col)
                self.__bytes.append((row, col))
                # Figure out grid W & H based in input
                if row > self.__height:
                    self.__height = row

                if col > self.__width:
                    self.__width = col

        self.__height += 1
        self.__width += 1


    def __create_memory_space(self):
        row = [self.FREE_BLOCK] * self.__width
        for _ in range(self.__height):
            self.__memory_space.append(copy.deepcopy(row))


    def display_memory_space(self):
        for row in self.__memory_space:
            output = ""
            for col in row:
                output += f"{col:2}"
            print(output)
        print()

    def tick(self):
        """
        Pass the next Nanosecond
        """
        coord = self.__bytes.pop(0)
        self.__memory_space[coord[0]][coord[1]] = "#"


    def simulate_byte_fall(self, ticks:int):
        for i in range(ticks):
            self.tick()
            print(f"----- {i+1} -----")
            self.display_memory_space()
            input()




#
