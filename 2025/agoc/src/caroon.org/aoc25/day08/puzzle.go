package day08

import (
	"caroon.org/aoc25/shared/space"
	"fmt"
	"github.com/ernestosuarez/itertools"
	"strconv"
	"strings"
)

const Title string = "Playground"

func solvePart1(boxPos []space.Point) int {
	var pointList itertools.List

	// build List of Points for itertools
	for _, point := range boxPos {
		pointList = append(pointList, point)
	}

	// combos := itertools.CombinationsList(pointList, 2)
	// for thing := range combos {
	// 	fmt.Println(thing[0], thing[1])
	// }

	return 0
}

func solvePart2(boxPos []space.Point) int {
	return 0
}

func processInput(data []string) []space.Point {
	var positions []space.Point

	for _, line := range data {
		coords := strings.SplitN(line, ",", 3)
		x, _ := strconv.Atoi(coords[0])
		y, _ := strconv.Atoi(coords[1])
		z, _ := strconv.Atoi(coords[2])

		positions = append(positions, space.Point{x, y, z})
	}

	return positions
}

func Exec(part string, data []string) (int, error) {
	var result int = 0
	var err error = nil

	boxPos := processInput(data)

	if part == "PART1" {
		result = solvePart1(boxPos)
	} else if part == "PART2" {
		result = solvePart2(boxPos)
	} else {
		err = fmt.Errorf("Day08 - Unknown Part: [%s]\n", part)
	}

	return result, err
}
