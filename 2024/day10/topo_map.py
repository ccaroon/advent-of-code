from direction import Direction
from location import Location

class TopoMap:
    TRAILHEAD = 0
    TRAILEND  = 9

    def __init__(self, filename:str) -> None:
        self.__filename = filename
        self.__area_map = None

        self.__load_map_data()


    def __load_map_data(self) -> None:
        self.__area_map = []
        with open(self.__filename, "r") as fptr:
            while line := fptr.readline():
                data = list(line.strip())
                data = [int(item) for item in data]
                self.__area_map.append(data)


    def __str__(self) -> str:
        output = ""
        for row in self.__area_map:
            for value in row:
                output += f"{value} "
            output += "\n"

        return output


    def mark_locations(self, locs:list[Location], marker:str) -> None:
        for loc in locs:
            self.__area_map[loc.row][loc.col] = marker


    def find_trailheads(self) -> list[Location]:
        trailheads = []
        for ridx, row in enumerate(self.__area_map):
            for cidx, _ in enumerate(row):
                if self.__area_map[ridx][cidx] == self.TRAILHEAD:
                    trailheads.append(Location(ridx, cidx))

        return trailheads


    def walk_trail(self, start:Location) -> set[Location]:
        """
        Walk the trail starting at the `start` location.

        Returns:
            set[Location]: List of unique TRAILEND locations that can be reached from `start`
        """
        trail_ends = set()
        branches = []

        # height of current/starting location
        height = self.__area_map[start.row][start.col]

        # If at the end of the trail, count it
        if height == self.TRAILEND:
            trail_ends.add(start)
        # Not at the end, continue walking
        else:
            # find all possible directions that can be moved in
            for direction in Direction.enumerate():
                if start.look(direction, self.__area_map) == height + 1:
                    branches.append(direction)

        # No branches means can't reach an end (9)
        if branches:
            # for each possible direction, move and recurse
            for branch_dir in branches:
                # branch_loc = start.copy().move(branch_dir)
                branch_loc = start.copy()
                branch_loc.move(branch_dir)
                trail_ends.update(self.walk_trail(branch_loc))

        return trail_ends


    def find_trails_ends(self, start) -> set[Location]:
        trail_ends = self.walk_trail(start)
        return trail_ends


    def score_trails(self) -> int:
        trailheads = self.find_trailheads()

        score = 0
        for thead in trailheads:
            trail_ends = self.find_trails_ends(thead)
            score += len(trail_ends)

        return score
