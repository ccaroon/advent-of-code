import random
import re

class ClawMachine:

    PRIZES = (
        "Linux Sticker",
        "Rubik's Cube",
        "Pack of Grape Bubblegum",
        "Block of Cheese",
        "Rubber Chicken",
        "Metallic Dice",
        "Air Freshener (Pine)",
        "Python Sticker",
        "No Tea"
    )

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


    def push_a(self):
        self.__x += self.__button_a[0]
        self.__y += self.__button_a[1]


    def push_b(self):
        self.__x += self.__button_b[0]
        self.__y += self.__button_b[1]


    def reset(self):
        self.__x = 0
        self.__y = 0


    def grab(self):
        item = None
        if self.__x == self.__prize_loc[0] and self.__y == self.__prize_loc[1]:
            item = random.choice(self.PRIZES)

        return item


    def __str__(self):
        return f"A{self.__button_a} B{self.__button_b} P{self.__prize_loc}"


    def run_hack(self, a_presses, b_presses):
        self.reset()

        for _ in range(a_presses):
            self.push_a()

        for _ in range(b_presses):
            self.push_b()

        item = self.grab()

        return item


    def reverse_engineer(self):
        """
        Button A -> 3 tokens
        Button B -> 1 token

        Button A: X+94, Y+34
        Button B: X+22, Y+67
        Prize: X=8400, Y=5400

        A * 80 + B * 40
        3 * 80 + 1 * 40
        240    + 40
        280
        """
        a_pushes = 0
        b_pushes = 0

        # find largest X
        if self.__button_a[0] > self.__button_b[0]:
            px = self.__prize_loc[0]

            while self.__x < px:
                self.push_b()
                print(self.__x)
        # press until less than px value


        return (a_pushes, b_pushes)







#
