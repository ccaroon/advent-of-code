package day12_test

import (
	"aoc15/day12"
	"aoc15/utils"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Day12", func() {

	DescribeTable("Part1", func(inputFile string, expectedValue int) {
		input := utils.ReadInputFile(inputFile)
		day := day12.New(1, input)
		err := day.SolvePart1()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part1/example1.data", 6),
		Entry(nil, "data/part1/example2.data", 6),
		Entry(nil, "data/part1/example3.data", 3),
		Entry(nil, "data/part1/example4.data", 3),
		Entry(nil, "data/part1/example5.data", 0),
		Entry(nil, "data/part1/example6.data", 0),
		Entry(nil, "data/part1/example7.data", 0),
		Entry(nil, "data/part1/example8.data", 0),
	)

	DescribeTable("Part2", func(inputFile string, expectedValue int) {
		input := utils.ReadInputFile(inputFile)
		day := day12.New(2, input)
		err := day.SolvePart2()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part2/example1.data", 6),
		Entry(nil, "data/part2/example2.data", 4),
		Entry(nil, "data/part2/example3.data", 0),
		Entry(nil, "data/part2/example4.data", 6),
	)
})
