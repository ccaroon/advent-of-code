package day03

import "fmt"

type Location struct {
	x int
	y int
}

func (day *Day03) SolvePart1() error {
	var houseCount int = 1
	var currLoc Location = Location{0, 0}
	var newLoc Location
	var locations map[Location]int = make(map[Location]int)

	// Count starting position as having been visited.
	locations[currLoc] = 1

	for _, direction := range day.Input[0] {
		switch direction {
		case '^':
			newLoc = Location{
				currLoc.x, currLoc.y + 1,
			}
		case '>':
			newLoc = Location{
				currLoc.x + 1, currLoc.y,
			}
		case 'v':
			newLoc = Location{
				currLoc.x, currLoc.y - 1,
			}
		case '<':
			newLoc = Location{
				currLoc.x - 1, currLoc.y,
			}
		default:
			fmt.Printf("Invalid Input [%c]\n", direction)
		}

		if _, exists := locations[newLoc]; !exists {
			houseCount += 1
		}
		locations[newLoc] += 1
		currLoc = newLoc
	}

	day.Answer = houseCount

	return nil
}

func (day *Day03) SolvePart2() error {
	return fmt.Errorf("Day #03 - Part 2 - Not implemented!")
}
