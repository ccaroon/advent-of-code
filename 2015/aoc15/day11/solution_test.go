package day11_test

import (
	"aoc15/day11"
	"aoc15/utils"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Day11", func() {

	DescribeTable("Part1", func(inputFile string, expectedValue string) {
		input := utils.ReadInputFile(inputFile)
		day := day11.New(1, input)
		err := day.SolvePart1()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part1/example1.data", "abcdffaa"),
		Entry(nil, "data/part1/example2.data", "ghjaabcc"),
	)

	DescribeTable("Part2", func(inputFile string, expectedValue string) {
		input := utils.ReadInputFile(inputFile)
		day := day11.New(2, input)
		err := day.SolvePart2()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part2/example1.data", "abcdffbb"),
		Entry(nil, "data/part2/example2.data", "ghjbbcdd"),
	)
})
