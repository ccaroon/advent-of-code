package day08

import (
	"cmp"
	"fmt"
	"slices"
	"sort"
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
type byDist []JBoxPair

func (lst byDist) Len() int           { return len(lst) }
func (lst byDist) Less(i, j int) bool { return lst[i].dist < lst[j].dist }
func (lst byDist) Swap(i, j int)      { lst[i], lst[j] = lst[j], lst[i] }

func solvePart1(boxPos []space.Point) int {
	var pointList itertools.List
	var jBoxPairs []JBoxPair
	var circuits []*Circuit

	// build List of Points for itertools
	for _, point := range boxPos {
		pointList = append(pointList, point)
	}
	combos := itertools.CombinationsList(pointList, 2)

	for pair := range combos {
		jBox1 := pair[0].(space.Point)
		jBox2 := pair[1].(space.Point)
		dist := jBox1.DistanceTo(jBox2)

		jBoxPairs = append(jBoxPairs, JBoxPair{jBox1, jBox2, dist})
	}

	sort.Sort(byDist(jBoxPairs))
	// fmt.Printf(" ==> JBoxPair Count [%d] <==\n", len(jBoxPairs))
	// for idx, pair := range jBoxPairs[:10] {
	// 	fmt.Printf("%d) %v\n", idx, pair)
	// }

	cId := 0
	for _, jBoxPair := range jBoxPairs[:1000] {
		// fmt.Printf("-> JBoxPair #%d %v | Circuits [%d]\n", idx, jBoxPair, len(circuits))

		addNewCircuit := true
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
				// do nothing
				// fmt.Printf("->  NoOp - jBox1 & jBox2 already connected to Circuit #%d\n", circuit.id)
				addNewCircuit = false
				// fmt.Printf("->  %v\n", circuit)
			}
			// if jBox1 is part of C1 and jBox2 is part of C2
			// then ... join the two circuits?
			// -> JBoxPair #9 {{906 360 560} {984 92 344} 352.936254867646}
			// ->  Adding jBox2 to Circuit #1
			// ->  &{1 [{906 360 560} {805 96 715} {739 650 466} {984 92 344}]}
			// ->  Adding jBox1 to Circuit #2
			// ->  &{2 [{862 61 35} {984 92 344} {906 360 560}]}
			//
			// Pair: {906 360 560} {984 92 344}
			// &{1 [{906 360 560} {805 96 715} {739 650 466}]}
			// &{2 [{862 61 35} {984 92 344}]}
		}

		// if len(modCircuits) > 1 {
		// 	fmt.Printf("ModCircuits [%d]\n", len(modCircuits))
		// }
		// fmt.Printf("ModCount [%d]\n", len(modCircuits))
		// for _, ct := range modCircuits {
		// 	fmt.Printf("%d - %v\n", ct.id, ct.junctionBoxes)
		// }
		// ...GOOD...
		// if len(modCircuits) > 1 {
		// 	modCircuits[0].merge(modCircuits[1])
		// 	circuits = slices.Delete(circuits, modCircuits[1].id, modCircuits[1].id+1)
		// }
		if len(modCircuits) > 1 {
			baseCircuit := circuits[modCircuits[0]]
			for _, cIdx := range modCircuits[1:] {
				baseCircuit.merge(circuits[cIdx])
			}

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

	// find the 3 largest circuits
	// var idxLen [][]int
	// for idx, circuit := range circuits {
	// 	idxLen = append(idxLen, []int{idx, circuit.length()})
	// }

	// lenCmp := func(a, b []int) int {
	// 	return cmp.Compare(a[1], b[1])
	// }
	// slices.SortFunc(idxLen, lenCmp)

	lenCmp := func(a, b *Circuit) int {
		return cmp.Compare(a.length(), b.length())
	}
	slices.SortFunc(circuits, lenCmp)

	// for _, circuit := range circuits {
	// 	fmt.Printf("%d) len [%d]\n", circuit.id, circuit.length())
	// }

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
