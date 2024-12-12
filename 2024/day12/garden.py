from shared.direction import Direction
from shared.location import Location

class Region:
    def __init__(self, plant_type:str, plots:list):
        self.plant_type = plant_type
        # The Locations of each Plot in the Region
        self.plots = plots


class Garden:
    """
    Garden

    Terminology:
        Plant Type  -> (A,X,O,M, etc)
        Plot        -> Many Plants of the same type
                    -> Single Row/Col
        Region      -> Made up of many Plots of same Plant type (Touching Plots)
    """
    def __init__(self, filename:str):
        self.__filename = filename

        self.__rows = None
        self.__cols = None
        self.__garden_map = None
        self.__load_garden_map()

        self.__regions = []



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


    def __map_region(self, ptype:str, location:Location):
        pass


    def __identify_regions(self):
        for ridx in range(self.__rows):
            for cidx in range(self.__cols):
                loc = Location(ridx, cidx)
                plant_type = self.__garden_map[loc.row][loc.col]
                region = self.__map_region(plant_type, loc)
                self.__regions.append(region)







#
