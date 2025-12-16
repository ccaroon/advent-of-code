package space

import (
	"math"
)

type Point struct {
	X, Y, Z int
}

func (pt *Point) DistanceTo(other Point) float64 {
	dx := math.Pow(float64(pt.X-other.X), 2)
	dy := math.Pow(float64(pt.Y-other.Y), 2)
	dz := math.Pow(float64(pt.Z-other.Z), 2)

	return math.Sqrt(dx + dy + dz)
}
