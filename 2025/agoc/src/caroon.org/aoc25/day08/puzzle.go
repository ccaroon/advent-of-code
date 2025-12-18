package day08

import (
	"caroon.org/aoc25/shared/space"
	"fmt"
	"github.com/ernestosuarez/itertools"
	"strconv"
	"strings"
)

const DayName string = "Day08"
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

	return -42
}

func solvePart2(boxPos []space.Point) int {
	return -42
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
		err = fmt.Errorf("%s - Unknown Part: [%s]\n", DayName, part)
	}

	if result == -42 {
		err = fmt.Errorf("%s - %s Not Implemented\n", DayName, part)
	}

	return result, err
}
