package day11

func (day *Day11) SolvePart1() error {
	passwd := NewPassword(day.Input[0])

	passwd.Rotate()

	day.Answer = passwd.Value()

	return nil
}

func (day *Day11) SolvePart2() error {
	passwd := NewPassword(day.Input[0])

	// Rotate twice to get the next two valid passwords
	passwd.Rotate()
	passwd.Rotate()

	day.Answer = passwd.Value()

	return nil
}
