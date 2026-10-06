package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	"aoc15/day01"
	"aoc15/day02"
	"aoc15/day03"
	"aoc15/puzzle"
	"aoc15/utils"
)

func main() {
	if len(os.Args) < 4 {
		fmt.Printf("Usage: %s <day-num> <part-num> <input-file>\n", os.Args[0])
		os.Exit(1)
	} else {
		var err error = nil

		dayNum, err := strconv.Atoi(os.Args[1])
		if err != nil {
			panic("Invalid Day Number: Requires integer (1|2|3...)")
		}

		partNum, err := strconv.Atoi(os.Args[2])
		if err != nil {
			panic("Invalid Part Number: Requires integer (1|2|3...)")
		}

		inputFileName := os.Args[3]
		input := utils.ReadInputFile(inputFileName)

		var pzzle puzzle.Puzzle
		switch dayNum {
		case 1:
			day := day01.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle(*day)
		case 2:
			day := day02.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle(*day)
		case 3:
			day := day03.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle(*day)
		default:
			err = fmt.Errorf("Unknown/Unimplemented Day [%d]\n", dayNum)
		}

		if err != nil {
			fmt.Printf("Error: %s\n", err)
		} else {
			var testIndicator string
			if strings.Index(inputFileName, "test-") == 0 {
				testIndicator = "(TEST)"
			}

			fmt.Println("+------------------------------------------------+")
			fmt.Println("|         *** Advent of Code - 2015 ***          |")
			fmt.Println("+------------------------------------------------+")
			fmt.Printf("| Day #%d / <%s> / Part #%d\n", pzzle.Day, pzzle.Title, pzzle.Part)
			fmt.Printf("| Answer: [%d] %s\n", pzzle.Answer, testIndicator)
			fmt.Println("+------------------------------------------------+")
		}
	}
}
