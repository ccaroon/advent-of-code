package shared

import (
	"bufio"
	"fmt"
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

func PrintAnswer(answer int) {
	aSpec := `
----------------------------------------------------
Answer: %d
----------------------------------------------------
			`
	fmt.Printf(aSpec, answer)
}
