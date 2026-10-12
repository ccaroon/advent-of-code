package day07_test

import (
	"aoc15/day07"
	"aoc15/utils"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

type EV struct {
	id       string
	expected uint16
}

var _ = Describe("Day07", func() {

	DescribeTable("Part1", func(inputFile string, expectedValues []EV) {
		input := utils.ReadInputFile(inputFile)
		day := day07.New(1, input)
		err := day.SolvePart1()

		Expect(err).To(BeNil())
		// Expect(day.Answer).To(Equal(expectedValue))

		for _, eValue := range expectedValues {
			Expect(day07.FindWire(eValue.id).Signal).To(Equal(eValue.expected))
		}
	},
		// Don't care about day.Answer | expectedValue
		Entry(nil,
			"data/part1/example1.data",
			[]EV{
				EV{"d", 72},
				EV{"e", 507},
				EV{"f", 492},
				EV{"g", 114},
				EV{"h", 65412},
				EV{"i", 65079},
				EV{"x", 123},
				EV{"y", 456},
			},
		),

		Entry(nil,
			"data/part1/example2.data",
			[]EV{
				EV{"a", 456},
				EV{"b", 456},
				EV{"x", 123},
				EV{"y", 456},
			},
		),

		Entry(nil,
			"data/part1/example3.data",
			[]EV{
				EV{"a", 123},
				EV{"b", 456},
				EV{"c", 72},
				EV{"d", 507},
				EV{"e", 30},
				EV{"f", 1824},
				EV{"g", 65412},
				EV{"h", 65079},
				EV{"z", 123},
				EV{"zz", 456},
			},
		),
	)

	DescribeTable("Part2", func(inputFile string, expectedValue int) {
		input := utils.ReadInputFile(inputFile)
		day := day07.New(2, input)
		err := day.SolvePart2()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part2/example1.data", 0),
	)
})
