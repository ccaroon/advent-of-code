package day06_test

import (
	"aoc15/day06"
	"aoc15/utils"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Day06", func() {

	Context("Instruction", func() {
		It("Can Parse an instruction string", func() {

			inst := day06.ParseInstruction("turn on 226,196 through 599,390")
			Expect(inst).ToNot(BeNil())
			Expect(inst.Operation).To(Equal(day06.TurnOn))
			Expect(inst.TopLeft.X).To(Equal(226))
			Expect(inst.TopLeft.Y).To(Equal(196))
			Expect(inst.BtmRight.X).To(Equal(599))
			Expect(inst.BtmRight.Y).To(Equal(390))

			inst = day06.ParseInstruction("turn off 660,55 through 986,197")
			Expect(inst).ToNot(BeNil())
			Expect(inst.Operation).To(Equal(day06.TurnOff))

			inst = day06.ParseInstruction("toggle 537,781 through 687,941")
			Expect(inst).ToNot(BeNil())
			Expect(inst.Operation).To(Equal(day06.Toggle))
		})
	})

	DescribeTable("Part1", func(inputFile string, expectedValue int) {
		input := utils.ReadInputFile(inputFile)
		day := day06.New(1, input)
		err := day.SolvePart1()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part1/example1.data", 1_000_000),
		Entry(nil, "data/part1/example2.data", 1_000),
		Entry(nil, "data/part1/example3.data", 0),
		Entry(nil, "data/part1/example4.data", 1_000_000-4),
	)

	DescribeTable("Part2", func(inputFile string, expectedValue int) {
		input := utils.ReadInputFile(inputFile)
		day := day06.New(2, input)
		err := day.SolvePart2()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(expectedValue))
	},

		Entry(nil, "data/part2/example1.data", 00),
	)
})
