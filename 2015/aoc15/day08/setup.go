package day08

import "aoc15/puzzle"

type Day08 puzzle.Puzzle[int]

const (
	title  = "Matchsticks"
	dayNum = 8
)

func New(part int, input []string) *Day08 {
	return &Day08{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day08) GetPart() int {
	return day.Part
}
