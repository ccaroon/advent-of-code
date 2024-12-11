# class DirectionMeta:
#     def __iter__(self):
#         return self.__ALL_DIRECTIONS


class Direction:
    # __metaclass__ = DirectionMeta

    __CODE_MAP = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    # __ALL_DIRECTIONS = [Direction(code) for code in __CODE_MAP.keys()]


    def __init__(self, code):
        self.__code = code


    @classmethod
    def enumerate(cls):
        return [Direction(code) for code in cls.__CODE_MAP.keys()]


    @property
    def code(self) -> str:
        return self.__code


    @property
    def rdelta(self) -> int:
        return self.__CODE_MAP[self.__code][0]


    @property
    def cdelta(self) -> int:
        return self.__CODE_MAP[self.__code][1]


    def __str__(self):
        return self.code


    def __repr__(self):
        return f"Direction('{self.code}','{self.rdelta}','{self.cdelta}')"
