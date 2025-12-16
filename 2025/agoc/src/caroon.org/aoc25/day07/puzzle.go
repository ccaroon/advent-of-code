package day07

import (
	"caroon.org/aoc25/shared/grid"
	"fmt"
	"strings"
)

const startMarker string = "S"
const splitterMarker string = "^"
const emptyMarker string = "."
const beamMarker string = "|"

func solvePart1(tachyonManifold [][]string) int {
	location := grid.Location{0, 7}
	south := location.Nearby(grid.S)
	fmt.Println(location, south)

	location.Move(grid.E)
	fmt.Println(location)

	return 0
}

func solvePart2(tachyonManifold [][]string) int {
	return 0
}

func processInput(data []string) [][]string {
	var tachyonManifold [][]string

	for _, line := range data {
		markers := strings.Split(line, "")
		tachyonManifold = append(tachyonManifold, markers)
	}

	return tachyonManifold
}

func Exec(part string, data []string) (int, error) {
	var result int = 0
	var err error = nil

	tachyonManifold := processInput(data)
	if part == "PART1" {
		result = solvePart1(tachyonManifold)
	} else if part == "PART2" {
		result = solvePart2(tachyonManifold)
	} else {
		err = fmt.Errorf("Day07 - Unknown Part: [%s]\n", part)
	}

	return result, err
}
