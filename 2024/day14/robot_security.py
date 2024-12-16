import re

from shared.direction import Direction
from shared.location import Location
from velocity import Velocity

class Robot:
    def __init__(self, pos:Location, velocity:Velocity, rng:tuple):
        self.__position = pos
        self.__velocity = velocity

        self.__range_x = rng[1]
        self.__range_y = rng[0]

        self.__xdir = Direction("R")
        if velocity.dx < 0:
            self.__xdir = Direction("L")

        self.__ydir = Direction("D")
        if velocity.dy < 0:
            self.__ydir = Direction("U")


    @property
    def x(self):
        return self.__position.col


    @property
    def y(self):
        return self.__position.row


    def move(self):
        # TODO: optimize this
        # print(f"Move R,C: {self.__ydir.code}[{self.__velocity.dy}],{self.__xdir.code}[{self.__velocity.dx}]")

        for _ in range(abs(self.__velocity.dx)):
            self.__position.move(self.__xdir)
            if self.x >= self.__range_x:
                self.__position.col = 0
            elif self.x < 0:
                self.__position.col = self.__range_x - 1

        for _ in range(abs(self.__velocity.dy)):
            self.__position.move(self.__ydir)
            if self.y >= self.__range_y:
                self.__position.row = 0
            elif self.y < 0:
                self.__position.row = self.__range_y - 1


    def __eq__(self, other):
        return self.__location == other.__location and self.__velocity == other.__velocity


    def __str__(self):
        return f"Robot @ {self.__position} -> V{self.__velocity}"


    def __repr__(self):
        return str(self)


class RobotSecurity:
    AREA_ROWS = 103
    AREA_COLS = 101

    EMPTY = []

    def __init__(self, input_file):
        self.__input_file = input_file
        self.__robots = []
        self.__read_robot_data()

        self.__area_map = None
        self.__init_map()

        self.__place_robots()


    def __init_map(self):
        self.__area_map = []
        for ridx in range(self.AREA_ROWS):
            self.__area_map.append([])
            for _ in range(self.AREA_COLS):
                self.__area_map[ridx].append([])


    def __read_robot_data(self):
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                match = re.match(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)", line)
                px = int(match.group(1))
                py = int(match.group(2))
                vx = int(match.group(3))
                vy = int(match.group(4))
                # Must "reverse" the X & Y values since Location & Velocity
                # are Row + Col based.
                self.__robots.append(
                    Robot(Location(py, px), Velocity(vy, vx), (self.AREA_ROWS, self.AREA_COLS))
                )


    def __place_robots(self):
        for robot in self.__robots:
            self.__area_map[robot.y][robot.x].append(robot)


    def __str__(self):
        output = ""
        for ridx in range(self.AREA_ROWS):
            for cidx in range(self.AREA_COLS):
                rcount = len(self.__area_map[ridx][cidx])
                if rcount == 0:
                    output += " ."
                else:
                    output += f"{rcount:2d}"

            output += "\n"

        return output

    @property
    def robots(self):
        return self.__robots


    def __quadrant(self, pos:Location):
        quadrant = 0
        if pos.row < self.AREA_ROWS // 2:
            if pos.col < self.AREA_COLS // 2:
                quadrant = 1
            elif pos.col > self.AREA_COLS // 2:
                quadrant = 2
        elif pos.row > self.AREA_ROWS // 2:
            if pos.col < self.AREA_COLS // 2:
                quadrant = 3
            elif pos.col > self.AREA_COLS // 2:
                quadrant = 4

        return quadrant


    def safety_factor(self):
        counts = {
            1: 0,
            2: 0,
            3: 0,
            4: 0
        }
        for ridx in range(self.AREA_ROWS):
            for cidx in range(self.AREA_COLS):
                quad = self.__quadrant(Location(ridx, cidx))
                # quad == 0 == Skip in the middle // outside a quadrant
                if quad:
                    counts[quad] += len(self.__area_map[ridx][cidx])

        # print(counts)

        factor = 1
        for cnt in counts.values():
            factor *= cnt

        return factor


    def tick(self):
        """
        Adjust positions of robots by 1 tick (second)
        """
        for robot in self.__robots:
            self.__area_map[robot.y][robot.x].remove(robot)
            robot.move()
            self.__area_map[robot.y][robot.x].append(robot)


    def easter_egg(self):
        """
        If they're the same type of robots, they should have a hard-coded
        Easter egg: very rarely, most of the robots should arrange themselves
        into a picture of a Christmas tree.

        Iter
        """
        found = False

        # Look for at least `look_count` robot occupied spaces
        look_count = 10
        look_for = "@" * look_count
        for _, row in enumerate(self.__area_map):
            # Create a cross section of `__area_map` for this row that contains
            # an "@" for any space that has at least 1 robot
            # e.g: .........@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....
            cross_section = ""
            for robots in row:
                if len(robots) > 0:
                    cross_section += "@"
                else:
                    cross_section += "."

            if look_for in cross_section:
                print("-------------------------------------------------------")
                print(cross_section)
                print("-------------------------------------------------------")
                found = True
                break

        return found
