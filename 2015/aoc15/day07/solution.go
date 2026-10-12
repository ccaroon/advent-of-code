package day07

import "fmt"

func (day *Day07) SolvePart1() error {
	for _, input := range day.Input {
		inst, err := parseInstruction(input)
		if err != nil {
			return err
		}

		err = inst.Exec()
		if err != nil {
			return err
		}
	}

	aWire := FindWire("a")
	day.Answer = int(aWire.Signal)

	return nil
}

func (day *Day07) SolvePart2() error {
	return fmt.Errorf("Day #07 - Part 2 - Not implemented!")
}
