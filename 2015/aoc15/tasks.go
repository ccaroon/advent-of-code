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

// Run unit tests for all Days
func TestAll() error {
	return ginkgo("./...")
}

// Run unit test by Day & Part
func Test(day int, part int) error {
	focusFmt := "Day%02d"
	focus := fmt.Sprintf(focusFmt, day)
	if part != 0 {
		focusFmt += ".Part%d"
		focus = fmt.Sprintf(focusFmt, day, part)
	}

	dayName := fmt.Sprintf("day%02d", day)

	return ginkgo("run", "--v", "--focus", focus, dayName)
}

// Compile the aoc15 executable
func Build() error {
	return g0("build", ".")
}

// Execute the Solution for a Day's Puzzle by Part
func Run(day int, part int) error {
	mg.Deps(Build)
	dayArg := fmt.Sprintf("%d", day)
	partArg := fmt.Sprintf("%d", part)
	inputArg := fmt.Sprintf("day%02d/data/input.data", day)
	return aoc(dayArg, partArg, inputArg)
}

// Runs Code Coverage &
// Generates: ./coverage.html
func Coverage() error {
	// Ginkgo coverage
	gArgs := []string{
		"-cover",
		"./...",
	}
	err := ginkgo(gArgs...)
	if err != nil {
		return err
	}

	// Generate report
	gtArgs := []string{
		"tool",
		"cover",
		"-html",
		"coverprofile.out",
		"-o",
		"coverage.html",
	}
	return g0(gtArgs...)
}
