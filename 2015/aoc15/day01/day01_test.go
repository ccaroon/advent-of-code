package day01_test

import (
	"aoc15/day01"
	"aoc15/utils"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Day01", func() {

	It("Part1", func() {
		input := utils.ReadInputFile("data/p1-ex1.data")
		puzzle, err := day01.Solve(1, input)

		Expect(err).To(BeNil())
		Expect(puzzle.Answer).To(Equal(3))
	})

	It("Part2", func() {
		input := utils.ReadInputFile("data/p2-ex1.data")
		puzzle, err := day01.Solve(2, input)

		Expect(err).To(BeNil())
		Expect(puzzle.Answer).To(Equal(5))
	})
})
