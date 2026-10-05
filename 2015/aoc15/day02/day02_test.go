package day02_test

import (
	"aoc15/day02"
	"aoc15/utils"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Day02", func() {

	DescribeTable("Part1", func(inputFile string, expectedValue int) {
		input := utils.ReadInputFile(inputFile)
		puzzle, err := day02.Solve(1, input)

		Expect(err).To(BeNil())
		Expect(puzzle.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part1/example1.data", 58),
		Entry(nil, "data/part1/example2.data", 43),
		Entry(nil, "data/part1/example3.data", 101),
	)

	DescribeTable("Part2", func(inputFile string, expectedValue int) {
		input := utils.ReadInputFile(inputFile)
		puzzle, err := day02.Solve(2, input)

		Expect(err).To(BeNil())
		Expect(puzzle.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part1/example1.data", 34),
		Entry(nil, "data/part1/example2.data", 14),
		Entry(nil, "data/part1/example3.data", 48),
	)
})
