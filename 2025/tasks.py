import base64
import importlib
import os

from cryptography.fernet import Fernet
from invoke import task

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ENC_KEY_FILE = f"{ROOT_DIR}/.aoc-password"
INPUT_DIR = f"{ROOT_DIR}/input"


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

        input_type = "example" if test else "input"
        input_file = f"{INPUT_DIR}/{day_name}-{input_type}.txt"

        puzzle = puzzle_class(input_file, **kwargs)
        puzzle.main(part=int(part))


@task
def genkey(_, passphrase):
    """Generate a Base64 Encoded Passphrase Key"""
    # key = Fernet.generate_key()
    # user_key = f"{passphrase:32}"
    user_key = passphrase.center(32, "-")
    b64_key = base64.urlsafe_b64encode(bytes(user_key, "utf-8"))

    with open(f"{ROOT_DIR}/.aoc-password", "wb") as fptr:
        fptr.write(b64_key)


@task
def add_input_file(_, day_num, src_path):
    """Add an Input File to the `input` dir and encrypt it"""
    enc_key = __read_enc_key()
    frnt = Fernet(enc_key)

    file_data = None
    with open(src_path, "rb") as fptr:
        file_data = fptr.read()

    enc_data = frnt.encrypt(file_data)
    out_file = f"{INPUT_DIR}/day{int(day_num):02}-input.enc"
    with open(out_file, "wb") as fptr:
        fptr.write(enc_data)

    os.remove(src_path)


@task
def decrypt_input(_):
    """Decrypt all `.enc` files in the `input` dir"""

    enc_key = __read_enc_key()
    frnt = Fernet(enc_key)
    for root, _, files in os.walk(INPUT_DIR):
        # print(root, files)
        for file in files:
            if file.endswith(".enc"):
                print(f"-> Decrypting {file}...")
                enc_data = None
                with open(f"{root}/{file}", "rb") as fptr:
                    enc_data = fptr.read()

                out_file = root + "/" + file.replace(".enc", ".txt")
                with open(out_file, "w") as fptr:
                    content = frnt.decrypt(enc_data)
                    fptr.write(content.decode())


@task
def clean(ctx):
    """De-clutter"""
    ctx.run("rm -f input/*-input.txt")


def __read_enc_key():
    with open(ENC_KEY_FILE, "rb") as fptr:
        enc_key = fptr.read()

    return enc_key  # noqa: RET504


#
