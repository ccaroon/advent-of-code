package day02

import "aoc15/puzzle"

type Day02 puzzle.Puzzle

const (
	title  = "I Was Told There Would Be No Math"
	dayNum = 2
)

func New(part int, input []string) *Day02 {
	return &Day02{
		Title: title,
		Day:   dayNum,
		Part:  part,
		Input: input,
	}
}

func (day *Day02) GetPart() int {
	return day.Part
}
