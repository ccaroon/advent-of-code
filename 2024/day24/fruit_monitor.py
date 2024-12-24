import re

class Operation:
    OP_AND = "AND"
    OP_OR = "OR"
    OP_XOR = "XOR"

    def __init__(self, input1, input2, operator:str):
        self.__input1 = input1
        self.__input2 = input2
        self.__operator = operator


    @property
    def input1(self):
        return self.__input1


    @property
    def input2(self):
        return self.__input2


    @property
    def result(self):
        return self.__execute()


    def connect(self, var_name, value):
        match var_name:
            case self.__input1:
                self.__input1 = value
            case self.__input2:
                self.__input2 = value


    def connected(self):
        in1_connected = False
        if isinstance(self.__input1, Operation):
            in1_connected = self.__input1.connected()
        elif isinstance(self.__input1, bool):
            in1_connected = True

        in2_connected = False
        if isinstance(self.__input2, Operation):
            in2_connected = self.__input2.connected()
        elif isinstance(self.__input2, bool):
            in2_connected = True

        return in1_connected and in2_connected


    def __str__(self):
        return f"{self.__input1} {self.__operator} {self.__input2}"


    def __repr__(self):
        return str(self)


    def __resolve_input(self, value):
        result = None
        match value:
            case Operation():
                result = value.result
            case bool():
                result = value
            case _:
                raise TypeError(f"Invalid Type for AND Operation: [{type(value)}]")

        return result


    def __and(self):
        value1 = self.__resolve_input(self.__input1)
        value2 = self.__resolve_input(self.__input2)
        return value1 and value2


    def __or(self):
        value1 = self.__resolve_input(self.__input1)
        value2 = self.__resolve_input(self.__input2)
        return value1 | value2


    def __xor(self):
        value1 = self.__resolve_input(self.__input1)
        value2 = self.__resolve_input(self.__input2)
        return value1 ^ value2


    def __execute(self):
        result = None
        match self.__operator:
            case self.OP_AND:
                result = self.__and()
            case self.OP_OR:
                result = self.__or()
            case self.OP_XOR:
                result = self.__xor()
            case _:
                raise ValueError(f"Unknown Operation: [{self.__operator}]")

        return result




class FruitMonitor:
    def __init__(self, input_file):
        self.__input_file = input_file

        self.__variables = {}
        self.__operations = {}
        self.__read_input_file()


    def __read_input_file(self):
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                if ":" in line:
                    var_name, value = line.strip().split(":")
                    self.__variables[var_name] = bool(int(value))
                elif "->" in line:
                    # ntg XOR fgs -> mjb
                    match = re.match(
                        r"(\w{3})\s+(AND|OR|XOR)\s+(\w{3})\s+->\s+(\w{3})",
                        line
                    )
                    self.__operations[match.group(4)] = Operation(
                        self.__variables.get(match.group(1), match.group(1)),
                        self.__variables.get(match.group(3), match.group(3)),
                        match.group(2)
                    )


    def simulate(self):
        # Wire it Up!
        for var, op in self.__operations.items():
            if not op.connected():
                op.connect(op.input1, self.__operations.get(op.input1))
                op.connect(op.input2, self.__operations.get(op.input2))

        # Turn z vars into a bit string, then eval as an int
        var_names = list(self.__operations.keys())
        var_names.sort(reverse=True)
        z_bits = ""
        for var in var_names:
            if var.startswith("z"):
                op = self.__operations.get(var)
                z_bits += "1" if op.result else "0"

        return int(z_bits, base=2)







#
