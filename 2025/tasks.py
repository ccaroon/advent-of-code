import base64
import importlib
import os

from cryptography.fernet import Fernet
from invoke import task

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


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

    day_id = int(day[3:]) if day.startswith("day") else int(day)
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


@task
def genkey(_, passphrase):
    # key = Fernet.generate_key()
    # user_key = f"{passphrase:32}"
    user_key = passphrase.center(32, "-")
    b64_key = base64.urlsafe_b64encode(bytes(user_key, "utf-8"))

    with open(f"{ROOT_PATH}/.aoc-password", "wb") as fptr:
        fptr.write(b64_key)

    print(ROOT_PATH)


@task
def add_input_file(_, day_num, src_path):
    # read enc key
    key_file = f"{ROOT_PATH}/.aoc-password"
    if os.path.exists(key_file):
        enc_key = None
        with open(key_file, "rb") as fptr:
            enc_key = fptr.read()

        frnt = Fernet(enc_key)

        file_data = None
        with open(src_path, "rb") as fptr:
            file_data = fptr.read()

        enc_data = frnt.encrypt(file_data)
        out_file = f"{ROOT_PATH}/input/day{int(day_num):02}-input.enc"
        with open(out_file, "wb") as fptr:
            fptr.write(enc_data)

        os.remove(src_path)
    else:
        print(f"=> Missing Key File: {key_file}")


#
