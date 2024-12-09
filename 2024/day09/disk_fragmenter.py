
class Block:
    def __init__(self, block_id, start_idx, end_idx):
        self.id = block_id
        self.start_idx = start_idx
        self.end_idx = end_idx


    def __str__(self):
        return f"B({self.id}, {self.start_idx}, {self.end_idx}, {len(self)})"


    def __len__(self):
        """
        Block Length

        >>> blk = Block('x', 0,1)
        >>> len(blk)
        2
        """
        return (self.end_idx - self.start_idx) + 1


class DiskFragmenter:
    FREE_BLOCK = "."

    def __init__(self, filename):
        self.__input_file = filename
        self.__disk_map = None
        self.__checksum = None
        self.__file_count = 0
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


    @property
    def file_count(self):
        return self.__file_count


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

        self.__file_count = file_id
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


    def __find_block(self, block_id:str, start_idx:int) -> Block:
        """
        Parameters:
            block_id (str): Block ID. FileID or FREE_BLOCK
            start_idx (int): Index from which to start the search

        Returns:
            Block
        """
        curr_idx = start_idx
        while curr_idx < len(self.__disk_map) and self.__disk_map[curr_idx] == block_id:
            curr_idx += 1
        end_idx = curr_idx - 1

        return Block(block_id, start_idx, end_idx)


    def __set_block(self, block):
        for idx in range(block.start_idx, block.end_idx + 1):
            self.__disk_map[idx] = block.id


    def smart_enfrag(self):
        for fid in range(self.__file_count - 1, -1, -1):
            file_id = str(fid)
            mv_idx = self.__disk_map.index(file_id)
            mv_block = self.__find_block(file_id, mv_idx)

            # find a block of free space big enough
            search_start = 0
            free_block = None
            while free_block is None and search_start < len(self.__disk_map):
                free_idx = self.__disk_map.index(self.FREE_BLOCK, search_start)
                check_block = self.__find_block(self.FREE_BLOCK, free_idx)
                if len(check_block) >= len(mv_block):
                    free_block = check_block
                else:
                    # keep looking
                    search_start = free_idx + 1

            # If found free space AND
            # we're moving the FileBlock to the Left
            if free_block and free_block.start_idx < mv_block.start_idx:
                # Set free_block space to mv_block fid
                block = Block(
                        mv_block.id,
                        free_block.start_idx,
                        free_block.start_idx + len(mv_block) - 1
                )
                self.__set_block(block)

                # Set mv_block space to FREE_BLOCK
                block = Block(
                        self.FREE_BLOCK,
                        mv_block.start_idx,
                        mv_block.end_idx
                )
                self.__set_block(block)

        self.__calc_checksum()
