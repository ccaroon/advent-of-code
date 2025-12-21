# ruff: noqa: SLF001 (Private member accessed)
import unittest
from collections import namedtuple

AnswerSet = namedtuple("AnswerSet", ["part1", "part2"])

EXPECTED = [
    None,
    (AnswerSet(3, 6), AnswerSet(1092, 6616)),
    (AnswerSet(1227775554, 4174379265), AnswerSet(56660955519, 79183223243)),
    (AnswerSet(357, None), AnswerSet(17430, None)),
    (AnswerSet(13, 43), AnswerSet(1411, 8557)),
    (AnswerSet(3, None), AnswerSet(789, None)),
    (AnswerSet(4277556, 3263827), AnswerSet(5733696195703, 10951882745757)),
]


class PuzzleTestCase(unittest.TestCase):
    DAY_NUM: int
    PUZZLE_CLASS: type

    # Hide from test discovery
    __test__ = False

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Enable test discovery for subclasses
        cls.__test__ = True

    def setUp(self, **kwargs):
        self.answers = EXPECTED[self.DAY_NUM][1]
        self.puzzle = self.PUZZLE_CLASS()

        self.test_answers = EXPECTED[self.DAY_NUM][0]
        self.test_puzzle = self.PUZZLE_CLASS(__test_mode=True)

        self.args = kwargs

    def test_part1(self):
        if self.test_answers.part1 is None or self.answers.part1 is None:
            self.skipTest(f"DAY{self.DAY_NUM}:P1 -> Not Implemented!")

        self.assertEqual(self.test_puzzle._part1(), self.test_answers.part1)

        skip_p1_reason = self.args.get("skip_p1", None)
        if skip_p1_reason:
            self.skipTest(f"DAY{self.DAY_NUM}:P1 -> {skip_p1_reason}")
        self.assertEqual(self.puzzle._part1(), self.answers.part1)

    def test_part2(self):
        if self.test_answers.part2 is None or self.answers.part2 is None:
            self.skipTest(f"DAY{self.DAY_NUM}:P2 -> Not Implemented!")

        self.assertEqual(self.test_puzzle._part2(), self.test_answers.part2)

        skip_p2_reason = self.args.get("skip_p2", None)
        if skip_p2_reason:
            self.skipTest(f"DAY{self.DAY_NUM}:P2 -> {skip_p2_reason}")
        else:
            self.assertEqual(self.puzzle._part2(), self.answers.part2)
