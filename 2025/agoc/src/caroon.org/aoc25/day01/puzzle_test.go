package day01_test

import (
	"fmt"
	"os"
	"testing"

	"github.com/BurntSushi/toml"
)

type answerPart struct {
	Answer  int
	Example int
}

type answers struct {
	Days map[string]answerDay
}

type answerDay struct {
	Part1 answerPart
	Part2 answerPart
}

// type simple struct {
// 	Name string
// 	Addr string
// }

// testname := fmt.Sprintf("")
// t.Run(testname, func(t *testing.T) {
// 	ans := IntMin(tt.a, tt.b)
// 	if ans != tt.want {
// 		t.Errorf("got %d, want %d", ans, tt.want)
// 	}
// })

func checkAnswer(t *testing.T, answer int, result int, err error) {
	if err != nil {
		t.Errorf("Exec Error: %v", err)
	}

	if result != answer {
		t.Errorf("Wrong!")
	}
}

func TestSolvePart1(t *testing.T) {
	// var answers = []struct {
	// 	part1, part2 int
	// }{
	// 	{1092, 6616},
	// }

	var answers answers
	var aFile string = "../../../../../tests/answers.toml"
	_, err := toml.DecodeFile(aFile, &answers)
	if err != nil {
		fmt.Printf("TOML Error: %v\n", err)
		os.Exit(1)
	}

	// for i, k := range meta.Keys() {
	// 	fmt.Printf("%d) %s\n", i, k)
	// }

	fmt.Printf("%v\n", answers.Days["day01"].Part1.Answer)
	os.Exit(1)

	// var stuff simple
	// var aFile string = "../../../../../tests/answers.toml"
	// _, err := toml.DecodeFile(aFile, &stuff)
	// if err != nil {
	// 	fmt.Printf("TOML Error: %v\n", err)
	// 	os.Exit(1)
	// }

	// fmt.Println(stuff.Name)
	// os.Exit(1)
	// fmt.Println(answers.Days["day01"])
	// data := utils.ReadInputFile("../../../../../input/day01-input.txt")

	// Part 1
	// result, err := day01.Exec("PART1", data)
	// checkAnswer(t, answers[0].part1, result, err)

	// Part 2
	// result, err = day01.Exec("PART2", data)
	// checkAnswer(t, answers[0].part2, result, err)
}
