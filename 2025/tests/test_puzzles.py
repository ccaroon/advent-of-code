import aoc.day01.puzzle
import aoc.day02.puzzle
import aoc.day03.puzzle
import aoc.day04.puzzle
import aoc.day05.puzzle
import aoc.day06.puzzle
import aoc.day07.puzzle
import aoc.day08.puzzle
import aoc.day09.puzzle
import aoc.day10.puzzle
import aoc.day11.puzzle
import aoc.day12.puzzle

from . import PuzzleTestCase


class TestDay01(PuzzleTestCase):
    DAY_NUM = 1
    PUZZLE_CLASS = aoc.day01.puzzle.SecretEntrance

    def setUp(self):
        return super().setUp()


class TestDay02(PuzzleTestCase):
    DAY_NUM = 2
    PUZZLE_CLASS = aoc.day02.puzzle.GiftShop

    def setUp(self):
        return super().setUp(
            skip_p2="takes a long time to run",
        )


class TestDay03(PuzzleTestCase):
    DAY_NUM = 3
    PUZZLE_CLASS = aoc.day03.puzzle.Lobby

    def setUp(self):
        return super().setUp()


class TestDay04(PuzzleTestCase):
    DAY_NUM = 4
    PUZZLE_CLASS = aoc.day04.puzzle.PrintingDepartment

    def setUp(self):
        return super().setUp()


class TestDay05(PuzzleTestCase):
    DAY_NUM = 5
    PUZZLE_CLASS = aoc.day05.puzzle.Cafeteria

    def setUp(self):
        return super().setUp()


class TestDay06(PuzzleTestCase):
    DAY_NUM = 6
    PUZZLE_CLASS = aoc.day06.puzzle.TrashCompactor

    def setUp(self):
        return super().setUp()


class TestDay07(PuzzleTestCase):
    DAY_NUM = 7
    PUZZLE_CLASS = aoc.day07.puzzle.Laboratories

    def setUp(self):
        return super().setUp()


class TestDay08(PuzzleTestCase):
    DAY_NUM = 8
    PUZZLE_CLASS = aoc.day08.puzzle.Playground

    def setUp(self):
        return super().setUp(skip_p1="Not implemented in Python (Yet!)")


class TestDay09(PuzzleTestCase):
    DAY_NUM = 9
    PUZZLE_CLASS = aoc.day09.puzzle.MovieTheater

    def setUp(self):
        return super().setUp()


class TestDay10(PuzzleTestCase):
    DAY_NUM = 10
    PUZZLE_CLASS = aoc.day10.puzzle.Factory

    def setUp(self):
        return super().setUp()


class TestDay11(PuzzleTestCase):
    DAY_NUM = 11
    PUZZLE_CLASS = aoc.day11.puzzle.Reactor

    def setUp(self):
        return super().setUp()


class TestDay12(PuzzleTestCase):
    DAY_NUM = 12
    PUZZLE_CLASS = aoc.day12.puzzle.ChristmasTreeFarm

    def setUp(self):
        return super().setUp()


#
