package day02

import (
	"fmt"
	"regexp"
	"slices"
	"strconv"
	"strings"
)

func solvePart1(data []string) int {
	var invalidIds []int
	var sum int

	for _, idRange := range data {
		parts := strings.SplitN(idRange, "-", 2)
		sid, _ := strconv.Atoi(parts[0])
		eid, _ := strconv.Atoi(parts[1])

		for pid := sid; pid <= eid; pid++ {
			idStr := fmt.Sprintf("%d", pid)
			idLen := len(idStr)
			middle := int(idLen / 2)

			// To Be INvalid...
			// ...must have even length
			// ...first half and last half must match
			if idLen%2 == 0 {
				firstHalf := idStr[0:middle]
				lastHalf := idStr[middle:]

				if firstHalf == lastHalf {
					invalidIds = append(invalidIds, pid)
				}
			}
		}
	}

	// Sum all the invalid Product IDs
	for _, iid := range invalidIds {
		sum += iid
	}

	return sum
}

func solvePart2(data []string) int {
	var invalidIds []int
	var sum int = 0

	for _, idRange := range data {
		parts := strings.SplitN(idRange, "-", 2)
		sid, _ := strconv.Atoi(parts[0])
		eid, _ := strconv.Atoi(parts[1])

		for pid := sid; pid <= eid; pid++ {
			idStr := fmt.Sprintf("%d", pid)
			idLen := len(idStr)

			// # Starting with the first N digits as a pattern (N=1)...
			// # ...#1 - does the pattern exist 2 or more times in the id_str?
			// # ...YES?
			// # ......stop -> INVALID
			// # ...NO?
			// # ......N++
			// # ......create a new pattern composed of the first N digits
			// # ......GOTO #1
			// # Example: id_str = "123123"
			// # pattern = "1"
			// # "^(1){2,}$" ~= "123123" -> Nope
			// # pattern = "12"
			// # "^(12){2,}$" ~= "123123" -> Nope
			// # pattern = "123"
			// # "^(123){2,}$" ~= "123123" -> Yup. Invalid! Stop!

			for idx := range idLen {
				// Must match against whole string
				pattern := fmt.Sprintf("^(%s){2,}$", idStr[0:idx+1])
				re := regexp.MustCompile(pattern)

				// If pattern/regex matches (two or more times)
				// then it's invalid
				if re.MatchString(idStr) {
					invalidIds = append(invalidIds, pid)
					break
				}
				// 		self._debug(f"  -> MATCH: {id_str} =~ /{regex}/")
				// 		invalid_ids.append(pid)
				// 		break
			}
		}
	}

	// Sum all the invalid Product IDs
	for _, iid := range invalidIds {
		sum += iid
	}

	return sum
}

func processData(data []string) []string {
	var productIdRanges []string

	for _, line := range data {
		tmpRanges := strings.Split(line, ",")
		productIdRanges = slices.Concat(productIdRanges, tmpRanges)
	}

	return productIdRanges
}

func Exec(part string, data []string) (int, error) {
	var result int = 0
	var err error = nil

	prdIdRanges := processData(data)
	if part == "PART1" {
		result = solvePart1(prdIdRanges)
	} else if part == "PART2" {
		result = solvePart2(prdIdRanges)
	} else {
		err = fmt.Errorf("Day02 - Unknown Part: [%s]\n", part)
	}

	return result, err
}
