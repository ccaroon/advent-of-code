import random

class Direction:
    __CODE_MAP = {
        # Compass dirs
        "N":  (-1, 0),
        "NE": (-1, 1),
        "E":  (0, 1),
        "SE": (1, 1),
        "S":  (1, 0),
        "SW": (1, -1),
        "W":  (0, -1),
        "NW": (-1,-1),
    }

    __ALT_CODE_MAP = {
        # Up, Down, Left, Right
        "U": __CODE_MAP["N"],
        "D": __CODE_MAP["S"],
        "L": __CODE_MAP["W"],
        "R": __CODE_MAP["E"],

        # Arrows
        "^": __CODE_MAP["N"],
        "v": __CODE_MAP["S"],
        "<": __CODE_MAP["W"],
        ">": __CODE_MAP["E"],
    }

    TURNS = {
        "N-L": "W",
        "N-R": "E",

        "E-L": "N",
        "E-R": "S",

        "S-L": "E",
        "S-R": "W",

        "W-L": "S",
        "W-R": "N"
    }


    VALID_CODES = tuple(__CODE_MAP.keys())

    def __init__(self, code:str):
        if code not in self.__CODE_MAP and code not in self.__ALT_CODE_MAP:
            raise ValueError(f"Invalid Direction Code '{code}'")

        self.__code = code
        self.__delta = self.__CODE_MAP.get(
            code,
            self.__ALT_CODE_MAP.get(code)
        )


    @classmethod
    def enumerate(cls, dirs=__CODE_MAP.keys()):
        return [Direction(code) for code in dirs]


    @property
    def code(self):
        return self.__code


    @property
    def row_delta(self):
        return self.__delta[0]


    @property
    def col_delta(self):
        return self.__delta[1]


    @classmethod
    def random(self):
        """
        Pick a random direction

        >>> d = Direction.random()
        >>> isinstance(d, Direction)
        True
        >>> d.code in Direction.VALID_CODES
        True
        """
        rand_code = random.choice(self.VALID_CODES)
        return Direction(rand_code)


    def copy(self):
        return Direction(self.code)


    def turn(self, direction):
        """
        >>> d = Direction("N")
        >>> new_dir = d.turn("L")
        >>> new_dir.code
        'W'

        >>> d = Direction("N")
        >>> new_dir = d.turn("R")
        >>> new_dir.code
        'E'

        >>> d = Direction("E")
        >>> new_dir = d.turn("L")
        >>> new_dir.code
        'N'

        >>> d = Direction("E")
        >>> new_dir = d.turn("R")
        >>> new_dir.code
        'S'

        >>> d = Direction("W")
        >>> new_dir = d.turn(Direction("R"))
        >>> new_dir.code
        'N'
        """
        dcode = direction
        if isinstance(direction, Direction):
            dcode = direction.code

        turn_code = f"{self.code}-{dcode}"
        return Direction(self.TURNS[turn_code])


    def __eq__(self, other):
        return self.code == other.code


    def __str__(self):
        return f"{self.__code} ({self.row_delta},{self.col_delta})"
