from functools import cache
from aoc.lib.puzzle import Puzzle


class Device:
    def __init__(self, name):
        self.name = name
        self.outputs = []

    def add_output(self, device):
        self.outputs.append(device)

    def __str__(self):
        return f"<{self.name}>"

    def __repr__(self):
        return f"{self.name}: {self.outputs}"

    def display(self):
        print(self.name)
        for out in self.outputs:
            print(f"  -> {out.name}")
            out.display()


class Packet:
    def __init__(self, start_device):
        self.start_device = start_device
        self.p1_out_count = 0
        self.p2_out_count = 0
        # self.path = [start_device.name]
        self.dac_count = 0
        self.fft_count = 0


class Reactor(Puzzle):
    """AOC-2025 // Day11 -- Reactor"""

    P1_START = "you"
    P2_START = "svr"
    DAC = "dac"
    FFT = "fft"
    OUT = "out"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__devices = {}
        self._read_input(self.__parse_input)

    def __parse_input(self, line):
        (name, out_data) = line.split(":", 2)

        device_name = name.strip()
        output_names = out_data.strip().split()

        # Build into tree
        device = self.__devices.get(device_name)
        if device is None:
            device = Device(device_name)
            self.__devices[device_name] = device

        for out_id in output_names:
            output = self.__devices.get(out_id)
            if output is None:
                output = Device(out_id)
                self.__devices[out_id] = output

            device.add_output(output)

    # @cache
    def __trace_route(self, packet):
        device = packet.start_device
        self._debug(f"Enter -> {device}")
        for node in device.outputs:
            self._debug(f"  -> {device.name}:{node.name}")

            match node.name:
                case self.OUT:
                    self._debug("  -> OUT")
                    packet.p1_out_count += 1

                    if packet.dac_count > 0 and packet.fft_count > 0:
                        packet.p2_out_count += 1
                case self.DAC:
                    packet.dac_count += 1
                case self.FFT:
                    packet.fft_count += 1

            if node.name != self.OUT:
                packet.start_device = node
                self.__trace_route(packet)

        if device.name == self.FFT:
            packet.fft_count -= 1
        elif device.name == self.DAC:
            packet.dac_count -= 1

        self._debug(f"Exit -> {device}")

    def _part1(self):
        # term condition is when all outputs of top-level `you`
        # have been processed
        packet = Packet(self.__devices[self.P1_START])
        self.__trace_route(packet)

        return packet.p1_out_count

    def _part2(self):
        # Find all of the paths that lead from `svr`` to out.
        # How many of those paths visit both `dac` and `fft`?
        packet = Packet(self.__devices[self.P2_START])
        # self.__trace_route(packet)

        # TODO: try this
        # walk the tree and build each path to `out`
        # then if `dac` in `path` and `fft` in `path` ++count

        # TODO: back-out
        # once found `out` how far do i need to "backout" to reset stuff
        # to continue walking the path?

        # TODO: I.e. ^^^ better keeping track of the paths

        # return packet.p2_out_count

        self.__trace_route(packet)

        return packet.p2_out_count


#
