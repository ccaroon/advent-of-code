import copy
import time

class RAM:
    FREE_BYTE = "."
    CORRUPTED_BYTE = "#"

    START = "S"
    EXIT = "E"

    OUT_OF_BOUNDS = "!"

    HISTORIANS = "X"
    VISITED = "o"

    UP    = (-1, 0)
    DOWN  = (1,  0)
    LEFT  = (0, -1)
    RIGHT = (0,  1)

    MOVE_DIRS = {
        "U": UP,
        "D": DOWN,
        "L": LEFT,
        "R": RIGHT
    }

    def __init__(self, input_file:str):
        self.__input_file = input_file

        self.__width = 0
        self.__height = 0
        self.__memory_space = []
        self.__byte_maze = None

        self.__bytes = []
        self.__read_input_file()
        self.__create_memory_space()


    def __read_input_file(self):
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                (col, row) = line.split(",", 2)
                row = int(row)
                col = int(col)
                self.__bytes.append((row, col))
                # Figure out grid W & H based in input
                if row > self.__height:
                    self.__height = row

                if col > self.__width:
                    self.__width = col

        self.__height += 1
        self.__width += 1


    def __create_memory_space(self):
        row = [self.FREE_BYTE] * self.__width
        for _ in range(self.__height):
            self.__memory_space.append(copy.deepcopy(row))

        self.__memory_space[0][0] = self.START
        self.__memory_space[self.__height-1][self.__width-1] = self.EXIT


    @property
    def mem_width(self):
        return self.__width


    @property
    def mem_height(self):
        return self.__height


    @property
    def byte_count(self):
        return len(self.__bytes)


    def __display_matrix(self, matrix):
        output = ""
        for row in matrix:
            for col in row:
                output += f"{col:2}"
            output += "\n"
        print(output)


    def display_memory_space(self):
        self.__display_matrix(self.__memory_space)


    def display_byte_maze(self):
        self.__display_matrix(self.__byte_maze)


    def tick(self):
        """
        Pass the next Nanosecond
        """
        try:
            coord = self.__bytes.pop(0)
            self.__memory_space[coord[0]][coord[1]] = self.CORRUPTED_BYTE
        except IndexError:
            print("Error: OutOfBytes")


    def __snapshot_memory_space(self):
        self.__byte_maze = copy.deepcopy(self.__memory_space)


    def __run_run_run(self, **kwargs):
        step_counter = 0
        curr_loc = [0, 0]
        trail = set()
        trail.add(tuple(curr_loc))
        found_exit = False

        visual = kwargs.get("visual", None)

        while not found_exit:
            self.__byte_maze[curr_loc[0]][curr_loc[1]] = self.VISITED

            # Analyze Surroundings
            surroundings = {}
            for code, mv_dir in self.MOVE_DIRS.items():
                loc = (curr_loc[0] + mv_dir[0], curr_loc[1] + mv_dir[1])
                what = None
                if loc[0] < 0 or loc[0] >= self.__height or loc[1] < 0 or loc[1] >= self.__width:
                    what = self.OUT_OF_BOUNDS
                else:
                    what = self.__byte_maze[loc[0]][loc[1]]

                surroundings[code] = {"what": what, "visited": loc in trail}


            # Find all valid directions
            primary_moves = {}
            secondary_moves = {}
            for mdir, info in surroundings.items():
                # Valid Space AND NOT already visited
                if (
                    info["what"] not in (self.CORRUPTED_BYTE, self.OUT_OF_BOUNDS)
                    and
                    info["visited"] == False
                   ):
                    primary_moves[mdir] = info

                # Valid Space, BUT ALREADY visited -- for backtracking
                if (
                    info["what"] not in (self.CORRUPTED_BYTE, self.OUT_OF_BOUNDS)
                    and
                    info["visited"] == True
                   ):
                    secondary_moves[mdir] = info

            move_options = None
            step_inc = 0
            backtracking = False
            if len(primary_moves) != 0:
                print("--Primary Moves--")
                move_options = primary_moves
                step_inc = 1
            else:
                print("--Secondary Moves--")
                move_options = secondary_moves
                step_inc = -1
                backtracking = True

            # if tuple(curr_loc) in trail:
            #     print("--Backtracking--")
            #     backtracking = True

            # --- TODO ---
            # --- IDEAS ---
            # if start stuck and **must** backtrack,
            # - go U & L until reach unvisited square
            # - along the way mark those backtracked spots as CORRUPTED
            #   ...so that that path will not be followed again

            if backtracking:
                match move_options:
                    case {"U": {}}:
                        curr_loc[0] += self.UP[0]
                        curr_loc[1] += self.UP[1]
                    case {"L": {}}:
                        curr_loc[0] += self.LEFT[0]
                        curr_loc[1] += self.LEFT[1]
                    case {"R": {}}:
                        curr_loc[0] += self.RIGHT[0]
                        curr_loc[1] += self.RIGHT[1]
                    case {"D": {}}:
                        curr_loc[0] += self.DOWN[0]
                        curr_loc[1] += self.DOWN[1]
                    case _:
                        print("CAN'T MOVE")
            else:
                match move_options:
                    case {"R": {}}:
                        curr_loc[0] += self.RIGHT[0]
                        curr_loc[1] += self.RIGHT[1]
                    case {"D": {}}:
                        curr_loc[0] += self.DOWN[0]
                        curr_loc[1] += self.DOWN[1]
                    case {"L": {}}:
                        curr_loc[0] += self.LEFT[0]
                        curr_loc[1] += self.LEFT[1]
                    case {"U": {}}:
                        curr_loc[0] += self.UP[0]
                        curr_loc[1] += self.UP[1]
                    case _:
                        print("CAN'T MOVE")


            # Freedom!
            if self.__byte_maze[curr_loc[0]][curr_loc[1]] == self.EXIT:
                found_exit = True

            # Update Info
            step_counter += step_inc
            trail.add(tuple(curr_loc))
            # Mark current location on the map
            self.__byte_maze[curr_loc[0]][curr_loc[1]] = self.HISTORIANS

            if visual:
                print(f"[{step_counter:03}]".center(self.__width*2, "-"))
                self.display_byte_maze()
                if visual == "manual":
                    input()
                else:
                    time.sleep(0.25)

        return step_counter


    def make_a_run_for_it(self, **kwargs):
        """
        Phase 2 -- Find the Exit, Quick!

        Find the shortest path from S(0,0) to E(W,H) while avoiding the
        CORRUPTED_BYTES.
        """
        step_count = 0

        # Stop Time...
        self.__snapshot_memory_space()
        # ...RUN!!!!!!!
        step_count = self.__run_run_run(**kwargs)

        return step_count


    def simulate_byte_fall(self, ticks:int, **kwargs):
        """
        Phase 1 -- Predict Byte Locations

        Simulate Bytes Falling for `ticks` nanoseconds
        """
        visual = kwargs.get("visual", None)

        nanoseconds = ticks if ticks < len(self.__bytes) else len(self.__bytes)-1
        for i in range(nanoseconds):
            self.tick()

            if visual:
                print(f"{(i+1):02}".center(self.mem_width*2, "-"))
                self.display_memory_space()
                if visual == "manual":
                    input()
                else:
                    time.sleep(0.25)







#
