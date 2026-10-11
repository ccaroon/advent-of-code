package day06

func (day *Day06) SolvePart1() error {
	lightGrid := NewLightGrid[int8](1000, 1000)

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

// 15706847 -- too high
func (day *Day06) SolvePart2() error {
	lightGrid := NewLightGrid[int16](1000, 1000)

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

	day.Answer = lightGrid.GetBrightness()

	return nil
}
