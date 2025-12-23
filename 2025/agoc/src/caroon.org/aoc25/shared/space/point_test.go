package space_test

import (
	"testing"

	"caroon.org/aoc25/shared/space"
)

func TestDistanceto(t *testing.T) {
	var pointA space.Point = space.Point{1, 2, 3}
	var pointB space.Point = space.Point{4, 5, 6}
	var expected float64 = 5.196152422706632

	result := pointA.DistanceTo(pointB)
	if result != expected {
		t.Errorf("%f != %f", result, expected)
	}
}
