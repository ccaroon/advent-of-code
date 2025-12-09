import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Point({self.x},{self.y},{self.z})"

    def distance_to(self, other):
        dx = (self.x - other.x) ** 2
        dy = (self.y - other.y) ** 2
        dz = (self.z - other.z) ** 2

        return math.sqrt(dx + dy + dz)
