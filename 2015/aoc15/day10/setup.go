package day10

import "aoc15/puzzle"

type Day10 puzzle.Puzzle[int]

const (
	title  = "Elves Look, Elves Say"
	dayNum = 10
)

func New(part int, input []string) *Day10 {
	return &Day10{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day10) GetPart() int {
	return day.Part
}
