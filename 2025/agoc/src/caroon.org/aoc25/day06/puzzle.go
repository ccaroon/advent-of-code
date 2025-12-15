package day06

import (
	"caroon.org/aoc25/shared"
	"fmt"
	"regexp"
	"strconv"
)

// "1   2 3  4 55    7" => [1,2,3,4,55,7]
func spaceSepNumsToIntArray(numStr string) []int {
	var numberList []int
	var splitRe *regexp.Regexp = regexp.MustCompile("\\s+")

	for _, num := range splitRe.Split(numStr, -1) {
		if num != "" {
			number, _ := strconv.Atoi(num)
			numberList = append(numberList, number)
		}
	}

	return numberList
}

func solvePart1(data []string) int {
	oneOrMoreSpace := regexp.MustCompile("\\s+")
	// The last line contains the operator for each column of numbers
	var ops []string = oneOrMoreSpace.Split(data[len(data)-1], -1)

	// Use the first line to initialize the answers for each column of nums
	var answers []int = spaceSepNumsToIntArray(data[0])

	// Split each additional line and add/mult each number for the
	// appropriate column
	// Exclude first line and last line
	// ...first line used to init totals
	// ...last line contains operators
	endIdx := len(data) - 1
	for _, line := range data[1:endIdx] {
		var numbers []int = spaceSepNumsToIntArray(line)

		for idx, num := range numbers {
			op := ops[idx]
			switch op {
			case "+":
				answers[idx] += num
			case "*":
				answers[idx] *= num
			}
		}
	}

	return shared.SumIntList(answers)
}

func solvePart2(data []string) int {
	return 0
}

func Exec(part string, data []string) (int, error) {
	var result int = 0
	var err error = nil

	if part == "PART1" {
		result = solvePart1(data)
	} else if part == "PART2" {
		result = solvePart2(data)
	} else {
		err = fmt.Errorf("Day06 - Unknown Part: [%s]\n", part)
	}

	return result, err
}
