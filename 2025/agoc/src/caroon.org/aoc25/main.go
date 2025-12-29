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
	"caroon.org/aoc25/day07"
	"caroon.org/aoc25/day08"
	"caroon.org/aoc25/day09"
	"caroon.org/aoc25/day10"
	"caroon.org/aoc25/day11"
	"caroon.org/aoc25/day12"
	"caroon.org/aoc25/shared/utils"
)

func main() {
	if len(os.Args) < 4 {
		fmt.Printf("Usage: %s <dayN> <part1|part2> <input-file>\n", os.Args[0])
		os.Exit(1)
	} else {
		var result int
		var title string
		var err error = nil

		dayNum := strings.ToUpper(os.Args[1])
		partNum := strings.ToUpper(os.Args[2])
		inputFileName := os.Args[3]
		data := utils.ReadInputFile(inputFileName)

		switch dayNum {
		case "DAY01":
			title = day01.Title
			result, err = day01.Exec(partNum, data)
		case "DAY02":
			title = day02.Title
			result, err = day02.Exec(partNum, data)
		case "DAY03":
			title = day03.Title
			result, err = day03.Exec(partNum, data)
		case "DAY04":
			title = day04.Title
			result, err = day04.Exec(partNum, data)
		case "DAY05":
			title = day05.Title
			result, err = day05.Exec(partNum, data)
		case "DAY06":
			title = day06.Title
			result, err = day06.Exec(partNum, data)
		case "DAY07":
			title = day07.Title
			result, err = day07.Exec(partNum, data)
		case "DAY08":
			title = day08.Title
			result, err = day08.Exec(partNum, data)
		case "DAY09":
			title = day09.Title
			result, err = day09.Exec(partNum, data)
		case "DAY10":
			title = day10.Title
			result, err = day10.Exec(partNum, data)
		case "DAY11":
			title = day11.Title
			result, err = day11.Exec(partNum, data)
		case "DAY12":
			title = day12.Title
			result, err = day12.Exec(partNum, data)
		default:
			err = fmt.Errorf("Unknown Day [%s]\n", dayNum)
		}

		if err != nil {
			fmt.Printf("Error: %s", err)
		} else {
			var testIndicator string
			if strings.Index(inputFileName, "test-") == 0 {
				testIndicator = "(TEST)"
			}

			fmt.Println("+------------------------------------------------+")
			fmt.Println("|        *** Advent of (Go)Code - 2025 ***       |")
			fmt.Println("+------------------------------------------------+")
			fmt.Printf("| %s / <%s> / %s\n", dayNum, title, partNum)
			fmt.Printf("| Answer: [%d] %s\n", result, testIndicator)
			fmt.Println("+------------------------------------------------+")
		}
	}
}
