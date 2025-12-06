import inspect
import os
from abc import ABC, abstractmethod


class Puzzle(ABC):
    PART1 = 1
    PART2 = 2

    def __init__(self, **kwargs):
        module = inspect.getmodule(self.__class__)
        self.__path = os.path.dirname(module.__file__)

        self.__test_mode = kwargs.get("__test_mode", False)
        self.__debug_mode = kwargs.get("__debug_mode", False)

    @abstractmethod
    def _part1(self):
        """Entry point for the Part 1 Puzzle Code"""

    @abstractmethod
    def _part2(self):
        """Entry point for the Part 2 Puzzle Code"""

    def _debug(self, msg):
        if self.__debug_mode:
            print(msg)

    def _read_input(self, handler, nostrip=False):
        """
        Open an INPUT file, read & pass each line to a handler function

        Assumes a file name 'input.txt' or 'test-input.txt' in the same
        directory as the calling class.
        """
        file = f"{self.__path}/" + ("test-input.txt" if self.__test_mode else "input.txt")

        f"{self.__path}/input.txt"
        with open(file) as fptr:
            while line := fptr.readline():
                handler(line if nostrip else line.strip())

    def _submit_answer(self, answer, part):
        title = self.__class__.__doc__ + f" // Part #{part}"
        title += " (TEST)" if self.__test_mode else ""
        divider = "#" * len(title)
        print(f"{divider}\n{title}\n{divider}")
        print(f"Answer: {answer}")

    def main(self, part: int):
        answer = None
        if part == self.PART1:
            answer = self._part1()
        elif part == self.PART2:
            answer = self._part2()

        self._submit_answer(answer, part)
