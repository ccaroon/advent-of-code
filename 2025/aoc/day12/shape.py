class Shape:
    def __init__(self, data):
        self.__data = data

    def rotate(self):
        pass

    def flip(self):
        pass

    def __str__(self):
        rows = ["".join(row) for row in self.__data]
        return "\n".join(rows)
