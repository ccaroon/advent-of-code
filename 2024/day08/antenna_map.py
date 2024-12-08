# import copy
import itertools

class Location:
    def __init__(self, row, col):
        self.row = row
        self.col = col


    def __repr__(self):
        return f"({self.row}, {self.col})"


    def __str__(self):
        return repr(self)


    def __eq__(self, other):
        """
        >>> Location(2,34) == Location(2,34)
        True

        >>> Location(42, 77) == Location(34, 765)
        False
        """
        return self.row == other.row and self.col == other.col


    def copy(self):
        return Location(self.row, self.col)


    def move(self, rd, cd):
        self.row += rd
        self.col += cd


    def distance_to(self, other):
        """
        >>> loc = Location(5,6)
        >>> other = Location(8,8)
        >>> loc.distance_to(other)
        (3, 2)

        >>> loc = Location(8,8)
        >>> other = Location(5,6)
        >>> loc.distance_to(other)
        (3, 2)
        """

        rdelta = abs(other.row - self.row)
        cdelta = abs(other.col - self.col)

        return (rdelta, cdelta)


class AntennaMap:
    EMPTY = "."
    ANTINODE = "#"

    def __init__(self, filename:str):
        self.__filename = filename
        self.__area_map = None
        self.__antenna_locs = None
        self.__antinode_locs = None

        self.__read_map()
        self.__find_antennas()


    @property
    def antinodes(self):
        return self.__antinode_locs


    @property
    def antennas(self):
        return self.__antenna_locs


    def __read_map(self):
        self.__area_map = []
        with open(self.__filename, "r") as fptr:
            while line := fptr.readline():
                data = list(line.strip())
                self.__area_map.append(data)


    def __str__(self):
        return self.format(self.__area_map)


    def format(self, amap):
        output = "   "

        for idx in range(len(amap[0])):
            output += f"{idx:02d} "

        output += "\n"

        for idx, row in enumerate(amap):
            output += f"{idx:02d} " + "  ".join(row) + "\n"

        return output


    def __find_antennas(self) -> dict:
        self.__antenna_locs = {}
        for ridx, row in enumerate(self.__area_map):
            for cidx, _ in enumerate(row):
                atype = self.__area_map[ridx][cidx]
                if atype != self.EMPTY:
                    if atype in self.__antenna_locs:
                        self.__antenna_locs[atype].append(Location(ridx, cidx))
                    else:
                        self.__antenna_locs[atype] = [Location(ridx,cidx)]


    def __valid_location(self, loc):
        return (
            loc.row >= 0 and loc.row < len(self.__area_map)
            and
            loc.col >= 0 and loc.col < len(self.__area_map[0])
        )


    def antinode_scan(self):
        self.__antinode_locs = []
        for _, locations in self.__antenna_locs.items():
            # print(f"{atype}: {locations}")
            loc_pairs = tuple(itertools.combinations(locations, r=2))

            for pair in loc_pairs:
                loc1 = pair[0]
                loc2 = pair[1]

                dist = loc1.distance_to(loc2)

                # TODO: Refactor -- use compass directions? from loc1 to loc2?
                # top node -- -
                # bot node -- +
                # rt node -- +
                # lf node -- -
                vrt = 0
                hrz = 0
                if loc1.row < loc2.row:
                    vrt = -1
                    top_loc = loc1
                    bot_loc = loc2
                else:
                    vrt = 1
                    top_loc = loc2
                    bot_loc = loc1

                if loc1.col < loc2.col:
                    hrz = -1
                else:
                    hrz = 1

                # Find location for TOP AntiNode
                node_loc = top_loc.copy()
                node_loc.move(dist[0] * vrt, dist[1] * hrz)
                if self.__valid_location(node_loc) and node_loc not in self.__antinode_locs:
                    self.__antinode_locs.append(node_loc)

                # Find location for BOTTOM AnitNode
                node_loc = bot_loc.copy()
                node_loc.move(dist[0] * vrt * -1, dist[1] * hrz * -1)
                if self.__valid_location(node_loc) and node_loc not in self.__antinode_locs:
                    self.__antinode_locs.append(node_loc)



#
