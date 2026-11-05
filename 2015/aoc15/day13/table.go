package day13

const (
	Left = iota
	Right
)

type Seat struct {
	occupant  *Person
	left      *Person
	right     *Person
	happiness int
}

type Table struct {
	seats []*Seat
}

func (seat *Seat) computeHappiness() int {
	var totalHappy int

	return totalHappy
}

// Seat a person at the table in the first open seat
func (table *Table) Seat(person *Person) {

}

// Seat a person at the Table next to a specific other person
func (table *Table) SeatNextTo(person *Person, other *Person, position int) {
	seat := table.findPerson(other)

	// TODO: this will potentially UNSEAT someone else
	// ...must keep track of that
	switch position {
	case Left:
		seat.left = person
	case Right:
		seat.right = person
	default:
		panic("Position MUST be Left | Right")
	}
}

// Returns the numeric position of a person at the table
func (table *Table) findPerson(person *Person) *Seat {
	var foundSeat *Seat

	for _, seat := range table.seats {
		if seat.occupant.name == person.name {
			foundSeat = seat
			break
		}
	}

	return foundSeat
}
