package day01

import (
	"fmt"
	"strings"
)

func (day *Day01) SolvePart1() error {
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

func (day *Day01) SolvePart2() error {
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
