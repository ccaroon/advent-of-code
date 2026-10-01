//go:build mage

package main

import (
	"fmt"
	"os"

	"github.com/magefile/mage/sh"
)

// So that the output of the commands will go to STDOUT
var _ = os.Setenv("MAGEFILE_VERBOSE", "true")

var ginkgo = sh.RunCmd("ginkgo")

func Run(day int, part int, example *bool) error {
	// fmt.Printf("Running %s Part #%d\n", day, part)

	focusFmt := "Day%02d.Part%d."
	if example != nil {
		focusFmt += "Example"
	} else {
		focusFmt += "Solve"
	}
	focus := fmt.Sprintf(focusFmt, day, part)

	dayName := fmt.Sprintf("day%02d", day)

	return ginkgo("run", "--v", "--focus", focus, dayName)
}
