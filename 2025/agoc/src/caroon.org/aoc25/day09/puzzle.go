package day09

import (
	"caroon.org/aoc25/shared/grid"
	"fmt"
	"github.com/ernestosuarez/itertools"
	"math"
	"strconv"
	"strings"
)

func solvePart1(tileLocs []grid.Location) int {
	// For every combination of 2 red-tiles, compute the
	// area and find the max
	var maxArea float64 = 0.0
	var tileList itertools.List

	// build List of tile locations for itertools
	for _, loc := range tileLocs {
		tileList = append(tileList, loc)
	}

	combos := itertools.CombinationsList(tileList, 2)
	for locPair := range combos {
		maxArea = math.Max(
			maxArea,
			grid.ComputeArea(
				locPair[0].(grid.Location),
				locPair[1].(grid.Location),
			),
		)
	}

	return int(maxArea)
}

func solvePart2(tileLocs []grid.Location) int {
	return 0
}

func processInput(data []string) []grid.Location {
	var tileLocs []grid.Location

	for _, line := range data {
		coords := strings.SplitN(line, ",", 2)
		row, _ := strconv.Atoi(coords[0])
		col, _ := strconv.Atoi(coords[1])

		tileLocs = append(tileLocs, grid.Location{row, col})
	}

	return tileLocs
}

func Exec(part string, data []string) (int, error) {
	var result int = 0
	var err error = nil

	tileLocs := processInput(data)

	if part == "PART1" {
		result = solvePart1(tileLocs)
	} else if part == "PART2" {
		result = solvePart2(tileLocs)
	} else {
		err = fmt.Errorf("Day09 - Unknown Part: [%s]\n", part)
	}

	return result, err
}
