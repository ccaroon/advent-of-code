package day09

import "aoc15/puzzle"

type Day09 puzzle.Puzzle

const (
	title  = "All in a Single Night"
	dayNum = 9
)

func New(part int, input []string) *Day09 {
	return &Day09{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day09) GetPart() int {
	return day.Part
}
