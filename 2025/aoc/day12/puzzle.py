import re

from aoc.day12.region import Region
from aoc.day12.shape import Shape
from aoc.lib.puzzle import Puzzle


class ChristmasTreeFarm(Puzzle):
    """AOC-2025 // Day12 -- Christmas Tree Farm"""

    def __init__(self, input_file, **kwargs):
        super().__init__(input_file, **kwargs)

        self.__shapes = []
        self.__regions = {}
        self.__gift_maps = []

        self.__shape_data = None
        self._read_input(self.__parse_input)

    def __parse_input(self, line):
        if self.__shape_data is not None:
            if not line:
                # Create Shape instance & add to __shapes
                self.__shapes.append(Shape(self.__shape_data))
                self.__shape_data = None
            else:
                self.__shape_data.append(list(line))
        elif re.match(r"^\d+:$", line):
            self.__shape_data = []
        elif re.match(r"^\d+x\d+:", line):
            size, gift_map = line.split(":")
            width, height = size.split("x")
            if size not in self.__regions:
                self.__regions[size] = Region(int(width), int(height))
            # TODO: need to associate with region
            self.__gift_maps.append(gift_map.strip().split(" "))

    def _part1(self):
        print(len(self.__shapes))

        # for shape in self.__shapes:
        #     print(shape, "\n----------")

    def _part2(self):
        pass
