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
    ROBOT = "@"
    EMPTY = "."

    def __init__(self, input_file:str):
        self.__input_file = input_file

        self.__area_map = None
        self.__moves = None
        self.__load_data()

        self.__robot = None
        self.__locate_robot()


    def __load_data(self):
        self.__area_map = []
        self.__moves = []
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                data = line.strip()
                # skip empty lines
                if data:
                    if data[0] == "#":
                        # map line
                        self.__area_map.append(list(data))
                    elif data[0] in ("^",">","v","<"):
                        # move line
                        for arrow in data:
                            self.__moves.append(Direction(arrow))


    def __str__(self):
        output = ""
        for row in self.__area_map:
            for thing in row:
                output += f"{thing} "

            output += "\n"

        return output


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
