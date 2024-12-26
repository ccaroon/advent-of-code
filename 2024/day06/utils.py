import copy

UP = (-1,0)
RT = (0,1)
DN = (1,0)
LF = (0,-1)

DIRECTION_MARKER = {
    UP: "U",
    DN: "D",
    LF: "L",
    RT: "R"
}

DIRECTION_LOOKUP = {
    "U": UP,
    "D": DN,
    "L": LF,
    "R": RT
}

TURN = {
    UP: RT,
    RT: DN,
    DN: LF,
    LF: UP
}

EVENT_MOVE = 1
EVENT_OBSTACLE = 2
EVENT_TURN = 3
EVENT_EXIT = 4

GUARD = "^"
POSITION_MARK  = "X"
OBSTACLE = "#"
EMPTY = "."
LOOP_OBSTACLE = "O"

def load_map(filename:str) -> list[list[str]]:
    """
    Load the Patrol Map into a useable format.
    """
    map_data = []
    with open(filename, "r") as fptr:
        while line := fptr.readline():
            map_data.append(list(line.strip()))

    return map_data


def print_map(area_map):
    for row in area_map:
        for col in row:
            print(f"{col:2}", end="")
        print("")


def walk_map(area_map:list[list[str]], start_pos, start_dir, event_handler) -> None:
    curr_row = start_pos[0]
    curr_col = start_pos[1]
    curr_dir = start_dir
    cache = {}
    on_map = True
    while on_map:
        event_handler(area_map,
            EVENT_MOVE,
            cache=cache,
            direction=curr_dir,
            position=(curr_row, curr_col)
        )

        # Look a head to figure out what to do
        ahead_row = curr_row + curr_dir[0]
        ahead_col = curr_col + curr_dir[1]
        ahead_space = None
        try:
            ahead_space = area_map[ahead_row][ahead_col]
        except IndexError:
            # In front of the Guard is the VOID, exit carefully
            event_handler(area_map,
                EVENT_EXIT, direction=curr_dir, position=(curr_row, curr_col))
            on_map = False

        # check for obstacle & turn
        if ahead_space == OBSTACLE:
            # print("...obstacle // turn")
            # At Guard's current pos/dir, there's an OBSTACLE in front of her
            event_handler(area_map,
                EVENT_OBSTACLE,
                cache=cache,
                direction=curr_dir,
                position=(ahead_row,ahead_col)
            )

            # turn
            new_dir = TURN[curr_dir]

            event_handler(
                area_map,
                EVENT_TURN,
                cache=cache,
                position=(curr_row,curr_col),
                direction=new_dir
            )

            curr_dir = new_dir
        else:
            # print("...empty // move")
            curr_row = ahead_row
            curr_col = ahead_col


def find_guard(area_map:list[list[str]]) -> tuple[int,int]:
    guard_row = None
    guard_col = None
    for row, section in enumerate(area_map):
        if GUARD in section:
            guard_row = row
            guard_col = section.index(GUARD)
            break

    return guard_row, guard_col


def analyze_map(area_map:list[list[str]], event_handler) -> list[list[str]]:
    """
    Scan the `area_map` to map out the Guard's route using the rules:

    - If there is something directly in front of you, turn right 90 degrees.
    - Otherwise, take a step forward.

    Params:
        area_map (list): Map data loaded using `load_map()`

    Returns:
        list: A copy of the `area_map` with the Guard's route marked.

    >>> analyze_map(
    ... [['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ...  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ...  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ...  ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ...  ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
    ...  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ...  ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
    ...  ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ...  ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ...  ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']]
    ... )
    [['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '#'], ['.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.'], ['.', '.', '#', '.', 'X', '.', '.', '.', 'X', '.'], ['.', '.', 'X', 'X', 'X', 'X', 'X', '#', 'X', '.'], ['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'], ['.', '#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'], ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '#', '.'], ['#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'], ['.', '.', '.', '.', '.', '.', '#', 'X', '.', '.']]
    """
    marked_map = copy.deepcopy(area_map)

    # find starting position, e.g. the guard
    guard_dir = UP
    guard_row, guard_col = find_guard(marked_map)

    walk_map(
        marked_map,
        (guard_row, guard_col),
        guard_dir,
        event_handler
    )

    return marked_map


class StupidError(Exception):
    pass

def stupid_handler(area_map, event, **kwargs):
    if event in (EVENT_MOVE, EVENT_OBSTACLE):
        cache = kwargs.get("cache")
        direction = kwargs.get("direction")
        position = kwargs.get("position")

        vector = (position[0], position[1], direction[0], direction[1])
        if vector in cache:
        # if position in cache and cache.get(position) == direction:
            # print("...move // loop?")
            raise StupidError("Stuck in a Loop!")
        else:
            cache[vector] = 1


def stupid_solution(area_map):
    guard_dir = UP
    guard_row, guard_col = find_guard(area_map)
    # print(f"Guard @ ({guard_row},{guard_col})")

    count = 0
    for ridx, row in enumerate(area_map):
        for cidx, col in enumerate(row):
            if col == EMPTY:
                print(f"Trying ({ridx},{cidx})...")
                # place obstacle at r,c
                test_map = copy.deepcopy(area_map)
                # print(f"Trying ({ridx},{cidx})")
                test_map[ridx][cidx] = OBSTACLE

                # print_map(test_map)
                # input()

                # check if loop
                try:
                    walk_map(
                        test_map,
                        (guard_row, guard_col),
                        guard_dir,
                        stupid_handler
                    )
                except StupidError:
                    count += 1
                    # print(f"({ridx},{cidx}) - Loop Count: {count}")

    return count


def place_obstacles(area_map:list[list[str]]) -> list[list[str]]:
    marked_map = copy.deepcopy(area_map)

    dir_map = analyze_map(area_map, mark_directions)

    guard_dir = UP
    # find starting position, e.g. the guard
    guard_row, guard_col = find_guard(marked_map)
    # Mark loop obstacles from guard start pos
    walk_map(
        marked_map,
        (guard_row, guard_col),
        guard_dir,
        mark_obstacles
    )

    # walk_map(
    #     marked_map,
    #     (96, 44),
    #     LF,
    #     mark_obstacles
    #     # debug_handler
    # )

    # Mark loop obstacles from each turning point
    for row, section in enumerate(dir_map):
        for col, marker in enumerate(section):
            if marker in DIRECTION_LOOKUP.keys():
                # print(f"Start: ({row},{col}) | Heading: {marker}")
                walk_map(
                    marked_map,
                    (row,col),
                    DIRECTION_LOOKUP[marker],
                    mark_obstacles
                )

    return marked_map


def count(marked_map:list[list[str]], marker) -> int:
    """
    Count the number of unique positions that are marked on the `marked_map`

    >>> count_unique_positions([['^',' ','#','.','.',]])
    0

    >>> count_unique_positions(
    ... [
    ...     ['.','#','X','^','X'],
    ...     ['.','X','.','.','.'],
    ...     ['.','X','X','.','.'],
    ...     ['.','.','X','X','.'],
    ...     ['.','X','X','X','.']
    ... ]
    ... )
    10
    """
    total = 0

    for row in marked_map:
        total += row.count(marker)

    return total

# Event Handlers for `analyze_map`
def mark_obstacles(area_map, event, **kwargs):
    if event == EVENT_TURN:
        turns = kwargs.get("turns")
        turn_count = len(turns)

        if turn_count % 4 == 3:
            first_turn = turns[0]
            this_turn = turns[turn_count - 1]

            first_pos = first_turn.get("position")
            first_dir = first_turn.get("prev_dir")

            this_pos = this_turn.get("position")
            this_dir = this_turn.get("new_dir")

            # print(f"Turn #{turn_count} -> ({this_pos}) heading {DIRECTION_MARKER[this_dir]}")


            # figure out where to set new obstacle
            obst_row = None
            obst_col = None
            if this_dir == LF or this_dir == RT:
                obst_row = this_pos[0]
                obst_col = first_pos[1] + this_dir[1]#- 1
            elif this_dir == UP or this_dir == DN:
                obst_row = first_pos[0] + this_dir[0] # - 1
                obst_col = this_pos[1]

            is_valid = True
            # if there's already an obstacle closer than the new obstacle,
            # then not valid a valid position for a new obstacle

            # TODO: reFactor these tests
            # Moving UP
            if this_dir == UP:
                col = this_pos[1]
                for row in range(this_pos[0], obst_row, -1):
                    if area_map[row][col] == OBSTACLE:
                        is_valid = False

            # Moving DN
            if this_dir == DN:
                col = this_pos[1]
                for row in range(this_pos[0], obst_row, 1):
                    if area_map[row][col] == OBSTACLE:
                        is_valid = False

            # Moving RT
            if this_dir == RT:
                row = area_map[this_pos[0]]
                if OBSTACLE in row[this_pos[1]:obst_col]:
                    is_valid = False

            # Moving LF
            if this_dir == LF:
                row = area_map[this_pos[0]]
                if OBSTACLE in row[obst_col:this_pos[1]]:
                    is_valid = False

            # set obstacle
            if is_valid:
                if area_map[obst_row][obst_col] == OBSTACLE:
                    # raise RuntimeError(f"{this_pos} -> {this_dir} want to place a LOOP_OBSTACLE on top of an existing OBSTACLE at ({obst_row},{obst_col})")
                    pass
                else:
                    area_map[obst_row][obst_col] = LOOP_OBSTACLE
    elif event == EVENT_EXIT:
        pass
        # print(f"Exited Map at {kwargs.get('position')}")


def mark_directions(area_map, event, **kwargs):
    if event == EVENT_TURN:
        turns = kwargs.get("turns")
        turn_count = len(turns)
        last_turn = turns[turn_count - 1]

        pos = last_turn.get("position")
        direction = last_turn.get("new_dir")

        marker = DIRECTION_MARKER.get(direction)
        area_map[pos[0]][pos[1]] = marker


def mark_positions(area_map, event, **kwargs):
    if event == EVENT_MOVE:
        pos = kwargs.get("position")
        area_map[pos[0]][pos[1]] = POSITION_MARK


def debug_handler(area_map, event, **kwargs):
    if event == EVENT_TURN:
        turns = kwargs.get("turns")
        print(f"Debug // Turn #{len(turns)}")
    elif event == EVENT_OBSTACLE:
        print()
    elif event == EVENT_EXIT:
        print(f"Debug // Exit @ {kwargs.get('position')}")
