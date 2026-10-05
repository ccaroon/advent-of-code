//go:build mage

package main

import (
	"fmt"
	"os"

	"github.com/magefile/mage/mg"
	"github.com/magefile/mage/sh"
)

// So that the output of the commands will go to STDOUT
var _ = os.Setenv("MAGEFILE_VERBOSE", "true")

var aoc = sh.RunCmd("./aoc15")
var g0 = sh.RunCmd("go")
var ginkgo = sh.RunCmd("ginkgo")

func Test(day int, part *int) error {
	focusFmt := "Day%02d"
	focus := fmt.Sprintf(focusFmt, day)
	if part != nil {
		focusFmt += ".Part%d"
		focus = fmt.Sprintf(focusFmt, day, *part)
	}

	dayName := fmt.Sprintf("day%02d", day)

	return ginkgo("run", "--v", "--focus", focus, dayName)
}

func Build() error {
	return g0("build", ".")
}

func Run(day int, part int) error {
	mg.Deps(Build)
	dayArg := fmt.Sprintf("%d", day)
	partArg := fmt.Sprintf("%d", part)
	inputArg := fmt.Sprintf("day%02d/data/input.data", day)
	return aoc(dayArg, partArg, inputArg)
}
