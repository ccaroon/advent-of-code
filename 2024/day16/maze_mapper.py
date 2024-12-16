from shared.direction import Direction
from shared.location import Location


class Choice:
    START = "S"
    FORWARD = "F"
    TURN_LEFT = "L"
    TURN_RIGHT = "R"
    END = "E"

    COST_FORWARD = 1
    # 90º clockwise or counter-clockwise
    COST_TURN    = 1000

    def __init__(self, code):
        self.__code = code
        self.__sub_choices = []


    def add(self, choice):
        self.__sub_choices.append(choice)


    @property
    def cost(self):
        cost = self.COST_FORWARD
        if self.__code in (self.TURN_LEFT, self.TURN_RIGHT):
            cost = self.COST_TURN

        return cost

    @property
    def is_leaf(self):
        return len(self.__sub_choices) == 0


class MazeMapper:
    START_MARKER = "S"
    END_MARKER = "E"

    WALL = "#"
    OPEN = "."

    def __init__(self, input_file:str):
        self.__input_file = input_file

        self.__dtree = None
        self.__score = 0
        self.__start_dir = Direction("E")

        self.__maze_map = None
        self.__start_pos = None
        self.__end_pos = None
        self.__read_file()


    @property
    def start(self):
        return self.__start_pos


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
                if self.START_MARKER in row:
                    col_idx = row.index(self.START_MARKER)
                    self.__start_pos = Location(row_idx, col_idx)

                if self.END_MARKER in row:
                    col_idx = row.index(self.END_MARKER)
                    self.__end_pos = Location(row_idx, col_idx)

                row_idx += 1

    def __str__(self):
        output = ""
        for row in self.__maze_map:
            for col in row:
                output += f"{col}"

            output += "\n"

        return output

    def __create_decision_tree(self):
        self.__dtree = []



    def analyze(self):
        self.__score = 0
        for ridx in range(len(self.__maze_map)):
            for cidx in range(len(self.__maze_map[0])):
                pass
                # NOTE:
                #   - turning is expensive, keep straight unless have to turn?
                #   - keep track of each decision
                #   - find all paths and choose lowest score?
                #   - don't repeat same spaces (loops)
                #   - rewind time
                #   - try every branch (F, L, R)

                #
                # --- PLAN1 ---
                # 1. if can move forward, move forward
                # 2. if wall, look left & right for open space
                #   - if ONLY left open, turn left, goto 1
                #   - if ONLY right open, turn right, goto 1
                #   - if BOTH open, turn TOWARDS "E", goto 1
                #   - no open space, turn right, goto 2
                # 3. if END, stop

                # --- ALT ---
                # if multiple open spaces, turn towards "E"
                #   - turn N times and move forward







#
