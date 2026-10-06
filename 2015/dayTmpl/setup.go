package day0X

import "aoc15/puzzle"

type Day0X puzzle.Puzzle

const (
	title  = "<PUZZLE TITLE GOES HERE>"
	dayNum = 0X
)

func New(part int, input []string) *Day0X {
	return &Day0X{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day0X) GetPart() int {
	return day.Part
}
