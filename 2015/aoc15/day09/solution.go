package day09

import "fmt"

func (day *Day09) SolvePart1() error {
	deliveryMap := NewMap()

	for _, input := range day.Input {
		deliveryMap.update(input)
	}

	for _, loc := range deliveryMap.locations {
		loc.Print()
	}

	return nil
}

func (day *Day09) SolvePart2() error {
	return fmt.Errorf("Day #09 - Part 2 - Not implemented!")
}
