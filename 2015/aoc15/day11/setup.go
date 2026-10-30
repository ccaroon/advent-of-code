package day11

import "aoc15/puzzle"

type Day11 puzzle.Puzzle[string]

const (
	title  = "Corporate Policy"
	dayNum = 11
)

func New(part int, input []string) *Day11 {
	return &Day11{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day11) GetPart() int {
	return day.Part
}
