package grid

import (
	"math"
)

func ComputeArea(loc1 Location, loc2 Location) float64 {
	rows := math.Abs(float64(loc1.Row-loc2.Row)) + 1
	cols := math.Abs(float64(loc1.Col-loc2.Col)) + 1

	return rows * cols
}
