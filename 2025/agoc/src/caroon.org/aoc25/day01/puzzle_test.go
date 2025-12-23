package day01_test

import (
	"testing"

	"caroon.org/aoc25/day01"
)

func TestSolvePart1(t *testing.T) {
	var answers = []struct {
		part1, part2 int
	}{
		{1092, 6616},
	}

	// testname := fmt.Sprintf("")
	// t.Run(testname, func(t *testing.T) {
	// 	ans := IntMin(tt.a, tt.b)
	// 	if ans != tt.want {
	// 		t.Errorf("got %d, want %d", ans, tt.want)
	// 	}
	// })

	data := []string{"R1", "L2"}
	result1, err := day01.Exec("PART1", data)

	if err != nil {
		t.Errorf("Exec Error: %v", err)
	}

	if result1 != answers[0].part1 {
		t.Errorf("Wrong!")
	}
}
