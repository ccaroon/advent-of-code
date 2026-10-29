package day10

import (
	"fmt"
	"strconv"
	"strings"
)

// https://www.youtube.com/watch?v=ea7lJkEhytA

func manualTest() {
	var value string
	var iters int

	fmt.Print("Enter <VALUE> <ITERATIONS>: ")
	fmt.Scanf("%s %d\n", &value, &iters)
	fmt.Printf("[%s] [%d]\n", value, iters)

	seq := NewMonsterSequence(value)
	seq.FastFwd(iters)

	seq.Print()
}

func (day *Day10) SolvePart1() error {

	// UNCOMMENT to create and run a specific sequence
	// manualTest()

	initValue, numIterations := parseInput(day.Input[0])
	if numIterations < 0 {
		numIterations = 40
	}

	seq := NewMonsterSequence(initValue)
	seq.FastFwd(numIterations)
	day.Answer = len(seq.Value)

	return nil
}

func (day *Day10) SolvePart2() error {
	initValue, numIterations := parseInput(day.Input[0])
	if numIterations < 0 {
		numIterations = 50
	}

	seq := NewMonsterSequence(initValue)
	seq.FastFwd(numIterations)
	day.Answer = len(seq.Value)

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
