package day10

import (
	"fmt"
	"strings"
)

type MonsterSequence struct {
	Value      string
	iterations int
	Left       *MonsterSequence
	Right      *MonsterSequence
}

func NewMonsterSequence(initialValue string) *MonsterSequence {
	return &MonsterSequence{
		Value:      initialValue,
		iterations: 0,
	}
}

// Compute the next Value in the sequence
func (seq *MonsterSequence) Next() {
	var currDigit byte = seq.Value[0]
	var count int = 1
	var newValue string

	// TODO: I apparently don't fully understand the "splitting" property
	//          ...as such this does not work
	// See: https://mathworld.wolfram.com/CosmologicalTheorem.html
	// if len(seq.Value) >= 10 && !seq.IsSplit() {
	// 	// fmt.Printf("Splitting %s...\n", seq.Value)
	// 	seq.Split()
	// 	fmt.Printf("%s [%d] -> Left[%s] | Right[%s]\n", seq.Value, seq.iterations, seq.Left.Value, seq.Right.Value)
	// }

	if seq.IsSplit() {
		seq.Left.Next()
		seq.Right.Next()

		newValue = fmt.Sprintf("%s%s", seq.Left.Value, seq.Right.Value)
	} else {
		for idx := 1; idx < len(seq.Value); idx++ {
			digit := seq.Value[idx]
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
	}

	seq.Value = newValue
	seq.iterations += 1
}

func (seq *MonsterSequence) Split() {
	var splitIdx int

	// Look for first `2` that is followed by a `1` or `3`
	sIdx := strings.Index(seq.Value, "2")
	for idx := sIdx + 1; idx < len(seq.Value)-1; idx++ {
		if seq.Value[idx] == '1' || seq.Value[idx] == '3' {
			splitIdx = idx
			break
		}
	}

	// split the Value at the `2`
	// create seq.Left & seq.Right
	seq.Left = NewMonsterSequence(seq.Value[0:splitIdx])
	seq.Right = NewMonsterSequence(seq.Value[splitIdx:])
}

func (seq *MonsterSequence) FastFwd(iterations int) {
	for idx := 0; idx < iterations; idx++ {
		seq.Next()
	}
}

func (seq *MonsterSequence) IsSplit() bool {
	return seq.Left != nil && seq.Right != nil
}

func (seq *MonsterSequence) Print() {
	// fmt.Println("--- MonsterSequence ---")
	fmt.Printf("%s i[%d] l[%d]\n", seq.Value, seq.iterations, len(seq.Value))

	if seq.IsSplit() {
		fmt.Println("--- Left ---")
		seq.Left.Print()
		fmt.Println("--- Right ---")
		seq.Right.Print()
	}
}
