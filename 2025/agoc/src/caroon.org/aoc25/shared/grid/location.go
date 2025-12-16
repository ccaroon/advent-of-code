package grid

type Location struct {
	Row int
	Col int
}

func (loc *Location) Nearby(direction Direction) Location {
	return Location{
		Row: loc.Row + direction.RowOffset,
		Col: loc.Col + direction.ColOffset}
}

func (loc *Location) Move(direction Direction) {
	loc.Row += direction.RowOffset
	loc.Col += direction.ColOffset
}
