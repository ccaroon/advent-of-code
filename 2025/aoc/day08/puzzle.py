import itertools
import pprint

from aoc.lib.point import Point
from aoc.lib.puzzle import Puzzle


class Playground(Puzzle):
    """AOC-2025 // Day08 -- Playground"""

    def __init__(self, input_file, **kwargs):
        super().__init__(input_file, **kwargs)

        self.__data = []
        self._read_input(self.__parse_input)

    def __parse_input(self, line):
        (x, y, z) = line.split(",", 3)
        self.__data.append(Point(int(x), int(y), int(z)))

    def _part1(self):
        # find the two junction boxes which are closest together but aren't
        # ...already directly connected
        #
        circuits = []
        combos = itertools.combinations(self.__data, 2)
        dists = []
        for pair in combos:
            dist = pair[0].distance_to(pair[1])
            # ((Point1, Point2), distance)
            dists.append((pair, dist))

        sorted_dists = sorted(dists, key=lambda d: d[1])
        # pprint.pprint(sorted_dists)

        for data in sorted_dists[0:10]:
            points = data[0]
            # dist = data[1]

            found_circuit = False
            for circuit in circuits:
                if points[0] in circuit or points[1] in circuit:
                    circuit.update(points)
                    found_circuit = True

            # add a new circuit
            if not found_circuit:
                circuits.append(set(points))

        pprint.pprint(circuits)
        print(len(circuits))

    def _part2(self):
        pass
