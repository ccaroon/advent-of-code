import importlib

from invoke import task

PUZZLES = {
    "day01": "SecretEntrance",
    "day02": "GiftShop",
    "day03": "Lobby",
    "day04": "PrintingDepartment",
    "day05": "Cafeteria",
    "day06": "TrashCompactor",
    "day07": "Laboratories",
    "day08": "Playground",
    "day09": "MovieTheater",
    "day10": "Factory",
    "day11": "Reactor",
    "day12": "ChristmasTreeFarm",
}


@task(
    iterable=["arg"],
    help={
        "day": "Day Ordinal: 1,2,3...12 | day1, day2 ... day12",
        "part": "Puzzle Part: 1 or 2",
        "test": "Use test-input.txt instead of input.txt",
        "debug": "Enable debug messages",
        "arg": "Arguments to pass to the puzzle in name=value pairs",
    },
)
def run(_, day, part, *, test=False, debug=False, arg=None):
    """Run an AOC-2025 Puzzle by `day` & `part`"""

    day_id = None
    day_name = None
    if day.startswith("day"):
        day_id = int(day[3:])
    else:
        day_id = int(day)

    day_name = f"day{day_id:02}"

    cls_name = PUZZLES.get(day_name)

    if cls_name is None:
        print(f"=> Invalid day '{day}' [{day_name}]! Did you forget to update the PUZZLES map?")
    else:
        # aoc.<day_name>.puzzle.<cls_name>
        # aoc.day01.puzzle.SecretEntrance
        module = importlib.import_module(f"aoc.{day_name}.puzzle")
        puzzle_class = getattr(module, cls_name)

        kwargs = {
            "day": day_name,
            "__test_mode": test,
            "__debug_mode": debug,
        }
        for arg_pair in arg:
            if "=" in arg_pair:
                (name, value) = arg_pair.split("=", 2)
                kwargs[name] = value
            else:
                kwargs[arg] = True

        puzzle = puzzle_class(**kwargs)
        puzzle.main(part=int(part))
