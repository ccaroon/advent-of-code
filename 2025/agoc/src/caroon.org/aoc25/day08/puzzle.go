package day08

import (
	"cmp"
	"fmt"
	"slices"
	"strconv"
	"strings"

	"caroon.org/aoc25/shared/space"
	"github.com/ernestosuarez/itertools"
)

const DayName string = "Day08"
const Title string = "Playground"

type JBoxPair struct {
	jBox1, jBox2 space.Point
	dist         float64
}

func solvePart1(boxPos []space.Point) int {
	var pointList itertools.List
	var jBoxPairs []JBoxPair
	var circuits []*Circuit

	// build List of Points for itertools
	for _, point := range boxPos {
		pointList = append(pointList, point)
	}
	combos := itertools.CombinationsList(pointList, 2)

	// Find the distance between each pair of junction boxes
	for pair := range combos {
		jBox1 := pair[0].(space.Point)
		jBox2 := pair[1].(space.Point)
		dist := jBox1.DistanceTo(jBox2)

		jBoxPairs = append(jBoxPairs, JBoxPair{jBox1, jBox2, dist})
	}

	// Sort junction box pairs by distance
	distCmp := func(a, b JBoxPair) int {
		return cmp.Compare(a.dist, b.dist)
	}
	slices.SortFunc(jBoxPairs, distCmp)

	// circuit ID - mainly for debugging purposes
	cId := 0
	// NOTE: for test input, only examine the first 10 pairs
	for _, jBoxPair := range jBoxPairs[:1000] {
		addNewCircuit := true
		// list if the indexes of the circuits that are modified
		// i.e. one or more junction boxes are connected to it
		var modCircuits []int
		for idx, circuit := range circuits {
			if circuit.isConnectedTo(jBoxPair.jBox1) && !circuit.isConnectedTo(jBoxPair.jBox2) {
				// fmt.Printf("->  Adding jBox2 to Circuit #%d\n", circuit.id)
				circuit.addJunctionBox(jBoxPair.jBox2)
				addNewCircuit = false
				// fmt.Printf("->  %v\n", circuit)
				modCircuits = append(modCircuits, idx)
			} else if !circuit.isConnectedTo(jBoxPair.jBox1) && circuit.isConnectedTo(jBoxPair.jBox2) {
				// fmt.Printf("->  Adding jBox1 to Circuit #%d\n", circuit.id)
				circuit.addJunctionBox(jBoxPair.jBox1)
				addNewCircuit = false
				// fmt.Printf("->  %v\n", circuit)
				modCircuits = append(modCircuits, idx)
			} else if circuit.isConnectedTo(jBoxPair.jBox1) && circuit.isConnectedTo(jBoxPair.jBox2) {
				// mark as not needing a new Circuit
				addNewCircuit = false
				// fmt.Printf("->  NoOp - jBox1 & jBox2 already connected to Circuit #%d\n", circuit.id)
				// fmt.Printf("->  %v\n", circuit)
			}
		}

		// Merge any Circuits that should now be connected b/c the jBoxPair
		// is part of more than 1 Circuit
		if len(modCircuits) > 1 {
			baseCircuit := circuits[modCircuits[0]]
			// Merge all modified Circuits into the first one
			for _, cIdx := range modCircuits[1:] {
				baseCircuit.merge(circuits[cIdx])
			}

			// Delete the circuits that were merged
			// Circuits to be deleted are NOT necessarily consecutive
			for _, cIdx := range modCircuits[1:] {
				circuits = slices.Delete(circuits, cIdx, cIdx+1)
			}
		}

		if addNewCircuit {
			// fmt.Printf("->  Creating New Circuit #%d\n", cId)
			newCircuit := NewCircuit(cId, []space.Point{jBoxPair.jBox1, jBoxPair.jBox2})
			circuits = append(circuits, newCircuit)
			cId++
			// fmt.Printf("->  %v\n", newCircuit)
		}
	}

	// Sort all Circuits by their length b/c we only need to know the
	// top three largest by length
	lenCmp := func(a, b *Circuit) int {
		return cmp.Compare(a.length(), b.length())
	}
	slices.SortFunc(circuits, lenCmp)

	// Print all Circuits for debuggin'
	// for _, circuit := range circuits {
	// 	fmt.Printf("%d) len [%d]\n", circuit.id, circuit.length())
	// }

	// Compute Answer
	result := 1
	lastThreeIdx := len(circuits) - 3
	for _, circuit := range circuits[lastThreeIdx:] {
		result *= circuit.length()
	}

	return result
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
