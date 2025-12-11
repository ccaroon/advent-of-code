from aoc.lib.puzzle import Puzzle


class Reactor(Puzzle):
    """AOC-2025 // Day11 -- Reactor"""

    P1_START = "you"
    P2_START = "svr"
    DAC = "dac"
    FFT = "fft"
    END = "out"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__path_count = 0
        self.__dac_in_path = False
        self.__fft_in_path = False

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
            keep_going = True
            match output:
                case self.END:
                    # if self.__dac_in_path and self.__fft_in_path:
                    self.__path_count += 1
                    self.__dac_in_path = False
                    self.__fft_in_path = False
                    keep_going = False
                case self.DAC:
                    self.__dac_in_path = True
                case self.FFT:
                    self.__fft_in_path = True
                # case _:

            if keep_going:
                self.__trace_route(output)

    def _part1(self):
        # term condition is when all outputs of top-level `you`
        # have been processed
        self.__trace_route(self.P1_START)

        return self.__path_count

    def _part2(self):
        # Find all of the paths that lead from `svr`` to out.
        # How many of those paths visit both `dac` and `fft`?

        self.__trace_route(self.P2_START)

        return self.__path_count
