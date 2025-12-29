from aoc.lib.puzzle import Puzzle


class TrashCompactor(Puzzle):
    """AOC-2025 // Day06 -- Trash Compactor"""

    def __init__(self, input_file, **kwargs):
        super().__init__(input_file, **kwargs)

        self.__data = []
        # nostrip b/c must preserve any starting or trailing whitespace
        # for part2
        self._read_input(self.__parse_input, nostrip=True)

    def __parse_input(self, line):
        self.__data.append(line.rstrip("\n"))

    def _part1(self):
        # The last line contains the operator for each column of numbers
        ops = self.__data[-1].split()

        # Use the first line to initialize the answers for each column of nums
        init_line = self.__data[0]
        answers = [int(num) for num in init_line.split()]

        # Split each additional line and add/mult each number for the
        # appropriate column
        # Exclude first line and last line
        # ...first line used to init totals
        # ...last line contains operators
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
        # The last line contains the operator for each column of numbers
        ops = self.__data[-1].split()
        row_len = len(self.__data[0])

        ops_idx = len(ops) - 1
        total = 0
        nums = []
        # Go 1 past the start of each row i.e. to -1 instead of 0
        # b/c we need to ensure that all the digits in col[0] get processed
        for ridx in range(row_len - 1, -2, -1):
            # A Column consists of all the numbers (vertically) that make up
            # a single mathematics operation
            # Columns are divided by there being a space at the same ridx
            # in every row
            # 1 Math Problem == 1 Column
            col_total = 0
            digits = []
            for row in self.__data[0:-1]:
                digits.append(row[ridx])  # noqa: PERF401
            # --------------------------------------------------
            # PERF401 wants me to do this. I don't want to.
            # digits = [row[ridx] for row in self.__data[0:-1]]
            # --------------------------------------------------

            num_str = "".join(digits)
            # ...ridx == -1 ... b/c we need the else below to fire
            # ...in order for all the digits in col[0] to form a number
            if num_str.strip() == "" or ridx == -1:
                # found column divider or beyond first (0th) column
                nums = [int(n) for n in nums]
                op = ops[ops_idx]
                if op == "+":
                    col_total = sum(nums)
                elif op == "*":
                    col_total = 1
                    for n in nums:
                        col_total *= n

                self._debug(f"{nums}({op}) = {col_total}")

                # Add to column total
                total += col_total
                # Reset nums to build next list of numbers
                nums = []
                # Jump to the operator for the next column's problem
                ops_idx -= 1
            else:
                # Still collecting all the numbers in a math problem column
                nums.append(num_str)

        return total
