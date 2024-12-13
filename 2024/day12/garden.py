# import copy

from shared.direction import Direction
from shared.location import Location

class Region:
    def __init__(self, plant_type:str):
        self.__plant_type = plant_type
        # The Locations of each Plot in the Region
        self.__plot_locations = set()


    def __str__(self):
        return f"{self.__plant_type} : {self.__plot_locations}"


    def __repr__(self):
        return str(self)


    def __contains__(self, item:Location):
        return item in self.__plot_locations


    @property
    def area(self):
        return len(self.__plot_locations)


    @property
    def perimeter(self):
        """
        The perimeter of a region is the number of sides of garden plots in the
        region that do not touch another garden plot in the same region.
            +-+
            |C|    -> 3
            + +-+
            |C C|  -> 2,2
            +-+ +
              |C|  -> 3
              +-+
        """
        perimiter = 0

        for plot_loc in self.__plot_locations:
            # Assume 4 side are open
            plot_perimeter = 4
            # Look for sides that touch other plots
            # and reduce the plot_perimeter count
            for direction in Direction.enumerate(("N","E","S","W")):
                neighbor = plot_loc + direction
                if neighbor in self.__plot_locations:
                    plot_perimeter -= 1

            perimiter += plot_perimeter

        return perimiter


    @property
    def is_empty(self):
        return len(self.__plot_locations) == 0


    def add_plot(self, location:Location):
        self.__plot_locations.add(location)


    def remove_plot(self, location:Location):
        if location in self.__plot_locations:
            self.__plot_locations.remove(location)


    def touches(self, location:Location):
        is_touching = False

        for plot_loc in self.__plot_locations:
            if location.adjacent_to(plot_loc):
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

    def __init__(self, filename:str):
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


    def calculate_fencing(self):
        total_cost = 0

        for region in self.__regions:
            region_cost = region.area * region.perimeter
            # print(f"{region} = {region.area}x{region.perimeter} == ${region_cost}")
            total_cost += region_cost

        return total_cost
