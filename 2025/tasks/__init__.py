import importlib
from invoke import task

PUZZLES = {
    "day01": "SecretEntrance"
}

@task(
    iterable=["args"],
    help={
        "day": "Day Ordinal: 1,2,3...12 | day1, day2 ... day12",
        "part": "Puzzle Part: 1 or 2",
        "test": "Use test-input.txt instead of input.txt",
        "debug": "Enable debug messages",
        "args": "Arguments to pass to the puzzle in name=value pairs"
    }
)
def run(ctx, day, part, test=False, debug=False, args=None):
    """ Run an AOC-2025 Puzzle by `day` & `part` """

    day_name = None
    if day.startswith("day"):
        day_name = day.lower()
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
        PuzzleClass = getattr(module, cls_name)

        kwargs = {
            "__test_mode": test,
            "__debug_mode": debug
        }
        for arg in args:
            if "=" in arg:
                (key, value) = arg.split("=", 2)
                kwargs[key] = value
            else:
                kwargs[arg] = True

        puzzle = PuzzleClass(**kwargs)
        puzzle.main(part=int(part))
