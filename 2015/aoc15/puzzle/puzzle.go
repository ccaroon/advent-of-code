package puzzle

type Puzzle struct {
	Title  string
	Day    int
	Part   int
	Input  []string
	Answer int
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
