package day01_test

import (
	"testing"

	"caroon.org/aoc25/day01"
	"caroon.org/aoc25/shared/utils"
)

// testname := fmt.Sprintf("")
// t.Run(testname, func(t *testing.T) {
// 	ans := IntMin(tt.a, tt.b)
// 	if ans != tt.want {
// 		t.Errorf("got %d, want %d", ans, tt.want)
// 	}
// })

func checkAnswer(t *testing.T, answer int, result int, err error) {
	if err != nil {
		t.Errorf("Exec Error: %v", err)
	}

	if result != answer {
		t.Errorf("Wrong!")
	}
}

func TestSolvePart1(t *testing.T) {
	var answers = []struct {
		part1, part2 int
	}{
		{1092, 6616},
	}

	data := utils.ReadInputFile("../../../../../input/day01-input.txt")

	// Part 1
	result, err := day01.Exec("PART1", data)
	checkAnswer(t, answers[0].part1, result, err)

	// Part 2
	result, err = day01.Exec("PART2", data)
	checkAnswer(t, answers[0].part2, result, err)
}
