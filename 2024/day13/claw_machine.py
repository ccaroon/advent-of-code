import random
import re


class Equation:
    def __init__(self, a, b, c):
        """
        Ax + By = C
        """
        self.a = a
        self.b = b
        self.c = c


    def __str__(self):
        return f"{self.a}x + {self.b}y = {self.c}"


    def __mul__(self, other):
        new_eq = None
        if isinstance(other, int):
            new_eq = Equation(
                self.a * other,
                self.b * other,
                self.c * other
            )
        else:
            raise ValueError(f"An Equation cannot be multiplied by a {type(other)}")

        return new_eq

    def __add__(self, other):
        new_eq = None
        if isinstance(other, Equation):
            new_eq = Equation(
                self.a + other.a,
                self.b + other.b,
                self.c + other.c
            )
        else:
            raise ValueError(f"An Equation cannot be added to a {type(other)}")

        return new_eq


class ClawMachine:

    UNIT_CORRECTION = 10000000000000

    PRIZES = (
        "Linux Sticker",
        "Rubik's Cube",
        "Pack of Grape Bubblegum",
        "Block of Cheese",
        "Rubber Chicken",
        "Metallic Dice",
        "Air Freshener (Pine)",
        "Python Sticker",
        "No Tea",
        "Happy SamX Sticker",
        "Stuffed Hippo",
        "Bogus Boquet",
        "Space Invader Plush"
    )

    def __init__(self, button_a:tuple, button_b:tuple, prize_loc:tuple):
        self.__button_a = button_a
        self.__button_b = button_b
        self.__prize_loc = prize_loc
        self.__x = 0
        self.__y = 0


    @classmethod
    def create(cls, input_file:str, **kwargs):
        correct_units = kwargs.get("correct_units", False)

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
                    if correct_units:
                        prize = (
                            prize[0] + cls.UNIT_CORRECTION,
                            prize[1] + cls.UNIT_CORRECTION
                        )

                    if button_a and button_b and prize:
                        machines.append(
                            ClawMachine(button_a, button_b, prize)
                        )
                        button_a = None
                        button_b = None
                        prize = None

        return machines


    def push_a(self, times=1):
        self.__x += self.__button_a[0] * times
        self.__y += self.__button_a[1] * times


    def push_b(self, times=1):
        self.__x += self.__button_b[0] * times
        self.__y += self.__button_b[1] * times


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


    # https://math.libretexts.org/Courses/Kansas_State_University/Your_Guide_to_Intermediate_Algebra/05%3A_Everything_else_you_need_to_know/5.07%3A_Solve_Systems_of_Linear_Equations_with_Two_Variables
    def __solve_eqs(self, eq_a:Equation, eq_b:Equation):
        """
        Ax + By = C
        """
        x = 0
        y = 0

        # Multiply each Equation by the othe's A coefficent
        # such that when the Equations are added, the A's cancel out
        # eliminating the X variable.
        step1a = eq_a * eq_b.a
        step1b = eq_b * (eq_a.a * -1)

        # Add EqA + EqB to eliminate X variable
        solve_for_y = step1a + step1b

        # Solve for Y
        y = solve_for_y.c // solve_for_y.b

        # Solve for X using the Y value found above
        x = (eq_a.c - eq_a.b * y) // eq_a.a

        return (x,y)


    def run_hack(self, a_presses, b_presses):
        self.reset()

        self.push_a(a_presses)
        self.push_b(b_presses)

        item = self.grab()

        return item


    def reverse_engineer(self):
        """
        Button A -> 3 tokens
        Button B -> 1 token
        """
        a_pushes = 0
        b_pushes = 0

        eq_a = Equation(
            self.__button_a[0],
            self.__button_b[0],
            self.__prize_loc[0]
        )
        # print(eq_a)

        eq_b = Equation(
            self.__button_a[1],
            self.__button_b[1],
            self.__prize_loc[1]
        )
        # print(eq_b)

        (a_pushes, b_pushes) = self.__solve_eqs(eq_a, eq_b)

        return (a_pushes, b_pushes)
