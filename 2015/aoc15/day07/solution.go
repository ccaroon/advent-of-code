package day07

// Declared here so that it can be use in unit tests
var MainCircuit Circuit

func (day *Day07) SolvePart1() error {
	MainCircuit = NewCircuit()

	for _, input := range day.Input {
		err := MainCircuit.Build(input)
		if err != nil {
			return err
		}
	}

	aWire := MainCircuit.FindWire("a")
	aWire.Resolve()
	day.Answer = int(aWire.Signal)

	return nil
}

func (day *Day07) SolvePart2() error {
	MainCircuit = NewCircuit()

	// Build the Circuit Normally
	for _, input := range day.Input {
		err := MainCircuit.Build(input)
		if err != nil {
			return err
		}
	}

	// Resolve 'a' Signal
	aWire := MainCircuit.FindWire("a")
	aWire.Resolve()

	// Reset the circuit to allow each wire to be resolved again
	MainCircuit.Reset()

	// Set b's Signal to a's Signal
	bWire := MainCircuit.FindWire("b")
	bWire.Signal = aWire.Signal
	// Mark bWire as resolved so that it does not get re-calculated
	// i.e. it's being resolved **here** by setting it's Signal to a's
	// Signal value
	bWire.resolved = true

	aWire.Resolve()
	day.Answer = int(aWire.Signal)

	return nil
}
