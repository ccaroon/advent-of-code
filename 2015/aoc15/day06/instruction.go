package day06

import (
	"regexp"
	"strconv"
)

const (
	TurnOn = iota
	TurnOff
	Toggle
)

type Instruction struct {
	Operation int
	TopLeft   Coord
	BtmRight  Coord
}

// turn on 226,196 through 599,390
// turn off 660,55 through 986,197
// toggle 537,781 through 687,941
func ParseInstruction(input string) Instruction {
	var inst Instruction
	re := regexp.MustCompile(`(turn\s+on|turn\s+off|toggle)\s+(\d+)\s*,\s*(\d+)\s+through\s+(\d+)\s*,\s*(\d+)`)

	matches := re.FindStringSubmatch(input)

	switch matches[1] {
	case "turn on":
		inst.Operation = TurnOn
	case "turn off":
		inst.Operation = TurnOff
	case "toggle":
		inst.Operation = Toggle
	}

	x, _ := strconv.Atoi(matches[2])
	y, _ := strconv.Atoi(matches[3])
	inst.TopLeft = Coord{
		X: x,
		Y: y,
	}

	x, _ = strconv.Atoi(matches[4])
	y, _ = strconv.Atoi(matches[5])
	inst.BtmRight = Coord{
		X: x,
		Y: y,
	}

	return inst
}
