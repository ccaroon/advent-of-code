import re

class ClawMachine:
    def __init__(self, button_a:tuple, button_b:tuple, prize_loc:tuple):
        self.__button_a = button_a
        self.__button_b = button_b
        self.__prize_loc = prize_loc
        self.__x = 0
        self.__y = 0


    @classmethod
    def create(cls, input_file:str):
        machines = []
        with open(input_file) as fptr:
            button_a = None
            button_b = None
            prize = None
            while line := fptr.readline():
                if match := re.match(r"Button A: X\+(\d+),\s+Y\+(\d+)", line):
                    button_a = (int(match.group(1)), int(match.group(2)))
                elif match := re.match(r"Button B: X\+(\d+),\s+Y\+(\d+)", line):
                    button_b = (int(match.group(1)), int(match.group(2)))
                elif match := re.match(r"Prize: X=(\d+),\s+Y=(\d+)", line):
                    prize = (int(match.group(1)), int(match.group(2)))
                    if button_a and button_b and prize:
                        machines.append(
                            ClawMachine(button_a, button_b, prize)
                        )
                        button_a = None
                        button_b = None
                        prize = None

        return machines


    def __str__(self):
        return f"A{self.__button_a} B{self.__button_b} P{self.__prize_loc}"


    def cheat(self):
        pass
