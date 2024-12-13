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
            plot_perimeter = 4
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


    def __identify_regions(self):
        region_map = {}
        for ridx in range(self.__rows):
            for cidx in range(self.__cols):
                loc = Location(ridx, cidx)
                plant_type = self.__garden_map[loc.row][loc.col]

                part_of_existing_region = False
                if plant_type in region_map:
                    # TODO: Clean up add/remove logic
                    added = False
                    for region in region_map[plant_type]:
                        if added:
                            region.remove_plot(loc)
                            for direction in Direction.enumerate(("N","E","S","W")):
                                # if loc.look(direction, self.__garden_map) == plant_type:
                                region.remove_plot(loc + direction)
                        elif region.touches(loc):
                            part_of_existing_region = True

                            region.add_plot(loc)

                            # Also add all locs to NESW
                            for direction in Direction.enumerate(("N","E","S","W")):
                                if loc.look(direction, self.__garden_map) == plant_type:
                                    region.add_plot(loc + direction)

                            added = True

                if not part_of_existing_region:
                    new_region = Region(plant_type)
                    new_region.add_plot(loc)
                    if plant_type not in region_map:
                        region_map[plant_type] = []

                    region_map[plant_type].append(new_region)

        self.__plant_types = len(region_map.keys())

        for region_list in region_map.values():
            non_empty = filter(lambda region: not region.is_empty, region_list)
            self.__regions.extend(non_empty)


    def calculate_fencing(self):
        total_cost = 0

        for region in self.__regions:
            region_cost = region.area * region.perimeter
            print(f"{region} = {region.area}x{region.perimeter} == ${region_cost}")
            total_cost += region_cost

        return total_cost
