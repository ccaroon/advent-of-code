import re

class Instructions:
    @staticmethod
    def adv(operand, regs):
        """
        The adv instruction (opcode 0) performs division. The numerator is the
        value in the A register. The denominator is found by raising 2 to the
        power of the instruction's combo operand. (So, an operand of 2 would
        divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result
        of the division operation is truncated to an integer and then written
        to the A register.
        """

        num = regs.get("A")
        denom = 2 ** operand

        regs.set("A", num // denom)


    @staticmethod
    def bxl(operand, regs):
        """
        The bxl instruction (opcode 1) calculates the bitwise XOR of register B
        and the instruction's literal operand, then stores the result in
        register B.
        """
        op1 = regs.get("B")
        op2 = operand

        regs.set("B", op1 ^ op2)


    @staticmethod
    def from_opcode(opcode):
        instruction = None
        if opcode == 0:
            instruction = Instructions.adv
        elif opcode == 1:
            instruction = Instructions.bxl

        return instruction


class RegisterBank:
    def __init__(self, reg_ids):
        self.__data = {}
        for rid in reg_ids:
            self.__data[rid] = None


    def __str__(self):
        return str(self.__data)


    def get(self, rid):
        return self.__data.get(rid)


    def set(self, rid, value):
        self.__data[rid] = value


class TriBitComputer:

    REG_A = "A"
    REG_B = "B"
    REG_C = "C"

    REGISTERS = (REG_A, REG_B, REG_C)

    def __init__(self, program_file):
        self.__program_file = program_file

        self.__instruction_ptr = 0

        self.__registers = RegisterBank(self.REGISTERS)
        self.__program = []


        self.__read_program()


    def __str__(self):
        return f"{self.__program} // {self.__registers}"


    def __read_program(self):
        self.__program = []
        valid_regs = "|".join(self.REGISTERS)
        with open(self.__program_file, "r") as fptr:
            while line := fptr.readline():
                reg_match = re.match(rf"Register\s+({valid_regs}):\s+(\d+)", line)
                if reg_match:
                    reg_id = reg_match.group(1)
                    reg_value = int(reg_match.group(2))
                    self.__registers.set(reg_id, reg_value)

                prg_match = re.match(r"Program:\s+(.*)", line)
                if prg_match:
                    codes = prg_match.group(1).split(",")
                    self.__program = [int(value) for value in codes]


    def __parse_operand(self, operand):
        """
        - Combo operands 0 through 3 represent literal values 0 through 3.
        - Combo operand 4 represents the value of register A.
        - Combo operand 5 represents the value of register B.
        - Combo operand 6 represents the value of register C.
        - Combo operand 7 is reserved and will not appear in valid programs.
        """
        value = None
        if operand <= 3:
            value = operand
        elif operand == 4:
            value = self.__registers.get(self.REG_A)
        elif operand == 5:
            value = self.__registers.get(self.REG_B)
        elif operand == 6:
            value = self.__registers.get(self.REG_B)
        elif operand == 7:
            pass
        else:
            raise RuntimeError(f"Invalid Operand [{operand}]")

        return value


    def execute(self):
        halted = False

        while not halted:
            opcode = self.__program[self.__instruction_ptr]
            operand = self.__program[self.__instruction_ptr + 1]

            inst = Instructions.from_opcode(opcode)
            # TODO: how to know what param are needed where for opcode?
            inst(self.__parse_operand(operand), self.__registers)

            # TODO: unless jump
            self.__instruction_ptr += 2

            if self.__instruction_ptr > len(self.__program):
                halted = True






#
