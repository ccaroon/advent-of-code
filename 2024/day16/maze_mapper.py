import copy
import time

from shared.location import Location
from shared.direction import Direction

from reindeer import Reindeer

class MazeMapper:
    START = "S"
    END = "E"
    WALL = "#"
    OPEN = "."

    def __init__(self, input_file:str, **kwargs):
        self.__input_file = input_file

        self.__maze_map = None
        self.__start_loc = None
        self.__end_loc = None
        self.__read_file()

        self.__debug = kwargs.get("debug", False)

        self.__reindeer = []


    @property
    def start(self):
        return self.__start_loc


    @property
    def end(self):
        return self.__end_loc


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
                    self.__end_loc = Location(row_idx, col_idx)

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


        THOUGHTS:
        - instead of killing if hit wall when can turn, allow at least 1 clone
          to turn and keep moving

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
                    clone.stuck = True

            if right_valid:
                if whats_right != self.WALL:
                    clone = reindeer.clone()
                    clone.turn(Direction("R"))
                    clone.move()
                    new_deer.append(clone)
                if whats_right == self.END:
                    clone.finished = True
                elif whats_right == self.START:
                    clone.stuck = True

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

        max_rdeer = kwargs.get("max_rdeer", 1000)
        max_iterations = kwargs.get("max_iter", 50)
        visual = kwargs.get("visual", False)

        # Start with 1 reindeer at the "S" location
        reindeer = Reindeer(self.__start_loc, Direction("E"), 0)
        self.__reindeer.append(reindeer)

        finished_count = 0
        still_going = True
        counter = 0
        while still_going and counter < max_iterations:
        # still_going and finished_count < (max_rdeer*.75) and counter < max_iterations:
            counter += 1
            new_deer = []
            for rdeer in self.__reindeer:
                clones = self.__move(rdeer)
                new_deer.extend(clones)

            # --- Add all new reindeer ---
            if len(self.__reindeer) < max_rdeer:
                self.__reindeer.extend(new_deer)


            # self.__reindeer.extend(new_deer)
            # --- Trim the oldest rdeer ---
            # self.__reindeer = self.__reindeer[-max_rdeer:]
            # --- Trim the newest rdeer ---
            # self.__reindeer = self.__reindeer[0:max_rdeer]

            # Get rid of rdeer with highest rid's; been in the maze too long
            # max_rid = 15
            # trimmed_rdeer = filter(lambda rd: rd.rid <= max_rid, self.__reindeer)
            # self.__reindeer = list(trimmed_rdeer)


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
                print(f"Iteration #{counter:04}/{max_iterations:04} | Reindeer: {len(self.__reindeer):04}/{max_rdeer:04} | Added: {len(new_deer)} | Finished: {finished_count}")
                # input()

            if visual:
                print(f"Iteration #{counter:03} | Reindeer: {len(self.__reindeer):04}/{max_rdeer:04} | Added: {len(new_deer)} | Finished: {finished_count}")
                tmp_map = copy.deepcopy(self.__maze_map)
                for rdeer in self.__reindeer:
                    self.__print_debug(rdeer)
                    tmp_map[rdeer.loc.row][rdeer.loc.col] = str(rdeer.rid)
                print(self.render_maze(tmp_map))
                if visual == "auto":
                    time.sleep(.25)
                elif visual == "manual":
                    input()


        print(f"==> StillGoing: {still_going}/{len(self.__reindeer)} | {counter}/{max_iterations} | Fin: {finished_count} <==")

        return lowest_score


    def __move2(self, reindeer:Reindeer):
        """
        I like to Move-It, Move-It!
        """
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

        # Action will be processes in order from 0 to N
        # ...so actions entered first will be processed first
        actions = []
        # if NO valid move (F|L|R):
        if not forward_valid and not left_valid and not right_valid:
            # - rewind to most recent snapshot
            actions.append({"type": "rewind"})
        else:
            # if CAN move forward:
            if forward_valid:
                # - take left snapshot if left is valid
                if left_valid:
                    actions.append(
                        {"type": "snapshot", "dir": "L", "what": whats_left})
                # - take right snapshot if right is valid
                if right_valid:
                    actions.append(
                        {"type": "snapshot", "dir": "R", "what": whats_right})
                # - move forward
                actions.append({"type": "move", "what": whats_forward})

            # if CANNOT move forward:
            else:
                # - if both L&R are valid,
                if left_valid and right_valid:
                    # -- snapshot L
                    actions.append(
                        {"type": "snapshot", "dir": "L", "what": whats_left})
                    # -- turn R and move
                    actions.append(
                        {"type": "turn", "dir": "R", "what": whats_right})
                    actions.append(
                        {"type": "move", "what": whats_forward})
                else:
                    # - if only 1 of L|R is valid, turn and move
                    turn_dir = "L" if left_valid else "R"
                    what = whats_left if left_valid else whats_right
                    actions.append(
                        {"type": "turn", "dir": turn_dir, "what": what})
                    actions.append(
                        {"type": "move", "what": whats_forward})

        # Handle actions
        for idx, action in enumerate(actions):
            match action["type"]:
                case "snapshot":
                    reindeer.snapshot(action["dir"])
                case "move":
                    reindeer.move()
                case "turn":
                    tdir = action["dir"]
                    reindeer.turn(Direction(tdir))
                case "rewind":
                    reindeer.rewind()
                case _:
                    raise ValueError(f"Unknown Action: {action}")

            if action.get("what") == self.END:
                reindeer.finished = True

            print(
                f"#{idx}) {action['type'].upper()} -> {action.get('dir', '-')} [{action.get('what', '-')}] -> {reindeer}")

        # if BACTRACKING:
        # - rewind to most recent snapshot
        if reindeer.stuck:
            reindeer.rewind()
            print(f"BACKTRACKING: rewind -> {reindeer}")



    def analyze2(self, **kwargs):
        lowest_score = 999_999_999_999

        rudolph = Reindeer(self.__start_loc, Direction("E"))
        # print(rudolph)

        max_iter = kwargs.get("max_iter", 250)
        visual = kwargs.get("visual")

        counter = 0
        while counter < max_iter and not rudolph.finished:
            counter += 1

            if visual:
                tmp_map = copy.deepcopy(self.__maze_map)
                tmp_map[rudolph.loc.row][rudolph.loc.col] = Reindeer.DIR_ARROW[rudolph.dir.code]
                print(self.render_maze(tmp_map))
                if visual == "auto":
                    time.sleep(.25)
                elif visual == "manual":
                    input()

            self.__move2(rudolph)

        return lowest_score






#
