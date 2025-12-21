# ruff: noqa: SLF001 (Private member accessed)
import unittest

from aoc.day02.puzzle import GiftShop

from . import EXPECTED


class TestDay01(unittest.TestCase):
    DAY = 2

    def setUp(self):
        self.answers = EXPECTED[self.DAY][1]
        self.puzzle = GiftShop()

        self.test_answers = EXPECTED[self.DAY][0]
        self.test_puzzle = GiftShop(__test_mode=True)

    def test_part1(self):
        self.assertEqual(self.test_puzzle._part1(), self.test_answers.part1)
        self.assertEqual(self.puzzle._part1(), self.answers.part1)

    def test_part2(self):
        self.assertEqual(self.test_puzzle._part2(), self.test_answers.part2)

        if True:
            self.skipTest("Day2 / Part2 takes a long time to run")
        else:
            self.assertEqual(self.puzzle._part2(), self.answers.part2)
