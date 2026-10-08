package day05

import "aoc15/puzzle"

type Day05 puzzle.Puzzle

const (
	title  = "Doesn't He Have Intern-Elves For This?"
	dayNum = 5
)

func New(part int, input []string) *Day05 {
	return &Day05{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day05) GetPart() int {
	return day.Part
}
