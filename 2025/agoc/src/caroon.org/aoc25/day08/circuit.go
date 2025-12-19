package day08

import (
	"slices"

	"caroon.org/aoc25/shared/space"
)

type Circuit struct {
	id            int
	junctionBoxes []space.Point
}

func NewCircuit(id int, jBoxes []space.Point) *Circuit {
	circuit := Circuit{id, jBoxes}

	return &circuit
}

func (ct *Circuit) addJunctionBox(newJBox space.Point) {
	ct.junctionBoxes = append(ct.junctionBoxes, newJBox)
}

func (ct *Circuit) isConnectedTo(jBox space.Point) bool {
	return slices.Contains(ct.junctionBoxes, jBox)
}

func (ct *Circuit) length() int {
	return len(ct.junctionBoxes)
}

func (ct *Circuit) merge(other *Circuit) {
	for _, jBox := range other.junctionBoxes {
		if !ct.isConnectedTo(jBox) {
			ct.addJunctionBox((jBox))
		}
	}
}
