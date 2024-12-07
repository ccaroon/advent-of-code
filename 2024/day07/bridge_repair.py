import itertools

class Equation:
    def __init__(self, operands, operators, result):
        self.operands = operands
        self.operators = operators
        self.result = result
        self.solveable = None # Unknown at this point


    @classmethod
    def from_str(cls, eq_string):
        (result, op_data) = eq_string.strip().split(":", 2)
        operands = op_data.strip().split(" ")
        operands = [int(num) for num in operands]

        equation = Equation(operands, [], int(result))
        return equation


    def __str__(self):
        output = ""
        for idx in range(len(self.operands)):
            operand = self.operands[idx]
            operator = None
            try:
                operator = self.operators[idx]
            except IndexError:
                operator = "?"

            if idx == len(self.operands) - 1:
                output += f"{operand} "
            else:
                output += f"{operand} {operator} "

        output += f"= {self.result}"

        return output


    def solve(self):
        """
        Attempt to solve the Equation.

        """
        # Only try to solve if it's solveability it unknown (None)
        if self.solveable is None:
            op_choices = itertools.product("+*", repeat=len(self.operands) - 1)

            for operators in op_choices:
                value = self.operands[0]
                for idx, operand in enumerate(self.operands[1:]):
                    operator = operators[idx]
                    if operator == "+":
                        value += operand
                    elif operator == "*":
                        value *= operand

                if value == self.result:
                    self.operators = list(operators)
                    self.solveable = True
                    break


class BridgeRepair:
    def __init__(self, filename):
        self.__data_file = filename
        self.equations = []

        self.__load_equations()


    def __load_equations(self):
        with open(self.__data_file) as fptr:
            line = fptr.readline()
            while line:
                self.equations.append(
                    Equation.from_str(line.strip())
                )

                line = fptr.readline()


    def calibration_result(self):
        """
        """
        total_result = 0
        for equation in self.equations:
            equation.solve()
            if equation.solveable:
                total_result += equation.result

        return total_result










#
