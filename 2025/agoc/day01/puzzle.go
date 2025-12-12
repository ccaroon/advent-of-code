package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const DIAL_POSITIONS int = 100

func read_input_file(filename string) []string {
	var data []string

	fptr, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer fptr.Close()

	file := bufio.NewScanner(fptr)
	for file.Scan() {
		data = append(data, file.Text())
	}

	return data
}

func rotate(data []string) map[string]int {
	dial_pos := 50
	zero_stats := map[string]int{
		"during_rotation": 0,
		"end_of_rotation": 0,
	}

	for _, rot_code := range data {
		code := rot_code[0]                    // "L" or "R"
		count, _ := strconv.Atoi(rot_code[1:]) // 0 ... INF

		// # => How many times around & back to same number
		// # => I.e. How many times it passes 0
		times_past_zero := int(count / DIAL_POSITIONS)

		// # => How many actual clicks/positions the dial moves
		clicks := count % DIAL_POSITIONS

		if code == 'L' {
			new_pos := dial_pos - clicks
			if new_pos < 0 {
				new_pos = new_pos + DIAL_POSITIONS
				if dial_pos != 0 && new_pos != 0 {
					times_past_zero += 1
				}
			}

			dial_pos = new_pos
		} else if code == 'R' {
			new_pos := dial_pos + clicks
			if new_pos >= DIAL_POSITIONS {
				new_pos = new_pos - DIAL_POSITIONS
				if dial_pos != 0 && new_pos != 0 {
					times_past_zero += 1
				}
			}

			dial_pos = new_pos
		} else {
			err := fmt.Sprintf("Invalid Rotation Code [%s]", rot_code)
			panic(err)
		}

		zero_stats["during_rotation"] += times_past_zero
		if dial_pos == 0 {
			zero_stats["end_of_rotation"] += 1
		}
	}

	return zero_stats
}

func solve_part1(data []string) int {
	stats := rotate(data)

	return stats["end_of_rotation"]
}

func solve_part2(data []string) int {
	stats := rotate(data)

	return stats["during_rotation"] + stats["end_of_rotation"]
}

func main() {
	if len(os.Args) < 3 {
		fmt.Printf("Usage: %s <part1|part2> <input-file>\n", os.Args[0])
		os.Exit(1)
	} else {
		part := os.Args[1]
		data := read_input_file(os.Args[2])

		count := 0
		if part == "part1" {
			count = solve_part1(data)
		} else if part == "part2" {
			count = solve_part2(data)
		}

		fmt.Printf("Day 01 // %s -> [%d]\n", part, count)
	}

}
