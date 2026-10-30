package day11

import (
	"fmt"
	"regexp"
	"slices"
)

const (
	asciiOffset = 96
	defaultLen  = 8
)

var (
	validateRe = regexp.MustCompile("[a-z]{8}")
)

type Password struct {
	data [defaultLen]uint8
}

func NewPassword(value string) *Password {
	passwd := Password{}

	// Convert letter (byte) to a number from 1 to 26 (a to z)
	// assumes ltr is a lowercase letter
	for idx, ltr := range value[0:defaultLen] {
		passwd.data[idx] = byte(ltr) - asciiOffset
	}

	return &passwd
}

func (passwd *Password) String() string {
	return passwd.Value()
}

func (passwd *Password) Value() string {
	var value string

	value = fmt.Sprintf(
		"%c%c%c%c%c%c%c%c",
		passwd.data[0]+asciiOffset,
		passwd.data[1]+asciiOffset,
		passwd.data[2]+asciiOffset,
		passwd.data[3]+asciiOffset,
		passwd.data[4]+asciiOffset,
		passwd.data[5]+asciiOffset,
		passwd.data[6]+asciiOffset,
		passwd.data[7]+asciiOffset,
	)

	return value
}

func (passwd *Password) Data() [8]uint8 {
	return passwd.data
}

func (passwd *Password) IsValid() bool {
	var valid bool

	// Must be 8 lowercase letters
	valid = validateRe.MatchString(passwd.Value())
	// fmt.Printf("reTest [%v]\n", valid)

	// Must contain one at-least 3 letter straight
	straightCount := 0
	for idx := 0; idx < len(passwd.data)-2; idx++ {
		ltrNum := passwd.data[idx]
		if passwd.data[idx+1] == ltrNum+1 && passwd.data[idx+2] == ltrNum+2 {
			straightCount += 1
		}
	}
	valid = valid && straightCount == 1

	// Must not contain i, o, l
	valid = valid && !slices.Contains(passwd.data[:], byte('i')-asciiOffset)
	// fmt.Printf("iTest [%v]\n", valid)
	valid = valid && !slices.Contains(passwd.data[:], byte('o')-asciiOffset)
	valid = valid && !slices.Contains(passwd.data[:], byte('l')-asciiOffset)

	// Must contain at least 2 unique, non-overlapping letter pairs
	pairCount := 0
	var pairValue uint8
	for idx := 0; idx < len(passwd.data)-1; idx++ {
		ltrNum := passwd.data[idx]
		if pairValue != ltrNum && passwd.data[idx+1] == ltrNum {
			pairValue = ltrNum
			pairCount += 1
			idx++
		}
	}
	valid = valid && pairCount >= 2

	return valid
}

// Advance the password to the next value
// Value **may not** necessarily be valid
// See: Rotate()
func (passwd *Password) Next() {
	for idx := defaultLen - 1; idx >= 0; idx-- {
		passwd.data[idx] += 1
		if passwd.data[idx] > 26 {
			passwd.data[idx] = 1
		} else {
			break
		}
	}
}

// Rotate the current password to the next Valid value
func (passwd *Password) Rotate() {
	passwd.Next()

	for !passwd.IsValid() {
		passwd.Next()
	}
}
