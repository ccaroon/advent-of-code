package day08

import (
	"fmt"
	"regexp"
	"strings"
)

func countCodeChars(input string) int {
	// fmt.Printf("=> cdeChr: [%s] -> [%d]\n", input, len(input))
	return len(input)
}

// The only escape sequences used are
// * \\ (single backslash),
// * \" (lone double-quote character),
// * \x plus two hexadecimal characters (single character with that ASCII code).
func countMemChars(input string) int {
	// Get rid of starting & ending double-quote
	memLine := strings.TrimPrefix(input, `"`)
	memLine = strings.TrimSuffix(memLine, `"`)

	// Backslash
	bsRe := regexp.MustCompile(`\\\\`)
	// Double-quote
	dqRe := regexp.MustCompile(`\\"`)
	// ASCII hex value
	hxRe := regexp.MustCompile(`\\x[0-9a-f][0-9a-f]`)

	// fmt.Printf("=> [%s]\n", memLine)

	memLine = bsRe.ReplaceAllString(memLine, `-`)
	// fmt.Printf("  -> [%s]\n", memLine)

	memLine = dqRe.ReplaceAllString(memLine, `"`)
	// fmt.Printf("  -> [%s]\n", memLine)

	// Just replace it with a `.` instead of the actual char it represents
	// ...byte(0x27) -> actual char
	memLine = hxRe.ReplaceAllString(memLine, `-`)
	// fmt.Printf("  -> [%s]\n", memLine)

	// fmt.Printf("=> MemChr: [%s] -> [%s] = [%d]\n", input, memLine, len(memLine))

	return len(memLine)
}

func (day *Day08) SolvePart1() error {
	var codeChars int
	var memChars int

	for _, input := range day.Input {
		codeChars += countCodeChars(input)
		memChars += countMemChars(input)
	}

	day.Answer = codeChars - memChars

	return nil
}

func (day *Day08) SolvePart2() error {
	return fmt.Errorf("Day #08 - Part 2 - Not implemented!")
}
