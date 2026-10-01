package day01

import (
	"aoc15/shared"
	"strings"
)

func Part1(inputFile string) int {
	input := shared.ReadInputFile(inputFile)

	floor := 0
	directions := strings.Join(input, "")
	numDirs := len(directions)

	for i := range numDirs {
		if directions[i] == '(' {
			floor += 1
		} else if directions[i] == ')' {
			floor -= 1
		} else {
			panic("WTF!")
		}
	}

	return floor
}

func Part2(inputFile string) int {
	var basementPos int
	input := shared.ReadInputFile(inputFile)

	floor := 0
	directions := strings.Join(input, "")
	numDirs := len(directions)

	for i := range numDirs {
		if directions[i] == '(' {
			floor += 1
		} else if directions[i] == ')' {
			floor -= 1
		} else {
			panic("WTF!")
		}

		if floor == -1 {
			basementPos = i + 1
			break
		}
	}

	return basementPos
}
