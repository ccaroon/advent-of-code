package day07

import (
	"caroon.org/aoc25/shared/grid"
	"fmt"
	"slices"
	"strings"
)

const startMarker string = "S"
const splitterMarker string = "^"
const emptyMarker string = "."

// const beamMarker string = "|"

func solvePart1(tachyonManifold [][]string) int {
	var splitCount int = 0
	var exitRow int = len(tachyonManifold) - 1
	// Used to keep track of the active Beam locations
	// Don't really care about the value, just need the
	// uniqueness of the keys
	// Used in lieu of a mathematical set
	var beams map[grid.Location]bool = map[grid.Location]bool{}

	startCol := slices.Index(tachyonManifold[0], startMarker)
	startLoc := grid.Location{0, startCol}
	// Add the first beam to get started
	beams[startLoc] = true

	for len(beams) > 0 {
		beamsAdded := make(map[grid.Location]bool)
		beamsRemoved := make(map[grid.Location]bool)

		for beam, _ := range beams {
			if beam.Row != exitRow {
				// look south of beam to see what's there
				nextLoc := beam.Nearby(grid.S)
				nextSpace := tachyonManifold[nextLoc.Row][nextLoc.Col]

				if nextSpace == splitterMarker {
					splitCount += 1
					// Split the beam into two new beams
					newBeam1 := beam.Nearby(grid.SW)
					beamsAdded[newBeam1] = true

					newBeam2 := beam.Nearby(grid.SE)
					beamsAdded[newBeam2] = true

				} else if nextSpace == emptyMarker {
					// Move down/S
					newLoc := beam.Nearby(grid.S)
					// Add new beam pos
					beamsAdded[newLoc] = true
				}
			}
			// Remove the old beam
			beamsRemoved[beam] = true
		}

		// removed dead beams
		for loc, _ := range beamsRemoved {
			delete(beams, loc)
		}

		// add new beams
		for loc, _ := range beamsAdded {
			beams[loc] = true
		}

	}

	return splitCount
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
