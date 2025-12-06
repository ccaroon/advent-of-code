from aoc.lib.puzzle import Puzzle


class TrashCompactor(Puzzle):
    """AOC-2025 // Day06 -- Trash Compactor"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__data = []
        self._read_input(self.__parse_input)

    def __parse_input(self, line):
        self.__data.append(line)

    def _part1(self):
        # The last line contains the operator for each column of numbers
        ops = self.__data[-1].split()

        # Use the first line to initialize the answers for each column of nums
        init_line = self.__data[0]
        answers = [int(num) for num in init_line.split()]

        # Split each additional line and add/mult each number for the
        # appropriate column
        # Exlude first line and last line
        for line in self.__data[1:-1]:
            numbers = [int(num) for num in line.split()]
            for idx, num in enumerate(numbers):
                op = ops[idx]
                if op == "+":
                    answers[idx] += num
                elif op == "*":
                    answers[idx] *= num

        return sum(answers)

    def _part2(self):
        pass







#
