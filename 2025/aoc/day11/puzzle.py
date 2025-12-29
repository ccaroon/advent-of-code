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

    def __init__(self, input_file, **kwargs):
        super().__init__(input_file, **kwargs)

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

    # input: path desc Ex: svr.fft.ggg.out
    # output: fft+dac+out counts
    @cache  # noqa: B019
    def __trace_route(self, path, dac_count, fft_count, out_count):
        device_path = path.split(".")
        device = self.__devices[device_path[-1]]
        # decode counts
        # dac_count = counts // 1_000_000
        # fft_count = counts % 1_000_000 // 1_000
        # out_count = counts % 1_000

        self._debug(f"Enter -> {device}")
        for node in device.outputs:
            self._debug(f"  -> {path}.{node.name}")

            match node.name:
                case self.OUT:
                    self._debug("  -> OUT")
                    out_count += 1

                    # if dac_count > 0 and fft_count > 0:
                    #     # TODO: Part 2 out count
                    #     out_count += 1
                case self.DAC:
                    dac_count += 1
                case self.FFT:
                    fft_count += 1

            if node.name != self.OUT:
                # packet.start_device = node
                # new_counts = dac_count * 1_000_000 + fft_count * 1000 + out_count * 1
                path, dac_count, fft_count, out_count = self.__trace_route(
                    f"{path}.{node.name}", dac_count, fft_count, out_count
                )

        if device.name == self.FFT:
            fft_count -= 1
        elif device.name == self.DAC:
            dac_count -= 1

        self._debug(f"Exit -> {device}")

        return path, dac_count, fft_count, out_count

    def _part1(self):
        # packet = Packet(self.__devices[self.P1_START])
        # self.__trace_route(packet)

        # return packet.p1_out_count
        path, dac_count, fft_count, out_count = self.__trace_route(self.P1_START, 0, 0, 0)

        return out_count

    def _part2(self):
        # Find all of the paths that lead from `svr`` to out.
        # How many of those paths visit both `dac` and `fft`?
        # --------------------------------------------------
        # packet = Packet(self.__devices[self.P2_START])
        # self.__trace_route(packet)
        # return packet.p2_out_count
        # --------------------------------------------------
        path, dac_count, fft_count, out_count = self.__trace_route(self.P2_START, 0, 0, 0)

        return out_count


#
