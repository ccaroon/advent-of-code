package day06

import (
	"caroon.org/aoc25/shared"
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

// Ex: "1   2 3  4 55    7" => [1,2,3,4,55,7]
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
	var total int = 0
	var numCols int = len(data[0])
	var nums []int

	// The last line contains the operator for each column of numbers
	oneOrMoreSpace := regexp.MustCompile("\\s+")
	var ops []string = oneOrMoreSpace.Split(data[len(data)-1], -1)
	opsIdx := len(ops) - 1

	for cidx := numCols - 1; cidx >= 0; cidx -= 1 {
		// A Column consists of all the numbers (vertically) that make up
		// a single mathematics operation
		// Columns are divided by there being a space at the same cidx
		// in every row
		// 1 Math Problem == 1 Column
		colTotal := 0

		// "Walk" down each row at column cidx to gather the digits of the
		// number
		var digits []string
		for _, row := range data[0 : len(data)-1] {
			digits = append(digits, string(row[cidx]))
		}

		numStr := strings.TrimSpace(strings.Join(digits, ""))

		if numStr != "" {
			// Still collecting all the numbers in a math problem's Column
			number, _ := strconv.Atoi(numStr)
			nums = append(nums, number)
		}

		// Found Column divider or beyond first (0th) column
		// Compute the answer and reset for the next problem
		if numStr == "" || cidx == 0 {
			colTotal = shared.TotalIntList(nums, ops[opsIdx])

			// Add to column total
			total += colTotal

			// Reset nums to build next list of numbers
			nums = []int{}

			// Jump to the operator for the next column's problem
			opsIdx -= 1
		}
	}

	return total
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
