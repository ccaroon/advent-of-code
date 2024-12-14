class Velocity:
    def __init__(self, dr, dc):
        self.__dr = dr
        self.__dc = dc


    @property
    def dx(self):
        return self.__dc


    @property
    def dy(self):
        return self.__dr


    def __eq__(self, other):
        return self.__dr == other.__dr and self.__dc == other.__dc


    def __str__(self):
        return f"({self.__dr},{self.__dc})"
