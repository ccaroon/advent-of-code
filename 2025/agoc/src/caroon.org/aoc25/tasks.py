from invoke import task

@task(
    help={
        "day": "Day Ordinal: 1,2,3...12 | day1, day2 ... day12",
        "part": "Puzzle Part: 1 or 2",
        "test": "Use test-input.txt instead of input.txt",
    },
)
def run(ctx, day, part, *, test=False):
    """Compile `aoc25` and run the specified Day & Part"""

    day_id = None
    day_name = None
    if day.startswith("day"):
        day_id = int(day[3:])
    else:
        day_id = int(day)

    day_name = f"day{day_id:02}"

    if part.startswith("part"):
        part_name = part.lower()
    else:
        part_name = f"part{part}"

    input_file = "test-input.txt" if test else "input.txt"

    # compile
    ctx.run("go build")

    # run
    ctx.run(f"./aoc25 {day_name} {part_name} {input_file}")


@task
def clean(ctx):
    """ Go Clean """
    ctx.run("go clean")


@task(
    aliases=['format']
)
def fmt(ctx):
    """ Format the Code """
    ctx.run("go fmt ./...")
