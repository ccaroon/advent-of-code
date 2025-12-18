package day01

import (
	"fmt"
	"strconv"
)

const Title string = "Secret Entrance"
const dialPositions int = 100

func rotateDial(data []string) map[string]int {
	dialPos := 50
	zeroStats := map[string]int{
		"duringRotation": 0,
		"endOfRotation":  0,
	}

	for _, rotCode := range data {
		code := rotCode[0]                    // "L" or "R"
		count, _ := strconv.Atoi(rotCode[1:]) // 0 ... INF

		// # => How many times around & back to same number
		// # => I.e. How many times it passes 0
		timesPastZero := int(count / dialPositions)

		// # => How many actual clicks/positions the dial moves
		clicks := count % dialPositions

		if code == 'L' {
			newPos := dialPos - clicks
			if newPos < 0 {
				newPos = newPos + dialPositions
				if dialPos != 0 && newPos != 0 {
					timesPastZero += 1
				}
			}

			dialPos = newPos
		} else if code == 'R' {
			newPos := dialPos + clicks
			if newPos >= dialPositions {
				newPos = newPos - dialPositions
				if dialPos != 0 && newPos != 0 {
					timesPastZero += 1
				}
			}

			dialPos = newPos
		} else {
			err := fmt.Sprintf("Invalid Rotation Code [%s]", rotCode)
			panic(err)
		}

		zeroStats["duringRotation"] += timesPastZero
		if dialPos == 0 {
			zeroStats["endOfRotation"] += 1
		}
	}

	return zeroStats
}

func solvePart1(data []string) int {
	stats := rotateDial(data)

	return stats["endOfRotation"]
}

func solvePart2(data []string) int {
	stats := rotateDial(data)

	return stats["duringRotation"] + stats["endOfRotation"]
}

func Exec(part string, data []string) (int, error) {
	var result int = 0
	var err error = nil

	if part == "PART1" {
		result = solvePart1(data)
	} else if part == "PART2" {
		result = solvePart2(data)
	} else {
		err = fmt.Errorf("Day01 - Unknown Part: [%s]\n", part)
	}

	return result, err
}
