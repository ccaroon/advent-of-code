package utils_test

import (
	"fmt"
	"testing"

	"caroon.org/aoc25/shared/utils"
)

func TestTotalIntList(t *testing.T) {
	var numbers = []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	var expected = map[string]int{"+": 45, "*": 362880}

	for _, op := range []string{"+", "*"} {
		testName := fmt.Sprintf("With Operator (%s)", op)
		t.Run(testName, func(t *testing.T) {
			result := utils.TotalIntList(numbers, op)
			if result != expected[op] {
				t.Errorf("%d != %d", result, expected[op])
			}
		})
	}
}

func TestReadInputFile(t *testing.T) {
	var fileName string = "./utils_test.go"

	lines := utils.ReadInputFile(fileName)

	if len(lines) <= 0 {
		t.Errorf("no lines read")
	}
}
