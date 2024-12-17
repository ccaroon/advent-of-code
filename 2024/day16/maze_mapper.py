import copy

from shared.direction import Direction
from shared.location import Location


class Reindeer:

    COST_FORWARD = 1
    COST_TURN = 1000

    DIR_ARROW = {
        "N": "^",
        "E": ">",
        "S": "v",
        "W": "<"
    }

    def __init__(self, start_loc:Location, start_dir:Direction, score:int, **kwargs):
        self.__location = start_loc
        self.__direction = start_dir
        self.__score = score

        self.__id = kwargs.get("id", 1)

        self.finished = False
        self.stuck = False


    @property
    def rid(self):
        return f"{self.DIR_ARROW[self.__direction.code]}"
        # return f"{self.__id}{self.DIR_ARROW[self.__direction.code]}"


    @property
    def score(self):
        return self.__score


    @property
    def loc(self):
        return self.__location


    @property
    def dir(self):
        return self.__direction


    def can_move(self):
        return not (self.finished or self.stuck)

    def status(self):
        status = "M"
        if self.finished:
            status = "F"
        elif self.stuck:
            status = "S"
        return status


    def __str__(self):
        return f"<{self.__id}>[{self.status()}] {self.__location} => {self.__direction.code} [{self.__score}]"


    def clone(self):
        return Reindeer(
            self.__location.copy(),
            self.__direction.copy(),
            self.__score,
            id=self.__id+1
        )


    def turn(self, tdir:Direction):
        if self.can_move():
            self.__score += self.COST_TURN
            self.__direction = self.__direction.turn(tdir)


    def move(self):
        if self.can_move():
            self.__score += self.COST_FORWARD
            self.__location.move(self.__direction)


class MazeMapper:
    START = "S"
    END = "E"
    WALL = "#"
    OPEN = "."
    REINDEER = "@"

    def __init__(self, input_file:str, **kwargs):
        self.__input_file = input_file

        self.__maze_map = None
        self.__start_loc = None
        self.__end_pos = None
        self.__read_file()

        self.__debug = kwargs.get("debug", False)

        self.__reindeer = []


    @property
    def start(self):
        return self.__start_loc


    @property
    def end(self):
        return self.__end_pos


    @property
    def size(self):
        return (len(self.__maze_map), len(self.__maze_map[0]))


    def __read_file(self):
        self.__maze_map = []
        row_idx = 0
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                row = list(line.strip())
                self.__maze_map.append(row)
                if self.START in row:
                    col_idx = row.index(self.START)
                    self.__start_loc = Location(row_idx, col_idx)

                if self.END in row:
                    col_idx = row.index(self.END)
                    self.__end_pos = Location(row_idx, col_idx)

                row_idx += 1

    def render_maze(self, maze_map):
        output = ""
        for row in maze_map:
            for col in row:
                output += f"{col:2}"

            output += "\n"

        return output


    def __print_debug(self, msg):
        if self.__debug:
            print(msg)


    def __str__(self):
        return self.render_maze(self.__maze_map)


    def __peek(self, location:Location, direction:Direction):
        peek_loc = location + direction
        return self.__maze_map[peek_loc.row][peek_loc.col]


    def __move(self, reindeer:Reindeer):
        """
        left -> clone and turn
        right -> clone and turn
        forward -> move
        """
        new_deer = []

        self.__print_debug(reindeer)

        # NOTE: MUST process F last
        for look_code in ("L", "R", "F"):
            if look_code in ("L", "R"):
                look_dir = reindeer.dir.turn(look_code)
                what = self.__peek(reindeer.loc, look_dir)
                self.__print_debug(f"...{look_code} -> [{what}]")
                if what in (self.OPEN, self.END):
                    self.__print_debug("......OPEN/END - clone/turn/move")
                    clone = reindeer.clone()
                    clone.turn(Direction(look_code))
                    clone.move()
                    new_deer.append(clone)
                elif what == self.WALL:
                    self.__print_debug("......WALL - NoOp")
                    # reindeer.stuck = True
                    pass
            elif look_code == "F":
                what = self.__peek(reindeer.loc, reindeer.dir)
                self.__print_debug(f"...{look_code} -> [{what}]")
                if what == self.OPEN:
                    self.__print_debug("......OPEN - move")
                    reindeer.move()
                elif what == self.END:
                    self.__print_debug("......END - move/finished")
                    reindeer.move()
                    reindeer.finished = True
                elif what in self.WALL:
                    self.__print_debug("......WALL - stuck")
                    reindeer.stuck = True

        self.__print_debug(f"...Clones: {len(new_deer)}")
        return new_deer


    def analyze(self, **kwargs):
        all_finished = []
        lowest_score = 0

        max_iterations = kwargs.get("max_iter", 50)

        self.__reindeer = []
        # Start with 1 reindeer at the "S" location
        reindeer = Reindeer(self.__start_loc, Direction("E"), 0)
        self.__reindeer.append(reindeer)

        still_going = True
        counter = 0
        while still_going and counter < max_iterations:
            counter += 1
            new_deer = []
            for rdeer in self.__reindeer:
                clones = self.__move(rdeer)
                new_deer.extend(clones)

            self.__reindeer.extend(new_deer)

            # Track "finished" reindeer
            finished = filter(lambda rd: rd.finished, self.__reindeer)
            all_finished.extend(list(finished))

            # Remove reindeer that have no more moves: finished or stuck
            self.__reindeer = list(filter(lambda rd: rd.can_move(), self.__reindeer))

            still_going = len(self.__reindeer) > 0

            if counter % 10 == 0:
                print(f"Iteration #{counter:02} | Reindeer: {len(self.__reindeer)} | Added: {len(new_deer)} | Finished: {len(all_finished)}")
            # tmp_map = copy.deepcopy(self.__maze_map)
            # for rdeer in self.__reindeer:
            #     self.__print_debug(rdeer)
            #     tmp_map[rdeer.loc.row][rdeer.loc.col] = str(rdeer.rid)
            # # self.__print_debug(f"Reindeer: {len(self.__reindeer)}")
            # print(self.render_maze(tmp_map))

            # input()


        # TODO: examine all rdeer for lowest score among all who finished
        lowest_score = 999_999_999_999
        for rdeer in all_finished:
            if rdeer.score < lowest_score:
                lowest_score = rdeer.score

        return lowest_score









#
