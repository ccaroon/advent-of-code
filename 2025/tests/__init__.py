from collections import namedtuple

AnswerSet = namedtuple("AnswerSet", ["part1", "part2"])


EXPECTED = [
    None,
    (AnswerSet(3, 6), AnswerSet(1092, 6616)),
    (AnswerSet(1227775554, 4174379265), AnswerSet(56660955519, 79183223243)),
]
