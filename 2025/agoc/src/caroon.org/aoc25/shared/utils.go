package shared

import (
	"bufio"
	"os"
)

func ReadInputFile(filename string) []string {
	var data []string

	fptr, err := os.Open(filename)
	if err != nil {
		panic(err)
	}
	defer fptr.Close()

	file := bufio.NewScanner(fptr)
	for file.Scan() {
		line := file.Text()
		if line != "" && line[0] != '#' {
			data = append(data, file.Text())
		}
	}

	return data
}

func SumIntList(numList []int) int {
	var sum int = 0

	for _, number := range numList {
		sum += number
	}

	return sum
}
