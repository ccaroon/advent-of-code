package day07

import "fmt"

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
	return fmt.Errorf("Day #07 - Part 2 - Not implemented!")
}
