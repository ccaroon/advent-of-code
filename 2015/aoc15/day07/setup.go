package day07

import "aoc15/puzzle"

type Day07 puzzle.Puzzle

const (
	title  = "Some Assembly Required"
	dayNum = 7
)

func New(part int, input []string) *Day07 {
	return &Day07{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day07) GetPart() int {
	return day.Part
}
