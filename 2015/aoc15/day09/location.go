package day09

import (
	"fmt"
)

type Location struct {
	Name         string
	Destinations []Destination
}

type Destination struct {
	Loc      *Location
	Distance int
}

// A path between multiple locations and the total distance from the
// starting Location to the ending Location
// A -> B -> C == 42
type Route struct {
	locations     []*Location
	totalDistance int
}

func NewLocation(name string) *Location {
	return &Location{
		Name: name,
	}
}

func (loc *Location) addDestination(dstLoc *Location, distance int) {
	dest := Destination{
		Loc:      dstLoc,
		Distance: distance,
	}

	loc.Destinations = append(loc.Destinations, dest)
}

// Find all the routes from this Location that visits every other location
// and the total distance between them.
func (loc *Location) findRoutes() []*Route {
	var routes []*Route

	// for _, dest := range loc.Destinations {
	// 	route := Route{}
	// 	route.locations = append(route.locations, loc)

	// }

	return routes
}

func (loc *Location) Print() {
	fmt.Println(loc.Name)
	for _, dest := range loc.Destinations {
		fmt.Printf("  -> %s %d miles\n", dest.Loc.Name, dest.Distance)
	}
}
