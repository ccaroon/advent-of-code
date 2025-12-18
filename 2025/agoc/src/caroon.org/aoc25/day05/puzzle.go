package day05

import (
	"fmt"
	"strconv"
	"strings"
)

const Title string = "Cafeteria"

type IngredientIdRange struct {
	start int
	end   int
}

func checkFreshness(iid int, idRange IngredientIdRange) bool {
	var isFresh bool = false

	if iid >= idRange.start && iid <= idRange.end {
		isFresh = true
	}

	return isFresh
}

func solvePart1(iids []int, idRanges []IngredientIdRange) int {
	var freshCount int = 0

	for _, iid := range iids {
		for _, idRng := range idRanges {
			if checkFreshness(iid, idRng) {
				freshCount += 1
				break
			}
		}

	}

	return freshCount
}

func solvePart2(iids []int, idRanges []IngredientIdRange) int {
	return 0
}

func processInput(data []string) ([]int, []IngredientIdRange) {
	var idRanges []IngredientIdRange
	var ids []int

	for _, line := range data {
		if strings.Contains(line, "-") {
			endPoints := strings.SplitN(line, "-", 2)

			start, _ := strconv.Atoi(endPoints[0])
			end, _ := strconv.Atoi(endPoints[1])

			idRanges = append(idRanges, IngredientIdRange{start, end})
		} else {
			iid, _ := strconv.Atoi(line)
			ids = append(ids, iid)
		}
	}

	return ids, idRanges
}

func Exec(part string, data []string) (int, error) {
	var result int = 0
	var err error = nil
	var iids []int
	var idRanges []IngredientIdRange

	iids, idRanges = processInput(data)

	if part == "PART1" {
		result = solvePart1(iids, idRanges)
	} else if part == "PART2" {
		result = solvePart2(iids, idRanges)
	} else {
		err = fmt.Errorf("Day05 - Unknown Part: [%s]\n", part)
	}

	return result, err
}
