package day03_test

import (
	"aoc15/day03"
	"aoc15/utils"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Day03", func() {

	DescribeTable("Part1", func(inputFile string, expectedValue int) {
		input := utils.ReadInputFile(inputFile)
		day := day03.New(1, input)
		err := day.SolvePart1()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part1/example1.data", 2),
		Entry(nil, "data/part1/example2.data", 4),
		Entry(nil, "data/part1/example3.data", 2),
	)

	DescribeTable("Part2", func(inputFile string, expectedValue int) {
		input := utils.ReadInputFile(inputFile)
		day := day03.New(2, input)
		err := day.SolvePart2()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part2/example1.data", 00),
	)
})
