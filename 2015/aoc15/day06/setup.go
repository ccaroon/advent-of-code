package day06

import "aoc15/puzzle"

type Day06 puzzle.Puzzle

const (
	title  = "Probably a Fire Hazard"
	dayNum = 6
)

func New(part int, input []string) *Day06 {
	return &Day06{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day06) GetPart() int {
	return day.Part
}
