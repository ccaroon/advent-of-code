#!/usr/bin/env python
import argparse
import pprint

from maze_mapper import MazeMapper

def main(args) -> None:
    """Day 16 // Puzzle 01"""

    mm = MazeMapper(args.input_file)
    # print(mm)
    low_score = mm.analyze(max_iter=args.max_iter)

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> Maze Size: {mm.size}
-> Start/End: {mm.start}/{mm.end}
-> Low Score: {low_score}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./maze.map"
    )
    parser.add_argument("--max-iter", "-m", type=int, default=50)
    args = parser.parse_args()

    main(args)
