package day03

import (
	"fmt"
	"strconv"
)

func findLargestBattery(bank []int, start int) (int, int) {
	var foundIdx int = 0
	var maxValue int = 0

	for idx, battery := range bank[start:] {
		if battery > maxValue {
			maxValue = battery
			foundIdx = start + idx
		}
	}

	return foundIdx, maxValue
}

func solvePart1(data []string) int {
	var totalJoltage int = 0

	// find the largest number in the bank starting at the beginning
	// ...but can't be the last number in the bank/list.
	// then find the largest number starting from the first num's position
	// concat, convert to int
	for _, bank := range data {
		var batteries []int
		// # convert to a list of ints
		for _, batt := range bank {
			bValue, _ := strconv.Atoi(string(batt))
			batteries = append(batteries, bValue)
		}

		// find the largest battery in the bank, EXCLUDING the last one
		// ...since no battery can follow it
		endIdx := len(batteries) - 1
		b1Idx, batt1 := findLargestBattery(batteries[:endIdx], 0)

		// find the largest battery AFTER the position of the first largest
		_, batt2 := findLargestBattery(batteries, b1Idx+1)

		joltage, _ := strconv.Atoi(fmt.Sprintf("%d%d", batt1, batt2))
		totalJoltage += joltage
	}

	return totalJoltage
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
		err = fmt.Errorf("Day03 - Unknown Part: [%s]\n", part)
	}

	return result, err
}
