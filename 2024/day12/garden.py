# import copy

from shared.direction import Direction
from shared.location import Location

class Plot:

    BOT_LEFT = (0,0)
    BOT_RGHT = (1,0)
    TOP_LEFT = (0,1)
    TOP_RGHT = (1,1)

    SIDE_TOP = (TOP_LEFT, TOP_RGHT)
    SIDE_LEFT = (TOP_LEFT, BOT_LEFT)
    SIDE_BOTTOM = (BOT_LEFT, BOT_RGHT)
    SIDE_RIGHT = (TOP_RGHT, BOT_RGHT)

    VERTEX_NAMES = {
        "top-left": TOP_LEFT,
        "top-right": TOP_RGHT,
        "bottom-left": BOT_LEFT,
        "bottom-right": BOT_RGHT
    }

    def __init__(self, location):
        self.__loc = location

        # Plots are Square. They have 4 corners/vertices
        # self.__vertices = (
        #     self.TOP_LEFT, self.TOP_RGHT,
        #     self.BOT_LEFT, self.BOT_RGHT
        # )


    @property
    def location(self):
        return self.__loc


    def __str__(self):
        return str(self.__loc)


    def __eq__(self, other):
        return self.__loc == other.__loc


    def __hash__(self):
        return hash((self.__loc))


    def vertex_uid(self, name:str):
        """ Unique ID for one of the four vertexes by name """
        vtx = self.VERTEX_NAMES.get(name)
        if vtx is None:
            raise ValueError(f"Invalid Vertex Name: '{name}'")

        return f"{self.__loc.row},{self.__loc.col}:{vtx[0]},{vtx[1]}"


class Region:
    def __init__(self, plant_type:str):
        self.__plant_type = plant_type
        # The Locations of each Plot in the Region
        self.__plots = set()


    def __str__(self):
        return f"{self.__plant_type} : {self.__plots}"


    def __repr__(self):
        return str(self)


    def __contains__(self, item:Plot):
        return item in self.__plots


    @property
    def area(self):
        return len(self.__plots)


    @property
    def sides(self):
        """
        Each straight section of fence counts as a side, regardless of how long
        it is.

        This Region has 8 sides:

              1
            +---+
            | C | 2,3
          8 |   +---+
            | C   C |
            +---+   | 4
            6,7 | C |
                +---+
                  5

        This Region has 4 sides:

                1
            +-+-+-+-+
            |R R R R| 2
          4 |R R R R|
            +-+-+-+-+
                3

              0 1 2 3
            0 A A A A
            1 B B C D
            2 B B C C
            3 E E E C


            1 => 4
            2 => 4 - (2 + 2) = 0 => 4
            3 => 4 - (2)     = 2 => 6
            4 => 4 - (2)     = 2 => 8
        """
        # Number of sides == Number of vertices
        # Minimum number of sides is 4, i.e. it has to at least be a rectangle
        # Assume a Rectangle
        side_count = 4

        counted_vtxs = {}

        for plot in self.__plots[1:]:
            for direction in Direction.enumerate(("N","E","S","W")):
                non_shared_sides = 4
                # N => shares TOP
                if direction.code == "N":
                    shared_side = Plot.SIDE_TOP
                    # vtx1 =

                # S => shares BOTTOM
                # E => shares RIGHT
                # W => shares LEFT


                neighbor = plot.location + direction
                if neighbor in self.__plots:
                    pass

        return side_count


    @property
    def perimeter(self):
        """
        The perimeter of a region is the number of sides of garden plots in the
        region that do not touch another garden plot in the same region.
            +-+
            |C|    -> 3
            + +-+           |
            |C C|  -> 2,2   |=> 10
            +-+ +           |
              |C|  -> 3
              +-+
        """
        perimeter = 0

        for plot in self.__plots:
            # Assume 4 side are open
            plot_perimeter = 4
            # Look for sides that touch other plots
            # and reduce the plot_perimeter count
            for direction in Direction.enumerate(("N","E","S","W")):
                neighbor = self.get_plot(plot.location + direction)
                if neighbor in self.__plots:
                    plot_perimeter -= 1

            perimeter += plot_perimeter

        return perimeter


    @property
    def is_empty(self):
        return len(self.__plots) == 0


    def get_plot(self, location:Location):
        found_plot = None
        for plot in self.__plots:
            if plot.location == location:
                found_plot = plot
                break

        return found_plot


    def add_plot(self, location:Location):
        self.__plots.add(Plot(location))


    def remove_plot(self, location:Location):
        plot = self.get_plot(location)
        if plot in self.__plots:
            self.__plots.remove(location)


    def touches(self, other):
        is_touching = False

        other_loc = None
        if isinstance(other, Location):
            other_loc = other
        elif isinstance(other, Plot):
            other_loc = other.location

        for plot in self.__plots:
            if plot.location.adjacent_to(other_loc):
                is_touching = True
                break

        return is_touching



class Garden:
    """
    Garden

    Terminology:
        Plant Type  -> (A,X,O,M, etc)
        Plot        -> Many Plants of the same type
                    -> Single Row/Col
        Region      -> Made up of many Plots of same Plant type (Touching Plots)
    """

    MARKER = "."

    def __init__(self, filename:str, **kwargs):
        self.__debug = kwargs.get("debug", False)

        self.__filename = filename

        self.__rows = None
        self.__cols = None
        self.__garden_map = None
        self.__load_garden_map()

        self.__plant_types = 0
        self.__regions = []
        self.__identify_regions()


    @property
    def plant_types(self):
        return self.__plant_types


    @property
    def regions(self):
        return self.__regions


    def __load_garden_map(self):
        self.__print_dbg("Loading Garden Map")

        self.__garden_map = []
        with open(self.__filename, "r") as fptr:
            while line := fptr.readline():
                self.__garden_map.append(list(line.strip()))

        self.__rows = len(self.__garden_map)
        self.__cols = len(self.__garden_map[0])


    def __str__(self) -> str:
        output = ""
        for row in self.__garden_map:
            output += " ".join(row) + "\n"

        return output


    def __make_regions(self, plant_type:str, plot_locs:list[Location]):
        self.__print_dbg("Making Regions")
        curr_plot_count = len(plot_locs)

        # Start a region
        region = Region(plant_type)
        self.__regions.append(region)
        region.add_plot(plot_locs.pop(0))
        new_plot_count = curr_plot_count - 1

        # Look for plot locs that touch the Region
        # Until the list of plots stops getting smaller, i.e. no more plots
        # touch this region
        while new_plot_count < curr_plot_count:
            curr_plot_count = new_plot_count
            tmp_locs = plot_locs.copy()
            for loc in tmp_locs:
                # if loc touches it, add to region
                if region.touches(loc):
                    region.add_plot(loc)
                    plot_locs.remove(loc)
                # if not, skip it
            new_plot_count = len(plot_locs)

        # Keep going until all plot locs have been sorted into a Region
        if len(plot_locs) > 0:
            self.__make_regions(plant_type, plot_locs)


    def __identify_regions(self):
        """
        Creates a mapping from a plant type to a list of locations of
        plots that contain that plant type.

        Hands each entry in that list off to the Region Maker(tm)
        """
        self.__print_dbg("Identifying Regions")

        plot_map = {}
        for ridx in range(self.__rows):
            for cidx in range(self.__cols):
                loc = Location(ridx, cidx)
                plant_type = self.__garden_map[loc.row][loc.col]

                if plant_type in plot_map:
                    plot_map[plant_type].append(loc)
                else:
                    plot_map[plant_type] = [loc]

        for ptype, plot_locs in plot_map.items():
            self.__make_regions(ptype, plot_locs)

        self.__plant_types = len(plot_map.keys())


    def calculate_fencing(self, with_discount=False):
        self.__print_dbg("Calculating Fencing")
        total_cost = 0

        for region in self.__regions:
            if with_discount:
                # region_cost = region.area * region.sides
                region_cost = 0
                print(region)
            else:
                region_cost = region.area * region.perimeter
            # print(f"{region} = {region.area}x{region.perimeter} == ${region_cost}")
            total_cost += region_cost

        return total_cost


    def __print_dbg(self, msg):
        """ Print a message if `debug` is ON """
        if self.__debug:
            print(f"...{msg}...")








#
