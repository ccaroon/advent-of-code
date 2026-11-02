package day12

import "aoc15/puzzle"

type Day12 puzzle.Puzzle[int]

const (
	title  = "JSAbacusFramework.io"
	dayNum = 12
)

func New(part int, input []string) *Day12 {
	return &Day12{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day12) GetPart() int {
	return day.Part
}
