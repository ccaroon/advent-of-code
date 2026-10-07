package day03

import "fmt"

type SantaEntity struct {
	location   Location
	houseCount int
	visited    map[Location]bool
}

func newSanta(startLoc Location) *SantaEntity {
	return &SantaEntity{
		location:   startLoc,
		houseCount: 0,
		visited:    make(map[Location]bool),
	}
}

func (s *SantaEntity) deliverPresent() {
	if _, exists := s.visited[s.location]; !exists {
		s.houseCount += 1
		s.visited[s.location] = true
	}
}

func (s *SantaEntity) move(direction rune) {
	switch direction {
	case '^':
		s.location.y += 1
	case '>':
		s.location.x += 1
	case 'v':
		s.location.y -= 1
	case '<':
		s.location.x -= 1
	default:
		fmt.Printf("Invalid Input [%c]\n", direction)
	}
}
