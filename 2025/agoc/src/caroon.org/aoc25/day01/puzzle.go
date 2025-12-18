package day01

import (
	"fmt"
	"strconv"
)

const Title string = "Secret Entrance"
const dialPositions int = 100

func rotateDial(data []string) map[string]int {
	dial_pos := 50
	zero_stats := map[string]int{
		"duringRotation": 0,
		"endOfRotation":  0,
	}

	for _, rot_code := range data {
		code := rot_code[0]                    // "L" or "R"
		count, _ := strconv.Atoi(rot_code[1:]) // 0 ... INF

		// # => How many times around & back to same number
		// # => I.e. How many times it passes 0
		times_past_zero := int(count / dialPositions)

		// # => How many actual clicks/positions the dial moves
		clicks := count % dialPositions

		if code == 'L' {
			new_pos := dial_pos - clicks
			if new_pos < 0 {
				new_pos = new_pos + dialPositions
				if dial_pos != 0 && new_pos != 0 {
					times_past_zero += 1
				}
			}

			dial_pos = new_pos
		} else if code == 'R' {
			new_pos := dial_pos + clicks
			if new_pos >= dialPositions {
				new_pos = new_pos - dialPositions
				if dial_pos != 0 && new_pos != 0 {
					times_past_zero += 1
				}
			}

			dial_pos = new_pos
		} else {
			err := fmt.Sprintf("Invalid Rotation Code [%s]", rot_code)
			panic(err)
		}

		zero_stats["duringRotation"] += times_past_zero
		if dial_pos == 0 {
			zero_stats["endOfRotation"] += 1
		}
	}

	return zero_stats
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
