package main

import (
	"fmt"
	"os"
	"strings"

	"caroon.org/aoc25/day01"
	"caroon.org/aoc25/day02"
	"caroon.org/aoc25/day03"
	"caroon.org/aoc25/day04"
	"caroon.org/aoc25/day05"
	"caroon.org/aoc25/day06"
	"caroon.org/aoc25/shared"
)

func main() {
	if len(os.Args) < 4 {
		fmt.Printf("Usage: %s <dayN> <part1|part2> <input-file>\n", os.Args[0])
		os.Exit(1)
	} else {
		var result int
		var err error = nil
		const baseInputFilePath string = "../../../../aoc"
		// var icons = []string{"☃️", "❄️", "🎅🏼", "🧊", "🎄", "🎁", "🍬", "🌟", "✡️"}

		dayNum := strings.ToUpper(os.Args[1])
		partNum := strings.ToUpper(os.Args[2])
		inputFilePath := fmt.Sprintf("%s/%s/%s", baseInputFilePath, strings.ToLower(dayNum), os.Args[3])
		data := shared.ReadInputFile(inputFilePath)

		switch dayNum {
		case "DAY01":
			result, err = day01.Exec(partNum, data)
		case "DAY02":
			result, err = day02.Exec(partNum, data)
		case "DAY03":
			result, err = day03.Exec(partNum, data)
		case "DAY04":
			result, err = day04.Exec(partNum, data)
		case "DAY05":
			result, err = day05.Exec(partNum, data)
		case "DAY06":
			result, err = day06.Exec(partNum, data)
		default:
			err = fmt.Errorf("Unknown Day [%s]\n", dayNum)
		}

		if err != nil {
			fmt.Printf("Error: %s", err)
		} else {
			// iconIdx := rand.Int() % len(icons)
			fmt.Println("❄️❄️❄️  Advent of Code - 2025 ❄️❄️❄️")
			fmt.Printf("=> %s // %s -> [%d]\n", dayNum, partNum, result)
		}

	}

}
