package day10

import (
	"strconv"
	"strings"
)

func (day *Day10) SolvePart1() error {
	initValue, numIterations := parseInput(day.Input[0])
	if numIterations < 0 {
		numIterations = 40
	}

	day.Answer = solveIt(initValue, numIterations)

	return nil
}

func (day *Day10) SolvePart2() error {
	initValue, numIterations := parseInput(day.Input[0])
	if numIterations < 0 {
		numIterations = 50
	}

	day.Answer = solveIt(initValue, numIterations)

	return nil
}

func parseInput(input string) (string, int) {
	var numIterations int
	var err error

	parts := strings.SplitN(input, "*", 2)
	initValue := parts[0]

	if len(parts) > 1 {
		numIterations, err = strconv.Atoi(parts[1])
		if err != nil {
			panic(err)
		}
	} else {
		numIterations = -1
	}

	return initValue, numIterations
}

func solveIt(initValue string, iterations int) int {
	seq := NewMonsterSequence(initValue)
	for idx := 0; idx < iterations; idx++ {
		seq.Next()
	}

	return len(seq.value)
}
