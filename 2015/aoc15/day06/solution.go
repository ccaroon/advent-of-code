package day06

import "fmt"

func (day *Day06) SolvePart1() error {
	lightGrid := NewLightGrid(1000, 1000)

	for _, input := range day.Input {
		instr := ParseInstruction(input)

		switch instr.Operation {
		case TurnOff:
			lightGrid.Off(instr.TopLeft, instr.BtmRight)
		case TurnOn:
			lightGrid.On(instr.TopLeft, instr.BtmRight)
		case Toggle:
			lightGrid.ToggleRange(instr.TopLeft, instr.BtmRight)
		}
	}

	day.Answer = lightGrid.CountOn()

	return nil
}

func (day *Day06) SolvePart2() error {
	return fmt.Errorf("Day #06 - Part 2 - Not implemented!")
}
