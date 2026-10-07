package day04

import (
	"crypto/md5"
	"fmt"
	"strings"
)

func findAdventCoin(secretKey string, prefix string, valueCap int) (int, error) {
	var found bool = false
	var foundValue int
	var err error

	for i := range valueCap {
		input := fmt.Sprintf("%s%d", secretKey, i)
		sum := md5.Sum([]byte(input))
		hexSum := fmt.Sprintf("%x", sum)

		if strings.HasPrefix(hexSum, prefix) {
			foundValue = i
			found = true
			break
		}
	}

	if !found {
		err = fmt.Errorf("Unable to find AdventCoin in range 0-%d", valueCap)
	}

	return foundValue, err
}

func (day *Day04) SolvePart1() error {
	var secretKey string = day.Input[0]

	value, err := findAdventCoin(secretKey, "00000", 9_999_999)

	if err == nil {
		day.Answer = value
	}

	return err
}

func (day *Day04) SolvePart2() error {
	var secretKey string = day.Input[0]

	value, err := findAdventCoin(secretKey, "000000", 9_999_999)

	if err == nil {
		day.Answer = value
	}

	return err
}
