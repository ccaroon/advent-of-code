import copy
import time

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
        self.__trail = set()
        self.__trail.add(start_loc)

        self.__id = kwargs.get("id", 1)

        self.finished = False
        self.stuck = False


    @property
    def rid(self):
        # return f"{self.DIR_ARROW[self.__direction.code]}"
        # return f"{self.__id}{self.DIR_ARROW[self.__direction.code]}"
        # return chr((self.__id + 33) % 126)
        return self.__id


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
        return not self.finished and not self.stuck

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
            id=self.__id + 1
        )


    def turn(self, tdir:Direction):
        if self.can_move():
            self.__score += self.COST_TURN
            self.__direction = self.__direction.turn(tdir)


    def move(self):
        if self.can_move():
            self.__score += self.COST_FORWARD
            self.__location.move(self.__direction)
            if self.__location in self.__trail:
                # stuck in a loop?
                self.stuck = True
                # print(f"{self} stuck in loop")
            else:
                self.__trail.add(self.__location)



class MazeMapper:
    START = "S"
    END = "E"
    WALL = "#"
    OPEN = "."
    REINDEER = "@"

    MAX_REINDEER = 1000


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

        #  LEFT
        look_dir = reindeer.dir.turn("L")
        whats_left = self.__peek(reindeer.loc, look_dir)
        left_valid = whats_left != self.WALL
        # RIGHT
        look_dir = reindeer.dir.turn("R")
        whats_right = self.__peek(reindeer.loc, look_dir)
        right_valid = whats_right != self.WALL
        # FORWARD / STRAIGHT AHEAD
        whats_forward = self.__peek(reindeer.loc, reindeer.dir)
        forward_valid = whats_forward != self.WALL

        choices = (left_valid, right_valid, forward_valid)
        choice_count = choices.count(True)
        # 0 choices => stuck
        if choice_count == 0:
            reindeer.stuck = True
        # 1 choice  => turn and move OR move
        # TODO: DRY it up
        elif choice_count == 1:
            if forward_valid:
                if whats_forward != self.WALL:
                    reindeer.move()
                if whats_forward == self.END:
                    reindeer.finished = True
                elif whats_forward == self.START:
                    reindeer.stuck = True
            elif left_valid:
                if whats_left != self.WALL:
                    reindeer.turn(Direction("L"))
                    reindeer.move()
                if whats_left == self.END:
                    reindeer.finished = True
                elif whats_left == self.START:
                    reindeer.stuck = True
            elif right_valid:
                if whats_right != self.WALL:
                    reindeer.turn(Direction("R"))
                    reindeer.move()
                if whats_right == self.END:
                    reindeer.finished = True
                elif whats_right == self.START:
                    reindeer.stuck = True
        # 2+ choices => if F -> move, if L,R -> clone, turn, move
        elif choice_count > 1:
            if left_valid:
                if whats_left != self.WALL:
                    clone = reindeer.clone()
                    clone.turn(Direction("L"))
                    clone.move()
                    new_deer.append(clone)
                if whats_left == self.END:
                    clone.finished = True
                elif whats_left == self.START:
                    reindeer.stuck = True

            if right_valid:
                if whats_right != self.WALL:
                    clone = reindeer.clone()
                    clone.turn(Direction("R"))
                    clone.move()
                    new_deer.append(clone)
                if whats_right == self.END:
                    clone.finished = True
                elif whats_right == self.START:
                    reindeer.stuck = True

            if forward_valid:
                if whats_forward != self.WALL:
                    reindeer.move()
                if whats_forward == self.END:
                    reindeer.finished = True
                elif whats_forward == self.START:
                    reindeer.stuck = True
            else:
                reindeer.stuck = True

        return new_deer


    def analyze(self, **kwargs):
        lowest_score = 999_999_999_999
        self.__reindeer = []

        max_iterations = kwargs.get("max_iter", 50)
        visual = kwargs.get("visual", False)

        # Start with 1 reindeer at the "S" location
        reindeer = Reindeer(self.__start_loc, Direction("E"), 0)
        self.__reindeer.append(reindeer)

        finished_count = 0
        still_going = True
        counter = 0
        while still_going and finished_count < 10 and counter < max_iterations:
        # while still_going and counter < max_iterations:
            counter += 1
            new_deer = []
            for rdeer in self.__reindeer:
                clones = self.__move(rdeer)
                new_deer.extend(clones)

            if len(self.__reindeer) < self.MAX_REINDEER:
                self.__reindeer.extend(new_deer)

            # Track "finished" reindeer
            finished = filter(lambda rd: rd.finished, self.__reindeer)
            for rdeer in finished:
                finished_count += 1
                if rdeer.score < lowest_score:
                    lowest_score = rdeer.score

            # Remove reindeer that have no more moves: finished or stuck
            # print(f"RDeer Before Prune: {len(self.__reindeer)}")
            self.__reindeer = list(filter(lambda rd: rd.can_move(), self.__reindeer))
            # print(f"RDeer After Prune: {len(self.__reindeer)}")

            still_going = len(self.__reindeer) > 0

            if counter % 100 == 0:
                print(f"Iteration #{counter:03} | Reindeer: {len(self.__reindeer)} | Added: {len(new_deer)} | Finished: {finished_count}")
                # input()

            if visual:
                print(f"Iteration #{counter:03} | Reindeer: {len(self.__reindeer)} | Added: {len(new_deer)} | Finished: {finished_count}")
                tmp_map = copy.deepcopy(self.__maze_map)
                for rdeer in self.__reindeer:
                    self.__print_debug(rdeer)
                    tmp_map[rdeer.loc.row][rdeer.loc.col] = str(rdeer.rid)
                print(self.render_maze(tmp_map))
                if visual == "auto":
                    time.sleep(.25)
                elif visual == "manual":
                    input()

        return lowest_score









#
