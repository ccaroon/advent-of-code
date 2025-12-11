from aoc.lib.puzzle import Puzzle


class Reactor(Puzzle):
    """AOC-2025 // Day11 -- Reactor"""

    START = "you"
    END = "out"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__path_count = 0
        self.__data = {}
        self._read_input(self.__parse_input)

    def __parse_input(self, line):
        (name, out_data) = line.split(":", 2)

        device_name = name.strip()
        outputs = out_data.strip().split()
        self.__data[device_name] = outputs

    def __trace_route(self, device):
        self._debug(f"[{device}]")
        for output in self.__data[device]:
            self._debug(f"  -> [{output}]")
            if output == self.END:
                self.__path_count += 1
            else:
                self.__trace_route(output)

    def _part1(self):
        # term condition is when all outputs of top-level `you`
        # have been processed
        self.__trace_route(self.START)

        return self.__path_count

    def _part2(self):
        pass
