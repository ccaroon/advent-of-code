package day05

import (
	"bytes"
	"strings"
)

var vowels []byte = []byte{'a', 'e', 'i', 'o', 'u'}
var naughtyLtrs []string = []string{"ab", "cd", "pq", "xy"}

func countVowels(input string) int {
	var count int

	for _, ltr := range input {
		if bytes.ContainsRune(vowels, ltr) {
			count += 1
		}
	}

	return count
}

func hasDoubleLtr(input string) bool {
	var hasDouble bool

	numLtrs := len(input)
	for i := range numLtrs - 1 {
		if input[i] == input[i+1] {
			hasDouble = true
			break
		}
	}

	return hasDouble
}

func hasNaughtyLtrs(input string) bool {
	var naughty bool

	for _, ltrPair := range naughtyLtrs {
		if strings.Contains(input, ltrPair) {
			naughty = true
			break
		}
	}

	return naughty
}

func (day *Day05) SolvePart1() error {
	var niceCount int

	for _, input := range day.Input {
		hasNaughtyLtr := hasNaughtyLtrs(input)
		numVowels := countVowels(input)
		hasDouble := hasDoubleLtr(input)

		if numVowels >= 3 && hasDouble && !hasNaughtyLtr {
			niceCount += 1
		}
	}

	day.Answer = niceCount

	return nil
}

// -----------------------------------------------------------------------------

// any two letters that appears at least twice in the string without overlapping
func hasTwoPair(input string) bool {
	var hasTwoPair bool

	numLtrs := len(input)
	for i := range numLtrs - 1 {
		ltrPair := input[i : i+2]
		count := strings.Count(input, ltrPair)
		if count >= 2 {
			hasTwoPair = true
			break
		}
	}

	return hasTwoPair
}

func hasXYXPtrn(input string) bool {
	var hasPtrn bool

	numLtrs := len(input)
	for i := range numLtrs - 2 {
		if input[i] == input[i+2] {
			hasPtrn = true
			break
		}
	}

	return hasPtrn
}

func (day *Day05) SolvePart2() error {
	var niceCount int

	for _, input := range day.Input {
		if hasTwoPair(input) && hasXYXPtrn(input) {
			niceCount += 1
		}
	}

	day.Answer = niceCount

	return nil
}
