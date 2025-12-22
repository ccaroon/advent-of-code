# ruff: noqa: SLF001 (Private member accessed)
import os
import unittest

import tomllib


class PuzzleTestCase(unittest.TestCase):
    DAY_NUM: int
    PUZZLE_CLASS: type

    TEST_DIR = os.path.dirname(os.path.abspath(__file__))

    # Hide from test discovery
    __test__ = False

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Enable test discovery for subclasses
        cls.__test__ = True

    def __load_answers(self):
        data = None
        with open(f"{self.TEST_DIR}/answers.toml", "rb") as fptr:
            data = tomllib.load(fptr)

        return data  # noqa: RET504

    def setUp(self, **kwargs):
        if not hasattr(self, "__answer_data") or self.__answer_data is None:
            self.__answer_data = self.__load_answers()

        self.answers = self.__answer_data.get(f"day{self.DAY_NUM:02}", {}).get("answer", {})
        # EXPECTED[self.DAY_NUM][1]
        self.puzzle = self.PUZZLE_CLASS()

        self.test_answers = self.__answer_data.get(f"day{self.DAY_NUM:02}", {}).get("example", {})
        # EXPECTED[self.DAY_NUM][0]
        self.test_puzzle = self.PUZZLE_CLASS(__test_mode=True)

        self.args = kwargs

    def test_part1(self):
        if self.test_answers.get("part1") is None or self.answers.get("part1") is None:
            self.skipTest(f"DAY{self.DAY_NUM}:P1 -> Not Implemented!")

        self.assertEqual(self.test_puzzle._part1(), self.test_answers["part1"])

        skip_p1_reason = self.args.get("skip_p1", None)
        if skip_p1_reason:
            self.skipTest(f"DAY{self.DAY_NUM}:P1 -> {skip_p1_reason}")
        self.assertEqual(self.puzzle._part1(), self.answers["part1"])

    def test_part2(self):
        if self.test_answers.get("part2") is None or self.answers.get("part2") is None:
            self.skipTest(f"DAY{self.DAY_NUM}:P2 -> Not Implemented!")

        self.assertEqual(self.test_puzzle._part2(), self.test_answers["part2"])

        skip_p2_reason = self.args.get("skip_p2", None)
        if skip_p2_reason:
            self.skipTest(f"DAY{self.DAY_NUM}:P2 -> {skip_p2_reason}")
        else:
            self.assertEqual(self.puzzle._part2(), self.answers["part2"])
