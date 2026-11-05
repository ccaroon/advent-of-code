package day13

import "aoc15/puzzle"

type Day13 puzzle.Puzzle[int]

const (
	title  = "Knights of the Dinner Table"
	dayNum = 13
)

func New(part int, input []string) *Day13 {
	return &Day13{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day13) GetPart() int {
	return day.Part
}
