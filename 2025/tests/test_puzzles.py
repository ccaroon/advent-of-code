# from aoc.day01.puzzle import SecretEntrance

import aoc.day01.puzzle
import aoc.day02.puzzle
import aoc.day03.puzzle
import aoc.day04.puzzle
import aoc.day05.puzzle
import aoc.day06.puzzle

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


#
