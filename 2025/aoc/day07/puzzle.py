from functools import cache

import aoc.lib.constants as const
from aoc.lib.location import Location
from aoc.lib.puzzle import Puzzle


class Node:
    TYPE_START = "S"
    TYPE_SPLITTER = "^"
    TYPE_EMPTY = "."
    TYPE_BEAM = "|"

    def __init__(self, ntype, location):
        self.type = ntype
        self.loc = location

        self.paths = []

    def __str__(self):
        return f"Node({self.type},{self.loc})"

    def __eq__(self, other):
        return self.loc == other.loc

    def __hash__(self):
        return hash(self.loc)

    def add_path(self, node):
        self.paths.append(node)


class Laboratories(Puzzle):
    """AOC-2025 // Day07 -- Laboratories"""

    def __init__(self, input_file, **kwargs):
        super().__init__(input_file, **kwargs)

        self.__tachyon_grid = []
        self._read_input(self.__parse_input)

        start_r = 0
        start_c = self.__tachyon_grid[0].index(Node.TYPE_START)
        self.__start_loc = Location(start_r, start_c)
        self.__exit_row = len(self.__tachyon_grid) - 1

    def __parse_input(self, line):
        self.__tachyon_grid.append(list(line))

    def _part1(self):
        self._debug(f"Start Loc: {self.__start_loc}")

        split_count = 0
        beams = set()
        beams.add(self.__start_loc.nearby(const.S))
        while beams:
            self._debug(f"  -> Beam Count: [{len(beams)}]")
            beams_to_add = set()
            beams_to_remove = set()
            for beam in beams:
                if beam.row != self.__exit_row:
                    # look south of beam to see what's there
                    next_loc = beam.nearby(const.S)
                    next_space = self.__tachyon_grid[next_loc.row][next_loc.col]

                    if next_space == Node.TYPE_SPLITTER:
                        split_count += 1
                        self._debug(f"  -> Split Count: [{split_count}]")

                        # Split the beam into two new beams
                        new_beam1 = beam.nearby(const.SW)
                        beams_to_add.add(new_beam1)

                        new_beam2 = beam.nearby(const.SE)
                        beams_to_add.add(new_beam2)
                    elif next_space == Node.TYPE_EMPTY:
                        # Move down/S
                        new_loc = beam.nearby(const.S)
                        # Add new beam pos
                        beams_to_add.add(new_loc)

                # Remove the old beam
                beams_to_remove.add(beam)

            beams.difference_update(beams_to_remove)
            beams.update(beams_to_add)

        return split_count

    @cache  # noqa: B019
    def __traverse_manifold(self, curr_node):
        timelines = 0
        new_nodes = []

        match curr_node.type:
            case Node.TYPE_START | Node.TYPE_EMPTY:
                loc = curr_node.loc.nearby(const.S)
                ntype = self.__tachyon_grid[loc.row][loc.col]
                node = Node(ntype, loc)
                new_nodes.append(node)
            case Node.TYPE_SPLITTER:
                timelines += 1
                self._debug(f"-> Timelines: {timelines}")
                for direction in (const.SE, const.SW):
                    loc = curr_node.loc.nearby(direction)
                    ntype = self.__tachyon_grid[loc.row][loc.col]
                    node = Node(ntype, loc)
                    new_nodes.append(node)

        for node in new_nodes:
            if node.loc.row < self.__exit_row:
                curr_node.add_path(node)
                timelines += self.__traverse_manifold(node)
            else:
                self._debug(f"-> Exit at {node}")

        return timelines

    def _part2(self):
        start_node = Node(Node.TYPE_START, self.__start_loc)
        self._debug(start_node)

        # Start in the current timeline
        timelines = 1

        # Also builds a tree of nodes, but it's not used
        timelines += self.__traverse_manifold(start_node)

        return timelines
