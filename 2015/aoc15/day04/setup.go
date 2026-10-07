package day04

import "aoc15/puzzle"

type Day04 puzzle.Puzzle

const (
	title  = "The Ideal Stocking Stuffer"
	dayNum = 4
)

func New(part int, input []string) *Day04 {
	return &Day04{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day04) GetPart() int {
	return day.Part
}
