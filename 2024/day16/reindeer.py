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

    def __init__(self, start_loc:Location, start_dir:Direction, score:int=0, **kwargs):
        self.__location = start_loc
        self.__direction = start_dir
        self.__score = score
        # Record of path choices that have not been tried yet
        self.__snapshots = []

        existing_trail = kwargs.get("trail")
        if existing_trail:
            self.__trail = existing_trail
        else:
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
            id=self.__id + 1,
            trail=self.__trail.copy()
        )


    def turn(self, tdir:Direction):
        if self.can_move():
            self.__score += self.COST_TURN
            self.__direction = self.__direction.turn(tdir)


    def rewind(self):
        """
        Rewind to a previous snapshot (loc/dir/score, etc.) in order to try a
        different path.
        """
        # Get the most recent snapshot
        snapshot = self.__snapshots.pop()

        self.__location = snapshot.get("location")
        self.__direction = snapshot.get("direction")
        # self.__trail = snapshot.get("trail")
        self.__score = snapshot.get("score")

        tdir = snapshot.get("turn_dir")
        self.turn(Direction(tdir))

        self.finished = False
        self.stuck = False


    def snapshot(self, turn_dir:str):
        """
        Take a snapshot of the current location/direction/score/trail, etc.

        Args:
            turn_dir (str): A new path can be traveled from the current location by turning in this direction.
        """
        snapshot = {
            "location": self.__location.copy(),
            "direction": self.__direction.copy(),
            # "trail": self.__trail.copy(),
            "score": self.__score,
            "turn_dir": turn_dir
        }
        self.__snapshots.append(snapshot)

        # print(f"SNAPSHOT: score[{self.__score}]")


    def move(self):
        if self.can_move():
            self.__score += self.COST_FORWARD
            self.__location.move(self.__direction)
            # print(f"MOVE: {self.__location} --in-- {self.__trail} ({type(self.__trail)})")
            if self.__location in self.__trail:
                # print(f"<{self.__id}> has been here before {self.__location}")
                self.stuck = True
            else:
                self.__trail.add(self.__location.copy())
        else:
            print(f"{self} -- CANT MOVE")
