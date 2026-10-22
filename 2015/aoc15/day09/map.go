package day09

import (
	"regexp"
	"slices"
	"strconv"
)

type Map struct {
	locations []*Location
}

func NewMap() *Map {
	return &Map{}
}

var distDescRe = regexp.MustCompile(`(\w+)\s+to\s+(\w+)\s+=\s+(\d+)`)

// Given a distance description in the format "Tristram to Norrath = 111",
// update the Map with the locations mentioned and the links between them.
func (mp *Map) update(input string) {
	// parse input line
	matches := distDescRe.FindStringSubmatch(input)
	loc1Name := matches[1]
	loc2Name := matches[2]
	distance, err := strconv.Atoi(matches[3])

	if err != nil {
		panic(err)
	}

	// Create/Find Location #1
	loc1 := mp.findLocation(loc1Name)
	if loc1 == nil {
		loc1 = NewLocation(loc1Name)
		mp.locations = append(mp.locations, loc1)
	}

	// Create/Find Location #2
	loc2 := mp.findLocation(loc2Name)
	if loc2 == nil {
		loc2 = NewLocation(loc2Name)
		mp.locations = append(mp.locations, loc2)
	}

	// Create/Add Destination to Src Location
	loc1.addDestination(loc2, distance)
	loc2.addDestination(loc1, distance)
}

func (mp *Map) findLocation(name string) *Location {
	var foundLoc *Location
	idx := slices.IndexFunc(mp.locations, func(loc *Location) bool {
		return loc.Name == name
	})

	if idx != -1 {
		foundLoc = mp.locations[idx]
	}

	return foundLoc
}

// Start at each locations and find a route the visits all other locations
func (mp *Map) findRoutes() {

}

//
