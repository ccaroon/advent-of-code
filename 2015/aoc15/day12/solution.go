package day12

import "fmt"

func (day *Day12) SolvePart1() error {
	data, err := ParseJSON(day.Input[0])
	if err != nil {
		return err
	}

	day.Answer = FindTotal(data)

	return nil
}

func (day *Day12) SolvePart2() error {
	return fmt.Errorf("Day #12 - Part 2 - Not implemented!")
}
