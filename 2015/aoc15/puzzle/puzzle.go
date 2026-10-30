package puzzle

import "fmt"

type AnswerType interface {
	int | string
}

type Puzzle[AT AnswerType] struct {
	Title  string
	Day    int
	Part   int
	Input  []string
	Answer AT
}

type Solver interface {
	GetPart() int
	SolvePart1() error
	SolvePart2() error
}

func Solve(solver Solver) error {
	var err error

	if solver.GetPart() == 1 {
		err = solver.SolvePart1()
	} else if solver.GetPart() == 2 {
		err = solver.SolvePart2()
	}

	return err
}

func (pz *Puzzle[AT]) Print() {
	fmt.Printf("| %s - Part #%d\n", pz.Title, pz.Part)
	fmt.Printf("| Answer: [%v]\n", pz.Answer)
	fmt.Println("+------------------------------------------------+")
}

// +------------------------------------------------+
// |         *** Advent of Code - 2015 ***          |
// |          Day #10: Elves Look, Elves Say        |
// |                     Part #1                    |
// +------------------------------------------------+
// | Answer: [.......]
// +------------------------------------------------+
