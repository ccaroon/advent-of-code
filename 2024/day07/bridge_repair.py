import itertools

class Equation:
    def __init__(self, operands:list[int], operators:list[str], result:int):
        self.operands = operands
        self.operators = operators
        self.result = result
        self.solveable = None # Unknown at this point


    @classmethod
    def from_str(cls, eq_string:str):
        """
        New Equation instance from string representation

        Params:
            eq_string (str): Format: "RESULT: n1 n2 n3 ... nN"

        >>> Equation.from_str("190: 10 19")
        10 ? 19 = 190

        >>> Equation.from_str("7290: 6 8 6 15")
        6 ? 8 ? 6 ? 15 = 7290
        """
        (result, op_data) = eq_string.strip().split(":", 2)
        operands = op_data.strip().split(" ")
        operands = [int(num) for num in operands]

        equation = Equation(operands, [], int(result))
        return equation


    def __repr__(self):
        return str(self)


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


    def solve(self, operators:list[str]):
        """
        Attempt to solve the Equation.

        If solveable, mark it as such and set the `operators` attribute to the
        set of operators that solve it.

        # Solveable from Constructor
        >>> test = Equation([10,19], [], 190)
        >>> test.solve(('+','*'))
        >>> test.solveable
        True
        >>> test
        10 * 19 = 190

        # Solveable from `from_str`
        >>> test = Equation.from_str("3267: 81 40 27")
        >>> test.solve(('+','*'))
        >>> test.solveable
        True
        >>> test
        81 + 40 * 27 = 3267

        # Unsolveable
        >>> test = Equation.from_str("161011: 16 10 13")
        >>> test.solve(('+','*'))
        >>> test.solveable
        False
        >>> test
        16 ? 10 ? 13 = 161011

        # Unsolveable with just '+' & '*'
        >>> test = Equation([6,8,6,15], [], 7290)
        >>> test.solve(('+','*'))
        >>> test.solveable
        False
        >>> test
        6 ? 8 ? 6 ? 15 = 7290

        # Solveable by adding '||' to above operators: '+' & '*'
        >>> test = Equation([6,8,6,15], [], 7290)
        >>> test.solve(('+','*', '||'))
        >>> test.solveable
        True
        >>> test
        6 * 8 || 6 * 15 = 7290
        """
        # Only try to solve if it's solveability it unknown (None)
        if self.solveable is None:
            # Assume not solveable
            self.solveable = False

            op_choices = itertools.product(
                operators, repeat=len(self.operands) - 1)

            for operators in op_choices:
                value = self.operands[0]
                for idx, operand in enumerate(self.operands[1:]):
                    operator = operators[idx]
                    if operator == "+":
                        value += operand
                    elif operator == "*":
                        value *= operand
                    elif operator == "||":
                        # Example:
                        # 6 * 8 || 6 * 15
                        # 48 || 6 * 15
                        # 486 * 15
                        # 7290
                        value = int(str(value) + str(operand))

                if value == self.result:
                    self.operators = list(operators)
                    self.solveable = True
                    break


class BridgeRepair:
    def __init__(self, filename:str, operators:list[str]):
        self.__data_file = filename
        self.__operators = operators
        self.equations = []

        self.__load_equations()


    def __load_equations(self):
        """ Load the Calibration Equations Data """
        with open(self.__data_file) as fptr:
            line = fptr.readline()
            while line:
                self.equations.append(
                    Equation.from_str(line.strip())
                )

                line = fptr.readline()


    def calibration_result(self):
        """
        Sum the results from each valid/solveable calibration equation.
        """
        total_result = 0
        for equation in self.equations:
            equation.solve(self.__operators)
            if equation.solveable:
                total_result += equation.result

        return total_result
