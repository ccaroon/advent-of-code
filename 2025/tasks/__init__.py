import importlib

from invoke import task


@task
def run(ctx, name):
    """ Run an AOC-2025 Puzzle by day name """
    day = importlib.import_module(f"aoc.{name}.puzzle")
    puzzle = day.Puzzle()

    puzzle.main()
