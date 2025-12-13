package main

import (
	"fmt"
	"os"
	"strings"

	"caroon.org/aoc25/day01"
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
			result = 0
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
