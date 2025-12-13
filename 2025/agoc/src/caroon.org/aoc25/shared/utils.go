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
		if line[0] != '#' {
			data = append(data, file.Text())
		}
	}

	return data
}
