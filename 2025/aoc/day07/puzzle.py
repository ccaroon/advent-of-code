import aoc.lib.constants as const
from aoc.lib.puzzle import Puzzle


class Laboratories(Puzzle):
    """AOC-2025 // Day07 -- Laboratories"""

    START = "S"
    SPLITTER = "^"
    EMPTY = "."
    BEAM = "|"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # list fo active beam positions
        self.__tachyon_grid = []
        self._read_input(self.__parse_input)

        # TOOD: move this to part1?
        start_r = 0
        start_c = self.__tachyon_grid[0].index(self.START)
        self.__start_pos = const.Position(start_r, start_c)
        self.__beams = set()
        self.__beams.add(const.move(self.__start_pos, const.S))
        self.__exit_row = len(self.__tachyon_grid) - 1

    def __parse_input(self, line):
        self.__tachyon_grid.append(list(line))

    def _part1(self):
        self._debug(f"Start Pos: {self.__start_pos}")

        split_count = 0
        while self.__beams:
            self._debug(f"  -> Beam Count: [{len(self.__beams)}]")
            beams_to_add = set()
            beams_to_remove = set()
            for beam in self.__beams:
                if beam.row != self.__exit_row:
                    # look south of beam to see what's there
                    next_pos = const.move(beam, const.S)
                    next_space = self.__tachyon_grid[next_pos.row][next_pos.col]

                    if next_space == self.SPLITTER:
                        split_count += 1
                        self._debug(f"  -> Split Count: [{split_count}]")

                        # Split the beam into two new beams
                        new_beam1 = const.move(beam, const.SW)
                        beams_to_add.add(new_beam1)

                        new_beam2 = const.move(beam, const.SE)
                        beams_to_add.add(new_beam2)
                    elif next_space == self.EMPTY:
                        # Move down/S
                        new_pos = const.move(beam, const.S)
                        # Add new beam pos
                        beams_to_add.add(new_pos)

                # Remove the old beam
                beams_to_remove.add(beam)

            self.__beams.difference_update(beams_to_remove)
            self.__beams.update(beams_to_add)

        return split_count

    def _part2(self):
        pass
        # need to figure out all the combinations of the particle going
        # left or right
        # ...based on number of splitters and number row rows?
