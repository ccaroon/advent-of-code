package day01

import (
	"aoc15/puzzle"
	"fmt"
	"strings"
)

type Day01 puzzle.Puzzle

func New(part int, input []string) *Day01 {
	return &Day01{
		Title: "Not Quite LISP",
		Day:   1,
		Part:  part,
		Input: input,
	}
}

func (day *Day01) solvePart1() error {
	floor := 0
	directions := strings.Join(day.Input, "")
	numDirs := len(directions)

	for i := range numDirs {
		if directions[i] == '(' {
			floor += 1
		} else if directions[i] == ')' {
			floor -= 1
		} else {
			return fmt.Errorf("Invalid Input [%c]", directions[i])
		}
	}

	day.Answer = floor

	return nil
}

func (day *Day01) solvePart2() error {
	var basementPos int

	floor := 0
	directions := strings.Join(day.Input, "")
	numDirs := len(directions)

	for i := range numDirs {
		if directions[i] == '(' {
			floor += 1
		} else if directions[i] == ')' {
			floor -= 1
		} else {
			return fmt.Errorf("Invalid Input [%c]", directions[i])
		}

		if floor == -1 {
			basementPos = i + 1
			break
		}
	}

	day.Answer = basementPos
	return nil
}

func Solve(part int, input []string) (*puzzle.Puzzle, error) {
	var err error

	day := New(part, input)

	if day.Part == 1 {
		err = day.solvePart1()
	} else if day.Part == 2 {
		err = day.solvePart2()
	}

	puzzle := puzzle.Puzzle(*day)

	return &puzzle, err
}
