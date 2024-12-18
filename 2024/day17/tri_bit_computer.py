import re

class Instructions:

    OPERAND_LITERAL = 1
    OPERAND_COMBO = 2

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
        e_op = Instructions.eval_operand(
            Instructions.OPERAND_COMBO, operand, regs)
        num = regs.get("A")
        denom = 2 ** e_op

        regs.set("A", num // denom)


    @staticmethod
    def bxl(operand, regs):
        """
        The bxl instruction (opcode 1) calculates the bitwise XOR of register B
        and the instruction's literal operand, then stores the result in
        register B.
        """
        op1 = regs.get("B")
        op2 = Instructions.eval_operand(
            Instructions.OPERAND_LITERAL, operand, regs)

        regs.set("B", op1 ^ op2)


    @staticmethod
    def bst(operand, regs):
        """
        The bst instruction (opcode 2) calculates the value of its combo
        operand modulo 8 (thereby keeping only its lowest 3 bits), then writes
        that value to the B register.
        """
        e_op = Instructions.eval_operand(
            Instructions.OPERAND_COMBO, operand, regs)
        regs.set("B", e_op % 8)


    @staticmethod
    def jnz(operand, regs):
        """
        The jnz instruction (opcode 3) does nothing if the A register is 0.
        However, if the A register is not zero, it jumps by setting the
        instruction pointer to the value of its literal operand; if this
        instruction jumps, the instruction pointer is not increased by 2 after
        this instruction.
        """
        jumped = False
        e_op = Instructions.eval_operand(
            Instructions.OPERAND_LITERAL, operand, regs)
        a_value = regs.get("A")
        if a_value != 0:
            jumped = True
            regs.set("IP", e_op)

        return {"jumped": jumped}


    @staticmethod
    def bxc(operand, regs):
        """
        The bxc instruction (opcode 4) calculates the bitwise XOR of register B
        and register C, then stores the result in register B. (For legacy
        reasons, this instruction reads an operand but ignores it.)
        """
        op1 = regs.get("B")
        op2 = regs.get("C")
        regs.set("B", op1 ^ op2)


    @staticmethod
    def out(operand, regs):
        """
        The out instruction (opcode 5) calculates the value of its combo
        operand modulo 8, then outputs that value. (If a program outputs
        multiple values, they are separated by commas.)
        """
        e_op = Instructions.eval_operand(
            Instructions.OPERAND_COMBO, operand, regs)
        value = e_op % 8
        return {"out": value}


    @staticmethod
    def bdv(operand, regs):
        """
        The bdv instruction (opcode 6) works exactly like the adv instruction
        except that the result is stored in the B register. (The numerator is
        still read from the A register.)
        """
        e_op = Instructions.eval_operand(
            Instructions.OPERAND_COMBO, operand, regs)
        num = regs.get("A")
        denom = 2 ** e_op

        regs.set("B", num // denom)


    @staticmethod
    def cdv(operand, regs):
        """
        The cdv instruction (opcode 7) works exactly like the adv instruction
        except that the result is stored in the C register. (The numerator is
        still read from the A register.)
        """
        e_op = Instructions.eval_operand(
            Instructions.OPERAND_COMBO, operand, regs)
        num = regs.get("A")
        denom = 2 ** e_op

        regs.set("C", num // denom)

    @staticmethod
    def eval_operand(op_type, operand, regs):
        """
        - Combo operands 0 through 3 represent literal values 0 through 3.
        - Combo operand 4 represents the value of register A.
        - Combo operand 5 represents the value of register B.
        - Combo operand 6 represents the value of register C.
        - Combo operand 7 is reserved and will not appear in valid programs.
        """
        value = None

        if op_type == Instructions.OPERAND_LITERAL:
            value = operand
        elif op_type == Instructions.OPERAND_COMBO:
            if operand <= 3:
                value = operand
            elif operand == 4:
                value = regs.get("A")
            elif operand == 5:
                value = regs.get("B")
            elif operand == 6:
                value = regs.get("C")
            elif operand == 7:
                pass
            else:
                raise RuntimeError(f"Invalid Operand [{operand}]")

        return value


    @staticmethod
    def from_opcode(opcode):
        instruction = None
        if opcode == 0:
            instruction = Instructions.adv
        elif opcode == 1:
            instruction = Instructions.bxl
        elif opcode == 2:
            instruction = Instructions.bst
        elif opcode == 3:
            instruction = Instructions.jnz
        elif opcode == 4:
            instruction = Instructions.bxc
        elif opcode == 5:
            instruction = Instructions.out
        elif opcode == 6:
            instruction = Instructions.bdv
        elif opcode == 7:
            instruction = Instructions.cdv

        return instruction


class RegisterBank:
    def __init__(self, reg_ids):
        self.__data = {}
        for rid in reg_ids:
            self.__data[rid] = 0


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
    REG_IP = "IP" # Instruction Pointer

    REGISTERS = (REG_A, REG_B, REG_C, REG_IP)

    def __init__(self, program_file, **kwargs):
        self.__program_file = program_file

        self.__registers = RegisterBank(self.REGISTERS)
        self.__program = []

        self.__debug = kwargs.get("debug", False)

        self.__read_program()


    @property
    def registers(self):
        return self.__registers


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


    def __trace(self, msg):
        if self.__debug:
            print(msg)


    def execute(self):
        self.__trace(f"BEGIN")
        self.__registers.set(self.REG_IP, 0)

        halted = False
        stdout = []
        while not halted:
            ip = self.__registers.get(self.REG_IP)
            self.__trace(f"...IP [{ip}] {self.__program}")
            if self.__registers.get(self.REG_IP) >= len(self.__program):
                self.__trace("...HALT")
                halted = True
                self.__trace("END")
            else:
                opcode = self.__program[ip]
                operand = self.__program[ip + 1]

                self.__trace(f"...{opcode} {operand} ")

                inst = Instructions.from_opcode(opcode)
                output = inst(operand, self.__registers)

                if output is not None and "out" in output:
                    value = output.get("out")
                    self.__trace(f"...OUT => {value}")
                    stdout.append(str(value))

                # TODO: flip this conditional
                if inst == Instructions.jnz and output.get("jumped"):
                    pass
                else:
                    self.__trace(f"...inc IP [{ip+2}]")
                    self.__registers.set(self.REG_IP, ip + 2)

                self.__trace(f"...REG {self.__registers}")

            if self.__debug:
                input("> ")

        return ",".join(stdout)
