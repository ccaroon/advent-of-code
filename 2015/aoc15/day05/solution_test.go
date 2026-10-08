package day05_test

import (
	"aoc15/day05"
	"aoc15/utils"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Day05", func() {

	DescribeTable("Part1", func(inputFile string, expectedValue int) {
		input := utils.ReadInputFile(inputFile)
		day := day05.New(1, input)
		err := day.SolvePart1()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part1/example1.data", 2),
	)

	DescribeTable("Part2", func(inputFile string, expectedValue int) {
		input := utils.ReadInputFile(inputFile)
		day := day05.New(2, input)
		err := day.SolvePart2()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part2/example1.data", 2),
	)
})
