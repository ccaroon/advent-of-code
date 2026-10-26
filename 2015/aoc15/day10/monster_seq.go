package day10

import "fmt"

type MonsterSequence struct {
	value      string
	iterations int
}

func NewMonsterSequence(initialValue string) *MonsterSequence {
	return &MonsterSequence{
		value:      initialValue,
		iterations: 0,
	}
}

// Compute the next value in the sequence
func (seq *MonsterSequence) Next() {
	var currDigit byte = seq.value[0]
	var count int = 1
	var newValue string

	for idx := 1; idx < len(seq.value); idx++ {
		digit := seq.value[idx]
		if digit != currDigit {
			// "Save" off the current run
			// fmt.Printf("ISaving run %d of %c\n", count, currDigit)
			newValue += fmt.Sprintf("%d%c", count, currDigit)

			// Start a new run
			currDigit = digit
			count = 1
		} else {
			count += 1
		}
	}

	// fmt.Printf("OSaving run %d of %c\n", count, currDigit)
	newValue += fmt.Sprintf("%d%c", count, currDigit)

	seq.value = newValue
	seq.iterations += 1
}

func (seq *MonsterSequence) Print() {
	fmt.Printf("%s [%d]\n", seq.value, seq.iterations)
}
