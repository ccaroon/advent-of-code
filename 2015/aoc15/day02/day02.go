package day02

import (
	"aoc15/puzzle"
	"slices"
	"strconv"
	"strings"
)

type Day02 puzzle.Puzzle

func New(part int, input []string) *Day02 {
	return &Day02{
		Title: "I Was Told There Would Be No Math",
		Day:   2,
		Part:  part,
		Input: input,
	}
}

func area(l, w int) int {
	return l * w
}

func surfaceArea(l, w, h int) int {
	return 2*l*w + 2*w*h + 2*h*l
}

func volume(l, w, h int) int {
	return l * w * h
}

func parseSize(size string) []int {
	parts := strings.SplitN(size, "x", 3)
	l, _ := strconv.Atoi(parts[0])
	w, _ := strconv.Atoi(parts[1])
	h, _ := strconv.Atoi(parts[2])

	dims := []int{l, w, h}
	slices.Sort(dims)

	return dims
}

func (day *Day02) solvePart1() error {
	for _, size := range day.Input {
		dims := parseSize(size)

		smallSideArea := area(dims[0], dims[1])
		surfaceArea := surfaceArea(dims[0], dims[1], dims[2])

		day.Answer += surfaceArea + smallSideArea
	}

	return nil
}

func (day *Day02) solvePart2() error {
	for _, size := range day.Input {
		dims := parseSize(size)

		distance := dims[0]*2 + dims[1]*2
		volume := volume(dims[0], dims[1], dims[2])

		day.Answer += distance + volume
	}

	return nil
}

func Solve(part int, input []string) (*puzzle.Puzzle, error) {
	var err error

	day := New(part, input)

	if day.Part == 1 {
		err = day.solvePart1()
	} else if day.Part == 2 {
		err = day.solvePart2()
	}

	puzzle := puzzle.Puzzle(*day)

	return &puzzle, err
}
