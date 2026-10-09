package day06

type Coord struct {
	X int
	Y int
}

const (
	ON  = true
	OFF = false
)

type LightGrid struct {
	numRows int
	numCols int
	lights  []bool
}

func NewLightGrid(rows, cols int) *LightGrid {
	return &LightGrid{
		numRows: rows,
		numCols: cols,
		lights:  make([]bool, rows*cols),
	}
}

func (lg *LightGrid) idxToCoord(idx int) Coord {
	var coord Coord

	coord.X = idx % lg.numCols
	coord.Y = (idx - coord.X) / lg.numCols

	return coord
}

func (lg *LightGrid) SetRange(topLeft, btmRight Coord, value bool) {
	startX := topLeft.X
	endX := btmRight.X
	startY := topLeft.Y
	endY := btmRight.Y

	for y := startY; y <= endY; y += 1 {
		for x := startX; x <= endX; x += 1 {
			// Convert X,Y to Array index
			idx := (y * lg.numCols) + x
			lg.lights[idx] = value
		}
	}
}

func (lg *LightGrid) ToggleRange(topLeft, btmRight Coord) {
	startX := topLeft.X
	endX := btmRight.X
	startY := topLeft.Y
	endY := btmRight.Y

	for y := startY; y <= endY; y += 1 {
		for x := startX; x <= endX; x += 1 {
			// Convert X,Y to Array index
			idx := (y * lg.numCols) + x
			if lg.lights[idx] == ON {
				lg.lights[idx] = OFF
			} else {
				lg.lights[idx] = ON
			}
		}
	}
}

func (lg *LightGrid) On(topLeft, btmRight Coord) {
	lg.SetRange(topLeft, btmRight, ON)
}

func (lg *LightGrid) Off(topLeft, btmRight Coord) {
	lg.SetRange(topLeft, btmRight, OFF)
}

func (lg *LightGrid) CountOn() int {
	var onCount int = 0
	var numLights int = lg.numRows * lg.numCols

	for idx := 0; idx < numLights; idx += 1 {
		if lg.lights[idx] == ON {
			onCount += 1
		}
	}

	return onCount
}
