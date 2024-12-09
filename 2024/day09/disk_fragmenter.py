
class DiskFragmenter:
    FREE_BLOCK = "."

    def __init__(self, filename):
        self.__input_file = filename
        self.__disk_map = None
        self.__checksum = None
        self.__read_disk_map()


    def __read_disk_map(self):
        with open(self.__input_file, "r") as fptr:
            line = fptr.readline()
            self.__disk_map = list(line.strip())
            # self.__disk_map = [int(num) for num in self.__disk_map]


    def __str__(self):
        # return str(self.__disk_map)
        return "".join(self.__disk_map)


    @property
    def checksum(self):
        return self.__checksum


    def expand(self):
        file_id = 0
        expanded_map = []

        for idx in range(0, len(self.__disk_map), 2):
            # idx => file block
            count = int(self.__disk_map[idx])
            file_blocks = [f"{file_id}"] * count
            expanded_map.extend(file_blocks)

            # idx + 1 => free blocks
            if idx + 1 < len(self.__disk_map):
                count = int(self.__disk_map[idx + 1])
                free_blocks = [self.FREE_BLOCK] * count
                expanded_map.extend(free_blocks)

            file_id += 1

        self.__disk_map = expanded_map


    def __calc_checksum(self):
        self.__checksum = 0

        for idx,fid in enumerate(self.__disk_map):
            if self.__disk_map[idx] != self.FREE_BLOCK:
                self.__checksum += idx * int(fid)

        return self.__checksum


    def enfrag(self):
        mv_idx = len(self.__disk_map)
        while True:
            mv_idx -= 1
            free_idx = self.__disk_map.index(".")
            if mv_idx <= free_idx:
                break

            self.__disk_map[free_idx], self.__disk_map[mv_idx] = self.__disk_map[mv_idx], self.__disk_map[free_idx]

        self.__calc_checksum()
