# Advent Of Code 2015
https://adventofcode.com/2015

Theme: Fix Santa's Snow Machine


## Go
* [x] ⭐️⭐️ [Day 01: Not Quite Lisp](./aoc15/day01/)


### Development
Code lives in the `aoc15` go module.

1. ...write code and/or unit tests for example input...
    - Each Day's puzzle is implemented as a separate package which must contain a `Solve(part int, input []string) (*puzzle.Puzzle, error)` function.
    - If adding a new Day's Puzzle solution, then you'll need to add a case to the `switch` statement in `main.go`.
2. Run Examples: `mage test <day> [-part=part]`
3. Run Solution:
    * `mage run <day> <part>`
    * -OR-
    * `go build .`
    * `./aoc15 <day> <part> <input-file>`
        - `day`: Int representing which Day's Puzzle.
        - `part`: Int representing which Puzzle Part.
        - `input-file`: Full or relative directory to an input file
4. ...repeat...
