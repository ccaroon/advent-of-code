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
    # Trace Type 1 & 2 i.e. part1 or part2
    TT1 = 1
    TT2 = 2

    def __init__(self, path, trace_type=TT1):
        self.__path = path
        self.dac_count = 0
        self.fft_count = 0
        self.__trace_type = trace_type

    @property
    def path(self):
        return self.__path

    @property
    def trace_type(self):
        return self.__trace_type

    def __len__(self):
        return len(self.path.split("."))

    def __eq__(self, other):
        return self.path == other.path

    def __hash__(self):
        return hash(self.path)

    def __repr__(self):
        return f"Packet({self.path},{self.trace_type})"

    def __str__(self):
        return f"{self.path} -> DAC:{self.dac_count} | FFT:{self.fft_count}"


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

    # @cache  # noqa: B019
    # NEVER SEE THE SAME PATH MORE THAN ONCE ... so caching is not effective
    def __trace_route(self, packet, cache):
        self._debug(f"Enter -> {packet}")

        out_count = cache.get(packet.path)
        if out_count is None:
            device_path = packet.path.split(".")
            device = self.__devices[device_path[-1]]

            dac_count = packet.dac_count
            fft_count = packet.fft_count
            out_count = 0

            for node in device.outputs:
                match node.name:
                    case self.OUT:
                        if packet.trace_type == Packet.TT1:
                            out_count += 1
                        elif packet.trace_type == Packet.TT2:  # noqa: SIM102
                            if dac_count > 0 and fft_count > 0:
                                out_count += 1
                        self._debug(f"  -> OUT: {packet}")
                    case self.DAC:
                        dac_count += 1
                        self._debug(f"  -> DAC: {packet}")
                    case self.FFT:
                        fft_count += 1
                        self._debug(f"  -> FFT: {packet}")

                if node.name != self.OUT:
                    new_packet = Packet(f"{packet.path}.{node.name}", packet.trace_type)
                    new_packet.dac_count = dac_count
                    new_packet.fft_count = fft_count
                    out_count += self.__trace_route(new_packet, cache)

            self._debug(f"Exit -> {packet} | OUT:{out_count}")

            print(f"{packet.path} => {out_count}")
            cache[packet.path] = out_count
        else:
            print(f"Cache Hit {packet.path}")

        return out_count

    def _part1(self):
        packet = Packet(self.P1_START)
        cache = {}
        out_count = self.__trace_route(packet, cache)

        return out_count  # noqa: RET504

    def _part2(self):
        # Find all of the paths that lead from `svr`` to out.
        # How many of those paths visit both `dac` and `fft`?
        packet = Packet(self.P2_START, Packet.TT2)
        cache = {}
        out_count = self.__trace_route(packet, cache)

        return out_count  # noqa: RET504


#
