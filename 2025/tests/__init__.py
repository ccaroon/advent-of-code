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

        self.part1 = self.__answer_data.get(f"day{self.DAY_NUM:02}", {}).get("part1", {})
        self.part2 = self.__answer_data.get(f"day{self.DAY_NUM:02}", {}).get("part2", {})

        self.puzzle = self.PUZZLE_CLASS(f"{self.TEST_DIR}/../input/day{self.DAY_NUM:02}-input.txt")
        self.test_puzzle = self.PUZZLE_CLASS(
            f"{self.TEST_DIR}/../input/day{self.DAY_NUM:02}-example.txt",
            __test_mode=True,
        )

        self.args = kwargs

    def test_part1(self):
        if self.part1.get("example") is None or self.part1.get("answer") is None:
            self.skipTest(f"DAY{self.DAY_NUM}:P1 -> Not Implemented!")

        skip_p1_reason = self.args.get("skip_p1", None)
        if skip_p1_reason:
            self.skipTest(f"DAY{self.DAY_NUM}:P1 -> {skip_p1_reason}")
        else:
            self.assertEqual(self.test_puzzle._part1(), self.part1["example"])
            self.assertEqual(self.puzzle._part1(), self.part1["answer"])

    def test_part2(self):
        if self.part2.get("example") is None or self.part2.get("answer") is None:
            self.skipTest(f"DAY{self.DAY_NUM}:P2 -> Not Implemented!")

        skip_p2_reason = self.args.get("skip_p2", None)
        if skip_p2_reason:
            self.skipTest(f"DAY{self.DAY_NUM}:P2 -> {skip_p2_reason}")
        else:
            self.assertEqual(self.test_puzzle._part2(), self.part2["example"])
            self.assertEqual(self.puzzle._part2(), self.part2["answer"])
