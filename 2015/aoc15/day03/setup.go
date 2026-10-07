package day03

import "aoc15/puzzle"

type Day03 puzzle.Puzzle

const (
	title  = "Perfectly Spherical Houses in a Vacuum"
	dayNum = 3
)

func New(part int, input []string) *Day03 {
	return &Day03{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day03) GetPart() int {
	return day.Part
}
