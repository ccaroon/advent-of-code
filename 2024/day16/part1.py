#!/usr/bin/env python
import argparse
import pprint

from maze_mapper import MazeMapper

def main(args) -> None:
    """Day 16 // Part 01"""

    mm = MazeMapper(args.input_file)

    # ---------------------------------
    low_score = mm.analyze(
        max_rdeer=args.max_rdeer,
        max_iter=args.max_iter,
        visual=args.visual
    )
    # ---------------------------------
    # low_score = mm.analyze2(
    #     max_iter=args.max_iter,
    #     visual=args.visual
    # )

    print(f"""{main.__doc__}
-> Input File: {args.input_file}
-> Maze Size: {mm.size}
-> Iterations/Deer: {args.max_iter} | {args.max_rdeer}
-> Start/End: {mm.start}/{mm.end}
-> Low Score: {low_score}
""")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=main.__doc__)

    parser.add_argument(
        "input_file", nargs="?",
        default="./maze.map"
    )
    parser.add_argument("--max-iter", "-i", type=int, default=250)
    parser.add_argument("--max-rdeer", "-d", type=int, default=1000)
    parser.add_argument("--visual", choices=("manual", "auto"), default=None)
    args = parser.parse_args()

    main(args)
