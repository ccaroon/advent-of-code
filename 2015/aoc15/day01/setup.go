package day01

import "aoc15/puzzle"

type Day01 puzzle.Puzzle

const (
	title  = "Not Quite LISP"
	dayNum = 01
)

func New(part int, input []string) *Day01 {
	return &Day01{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day01) GetPart() int {
	return day.Part
}
