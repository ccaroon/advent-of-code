package day06

type Coord struct {
	X int
	Y int
}

const (
	ON  = 1
	OFF = 0
)

type LightType interface {
	int8 | int16
}

type LightGrid[LT LightType] struct {
	numRows int
	numCols int
	lights  []LT
}

func NewLightGrid[LT LightType](rows, cols int) *LightGrid[LT] {
	return &LightGrid[LT]{
		numRows: rows,
		numCols: cols,
		lights:  make([]LT, rows*cols),
	}
}

// func (lg *LightGrid) idxToCoord(idx int) Coord {
// 	var coord Coord

// 	coord.X = idx % lg.numCols
// 	coord.Y = (idx - coord.X) / lg.numCols

// 	return coord
// }

func (lg *LightGrid[LT]) SetRange(topLeft, btmRight Coord, value LT) {
	startX := topLeft.X
	endX := btmRight.X
	startY := topLeft.Y
	endY := btmRight.Y

	for y := startY; y <= endY; y += 1 {
		for x := startX; x <= endX; x += 1 {
			// Convert X,Y to Array index
			idx := (y * lg.numCols) + x

			switch v := any(value).(type) {
			case int8:
				lg.lights[idx] = value
			case int16:
				if value == ON {
					lg.lights[idx] += 1
				} else if value == OFF && lg.lights[idx] > 0 {
					lg.lights[idx] -= 1
				}
			default:
				panic(v)
			}

		}
	}
}

func (lg *LightGrid[LT]) ToggleRange(topLeft, btmRight Coord) {
	startX := topLeft.X
	endX := btmRight.X
	startY := topLeft.Y
	endY := btmRight.Y

	for y := startY; y <= endY; y += 1 {
		for x := startX; x <= endX; x += 1 {
			// Convert X,Y to Array index
			idx := (y * lg.numCols) + x

			switch v := any(lg.lights[0]).(type) {
			case int8:
				if lg.lights[idx] == ON {
					lg.lights[idx] = OFF
				} else {
					lg.lights[idx] = ON
				}
			case int16:
				lg.lights[idx] += 2
			default:
				panic(v)
			}

		}
	}
}

func (lg *LightGrid[LT]) On(topLeft, btmRight Coord) {
	lg.SetRange(topLeft, btmRight, ON)
}

func (lg *LightGrid[LT]) Off(topLeft, btmRight Coord) {
	lg.SetRange(topLeft, btmRight, OFF)
}

func (lg *LightGrid[LT]) CountOn() int {
	var onCount int = 0
	var numLights int = lg.numRows * lg.numCols

	for idx := 0; idx < numLights; idx += 1 {
		if lg.lights[idx] == ON {
			onCount += 1
		}
	}

	return onCount
}

func (lg *LightGrid[LT]) GetBrightness() int {
	var totalBrightness int = 0
	var numLights int = lg.numRows * lg.numCols

	for idx := 0; idx < numLights; idx += 1 {
		totalBrightness += int(lg.lights[idx])

	}

	return totalBrightness
}
