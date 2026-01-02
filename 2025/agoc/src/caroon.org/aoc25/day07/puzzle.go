package day07

import (
	"fmt"
	"slices"
	"strings"

	"caroon.org/aoc25/shared/grid"
)

const DayName string = "Day07"
const Title string = "Laboratories"

const startMarker string = "S"
const splitterMarker string = "^"
const emptyMarker string = "."

type Node struct {
	marker string
	loc    grid.Location
}

func solvePart1(tachyonManifold [][]string) int {
	var splitCount int = 0
	var exitRow int = len(tachyonManifold) - 1
	// Used to keep track of the active Beam locations
	// Don't really care about the value, just need the
	// uniqueness of the keys
	// Used in lieu of a mathematical set
	var beams map[grid.Location]bool = map[grid.Location]bool{}

	startCol := slices.Index(tachyonManifold[0], startMarker)
	startLoc := grid.Location{Row: 0, Col: startCol}
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

func traverseManifold(tachyonManifold [][]string, currNode Node, cache map[Node]int) int {
	var timelines int = 0
	newNodes := []Node{}

	if cache[currNode] > 0 {
		timelines = cache[currNode]
	} else {
		switch currNode.marker {
		case startMarker:
			fallthrough
		case emptyMarker:
			loc := currNode.loc.Nearby(grid.S)
			marker := tachyonManifold[loc.Row][loc.Col]
			node := Node{marker: marker, loc: loc}
			newNodes = append(newNodes, node)
		case splitterMarker:
			timelines += 1
			for _, direction := range []grid.Direction{grid.SE, grid.SW} {
				loc := currNode.loc.Nearby(direction)
				marker := tachyonManifold[loc.Row][loc.Col]
				node := Node{marker: marker, loc: loc}
				newNodes = append(newNodes, node)
			}
		}

		for _, node := range newNodes {
			if node.loc.Row < len(tachyonManifold)-1 {
				timelines += traverseManifold(tachyonManifold, node, cache)
			}
		}
		cache[currNode] = timelines
	}

	return timelines
}

func solvePart2(tachyonManifold [][]string) int {
	// Start in current timeline ... of which there is 1
	var timelines int = 1
	// For memoization
	var cache map[Node]int = make(map[Node]int)

	startCol := slices.Index(tachyonManifold[0], startMarker)
	startLoc := grid.Location{Row: 0, Col: startCol}
	startNode := Node{marker: startMarker, loc: startLoc}

	// cache -> to Memoize the traverseManfold function
	timelines += traverseManifold(tachyonManifold, startNode, cache)

	return timelines
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
		err = fmt.Errorf("%s - Unknown Part: [%s]\n", DayName, part)
	}

	if result == -42 {
		err = fmt.Errorf("%s - %s Not Implemented\n", DayName, part)
	}

	return result, err
}
