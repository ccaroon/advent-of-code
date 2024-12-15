from shared.direction import Direction
from shared.location import Location


class Robot:
    def __init__(self, pos:Location):
        self.postion = pos


    @property
    def row(self):
        return self.postion.row


    @property
    def col(self):
        return self.postion.col


    def move(self, direction):
        self.postion.move(direction)


    def noop(self):
        pass


    def __str__(self):
        return str(self.postion)


class GPS(Location):
    def __init__(self, row, col):
        super().__init__(row, col)


    @property
    def coord(self):
        return (self.row * 100) + self.col


class Warehouse:

    WALL = "#"
    BOX = "O"
    BIG_BOX = ("[","]")
    ROBOT = "@"
    EMPTY = "."

    def __init__(self, input_file:str, super_size=False):
        self.__input_file = input_file
        self.__super_size = super_size

        self.__area_map = None
        self.__moves = None
        self.__load_data()

        self.__robot = None
        self.__locate_robot()


    def __load_data(self):
        """

        if `super_size`:
            - # => ## instead.
            - O => [] instead.
            - . => .. instead.
            - @ => @. instead.

        """
        self.__area_map = []
        self.__moves = []
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                row = []

                data = line.strip()
                if data:
                    for item in list(data):
                        if item == self.WALL:
                            row.append(self.WALL)
                            if self.__super_size:
                                row.append(self.WALL)
                        elif item == self.BOX:
                            if self.__super_size:
                                row.extend(self.BIG_BOX)
                            else:
                                row.append(self.BOX)
                        elif item == self.EMPTY:
                            row.append(self.EMPTY)
                            if self.__super_size:
                                row.append(self.EMPTY)
                        elif item == self.ROBOT:
                            row.append(self.ROBOT)
                            if self.__super_size:
                                row.append(self.EMPTY)
                        elif item in ("^",">","v","<"):
                            # move line
                            # for arrow in data:
                            self.__moves.append(Direction(item))
                    if row:
                        self.__area_map.append(row)


    def __str__(self):
        output = ""
        padding = " "
        if self.__super_size:
            padding = ""
        for row in self.__area_map:
            for thing in row:
                output += f"{thing}{padding}"

            output += "\n"

        return output


    # TODO: needs super_size update
    def __locate_boxes(self) -> list[GPS]:
        boxes = []
        for ridx, row in enumerate(self.__area_map):
            for cidx, thing in enumerate(row):
                if thing == self.BOX:
                    boxes.append(GPS(ridx, cidx))

        return boxes


    def __locate_robot(self):
        self.__robot = None
        for ridx, row in enumerate(self.__area_map):
            if self.__robot:
                break
            for cidx, thing in enumerate(row):
                if thing == self.ROBOT:
                    self.__robot = Robot(Location(ridx, cidx))
                    break


    @property
    def robot(self):
        return self.__robot


    @property
    def boxes(self):
        return self.__locate_boxes()


    # TODO: needs super size update
    def __move_robot(self, direction):
        robot = self.__robot
        next_pos = robot.postion.copy()
        next_pos.move(direction)
        next_space = self.__area_map[next_pos.row][next_pos.col]

        # if next space empty, just move robot
        if next_space == self.EMPTY:
            self.__area_map[robot.row][robot.col] = self.EMPTY
            robot.move(direction)
            self.__area_map[robot.row][robot.col] = self.ROBOT

        # if next space wall, noop
        elif next_space == self.WALL:
            robot.noop()

        # if next space box,
        elif next_space == self.BOX:
            boxes = []
            # lookup down the line until find a NOT BOX / !BOX
            while next_space == self.BOX:
                boxes.append(next_pos.copy())
                next_pos.move(direction)
                next_space = self.__area_map[next_pos.row][next_pos.col]

            if next_space == self.EMPTY:
                # if empty, move all boxes, then robot

                # move each box in direction
                for box in boxes:
                    box.move(direction)
                    self.__area_map[box.row][box.col] = self.BOX

                # move robot in direction
                self.__area_map[robot.row][robot.col] = self.EMPTY
                robot.move(direction)
                self.__area_map[robot.row][robot.col] = self.ROBOT

            elif next_space == self.WALL:
                # if wall, noop
                robot.noop()


    def activate_robot(self):
        # print(self)
        for direction in self.__moves:
            self.__move_robot(direction)
            # print(f"Move: {direction.code}")
            # print(self)


    def checksum(self):
        boxes = self.__locate_boxes()
        checksum = 0

        for box in boxes:
            checksum += box.coord

        return checksum
