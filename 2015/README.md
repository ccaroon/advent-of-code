# Advent Of Code 2015
https://adventofcode.com/2015

Theme: Fix Santa's Snow Machine

Icons: [⭐️🚫]

## Go
* [x] ⭐️⭐️ [Day 01: Not Quite Lisp](./aoc15/day01)
* [x] ⭐️⭐️ [Day 02: I Was Told There Would Be No Math](./aoc15/day02)
* [x] ⭐️⭐️ [Day 03: Perfectly Spherical Houses in a Vacuum](./aoc15/day03)
* [x] ⭐️⭐️ [Day 04: The Ideal Stocking Stuffer](./aoc15/day04)
* [x] ⭐️⭐️ [Day 05: Doesn't He Have Intern-Elves For This?](./aoc15/day05)
* [ ] ⭐️🚫 [Day 06: Probably a Fire Hazard](./aoc15/day06)

### Development
Code lives in the `aoc15` go module.

1. ...write code and/or unit tests for example input...
    - If adding a new Day's Puzzle...
        + `cp -a dayTmpl aoc15/day0N`
        + Search & replace all `0X` with `0N`
        + Write puzzle solution code
        + Update unit test cases
        + add a case to the `switch` statement in `main.go`.
2. Run Examples: `mage test <day> <part>`
    - if `<part>` is `0` then run test for both parts
3. Run Solution:
    * `mage run <day> <part>`
    * -OR-
    * `go build .`
    * `./aoc15 <day> <part> <input-file>`
        - `day`: Int representing which Day's Puzzle.
        - `part`: Int representing which Puzzle Part.
        - `input-file`: Full or relative directory to an input file
4. ...repeat...
