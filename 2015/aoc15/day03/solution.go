package day03

type Location struct {
	x int
	y int
}

func (day *Day03) SolvePart1() error {
	santa := newSanta(Location{0, 0})
	santa.deliverPresent()

	for _, direction := range day.Input[0] {
		santa.move(direction)
		santa.deliverPresent()
	}

	day.Answer = santa.houseCount

	return nil
}

func (day *Day03) SolvePart2() error {
	realSanta := newSanta(Location{0, 0})
	realSanta.deliverPresent()

	roboSanta := newSanta(Location{0, 0})
	// Both Santas need to shared the list of visited houses
	roboSanta.visited = realSanta.visited
	roboSanta.deliverPresent()

	for i, direction := range day.Input[0] {
		if i%2 == 0 {
			realSanta.move(direction)
			realSanta.deliverPresent()
		} else {
			roboSanta.move(direction)
			roboSanta.deliverPresent()
		}
	}

	day.Answer = realSanta.houseCount + roboSanta.houseCount

	return nil
}
