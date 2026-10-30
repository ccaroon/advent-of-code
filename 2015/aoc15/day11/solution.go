package day11

import "fmt"

func (day *Day11) SolvePart1() error {
	passwd := NewPassword(day.Input[0])

	passwd.Rotate()

	day.Answer = passwd.Value()

	return nil
}

func (day *Day11) SolvePart2() error {
	return fmt.Errorf("Day #11 - Part 2 - Not implemented!")
}
