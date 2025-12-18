package day12

import (
	"fmt"
)

const DayName string = "Day12"
const Title string = "Christmas Tree Farm"

func solvePart1(data []string) int {
	return -42
}

func solvePart2(data []string) int {
	return -42
}

// func processInput(data []string) map[string]Device {
// 	// ccc: ddd eee fff
// 	devices := map[string]Device{}

// 	for _, line := range data {
// 		name, outStr, _ := strings.Cut(line, ":")
// 		outputs := strings.Split(strings.TrimSpace(outStr), " ")
// 		devices[name] = Device{name, outputs}
// 	}

// 	return devices
// }

func Exec(part string, data []string) (int, error) {
	var result int = 0
	var err error = nil

	if part == "PART1" {
		result = solvePart1(data)
	} else if part == "PART2" {
		result = solvePart2(data)
	} else {
		err = fmt.Errorf("%s - Unknown Part: [%s]\n", DayName, part)
	}

	if result == -42 {
		err = fmt.Errorf("%s - %s Not Implemented\n", DayName, part)
	}

	return result, err
}
