package main

import (
	"fmt"
	"os"
	"strconv"

	"aoc15/day01"
	"aoc15/day02"
	"aoc15/day03"
	"aoc15/day04"
	"aoc15/day05"
	"aoc15/day06"
	"aoc15/day07"
	"aoc15/day08"
	"aoc15/day09"
	"aoc15/day10"
	"aoc15/day11"
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

		var pzzle any
		switch dayNum {
		case 1:
			day := day01.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle[int](*day)
		case 2:
			day := day02.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle[int](*day)
		case 3:
			day := day03.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle[int](*day)
		case 4:
			day := day04.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle[int](*day)
		case 5:
			day := day05.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle[int](*day)
		case 6:
			day := day06.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle[int](*day)
		case 7:
			day := day07.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle[int](*day)
		case 8:
			day := day08.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle[int](*day)
		case 9:
			day := day09.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle[int](*day)
		case 10:
			day := day10.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle[int](*day)
		case 11:
			day := day11.New(partNum, input)
			err = puzzle.Solve(day)
			pzzle = puzzle.Puzzle[string](*day)
		default:
			err = fmt.Errorf("Unknown/Unimplemented Day [%d]\n", dayNum)
		}

		if err != nil {
			fmt.Printf("Error: %s\n", err)
		} else {
			fmt.Println("+------------------------------------------------+")
			fmt.Println("|         *** Advent of Code - 2015 ***          |")
			fmt.Printf("|                    Day #%02d                     |\n", dayNum)
			fmt.Println("+------------------------------------------------+")

			switch v := pzzle.(type) {
			case puzzle.Puzzle[int]:
				pz := puzzle.Puzzle[int](v)
				pz.Print()
			case puzzle.Puzzle[string]:
				pz := puzzle.Puzzle[string](v)
				pz.Print()
			default:
				fmt.Printf("Unknown Puzzle Type [%T]\n", v)
			}
		}
	}
}
