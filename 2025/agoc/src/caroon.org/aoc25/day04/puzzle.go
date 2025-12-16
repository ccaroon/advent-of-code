package day04

import (
	"caroon.org/aoc25/shared/grid"
	"fmt"
	"strings"
)

const removedRollMark string = "x"
const maxNearbyRolls int = 4
const paperRollMark string = "@"

func countRolls(paperRolls [][]string, row int, col int) int {
	var count int = 0
	var width int = len(paperRolls[0])
	var height int = len(paperRolls)

	for _, direction := range grid.Directions {
		ridx := row + direction.RowOffset
		cidx := col + direction.ColOffset

		if (ridx >= 0 && ridx < height) &&
			(cidx >= 0 && cidx < width) &&
			(paperRolls[ridx][cidx] == paperRollMark) {
			count += 1
		}
	}

	return count
}

func solvePart1(paperRolls [][]string) int {
	var count int = 0

	for ridx, row := range paperRolls {
		for cidx, item := range row {
			if item == paperRollMark {
				numRolls := countRolls(paperRolls, ridx, cidx)
				if numRolls < maxNearbyRolls {
					count += 1
				}
			}
		}
	}

	return count
}

func solvePart2(paperRolls [][]string) int {
	var totalRemoved int = 0
	var canRemove bool = true

	for canRemove != false {
		numRemoved := 0
		for ridx, row := range paperRolls {
			for cidx, item := range row {
				if item == paperRollMark {
					numRolls := countRolls(paperRolls, ridx, cidx)

					if numRolls < maxNearbyRolls {
						paperRolls[ridx][cidx] = removedRollMark
						numRemoved += 1
					}

				}

			}
		}

		if numRemoved > 0 {
			totalRemoved += numRemoved
		} else {
			canRemove = false
		}

	}

	return totalRemoved
}

// Convert array of strings
// [
//
//	".@.@.",
//	"@...@"
//
// ]
// into 2D array
// [
//
//	[".","@",".","@","."],
//	["@",".",".",".","@"]
//
// ]
func processInput(data []string) [][]string {
	var paperRolls [][]string

	for _, line := range data {
		row := strings.Split(line, "")
		paperRolls = append(paperRolls, row)
	}

	return paperRolls
}

func Exec(part string, data []string) (int, error) {
	var result int = 0
	var err error = nil

	paperRolls := processInput(data)

	if part == "PART1" {
		result = solvePart1(paperRolls)
	} else if part == "PART2" {
		result = solvePart2(paperRolls)
	} else {
		err = fmt.Errorf("Day04 - Unknown Part: [%s]\n", part)
	}

	return result, err
}
