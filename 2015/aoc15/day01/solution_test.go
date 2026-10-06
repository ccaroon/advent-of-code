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
		day := day01.New(1, input)
		err := day.SolvePart1()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(3))
	})

	It("Part2", func() {
		input := utils.ReadInputFile("data/p2-ex1.data")
		day := day01.New(2, input)
		err := day.SolvePart2()

		Expect(err).To(BeNil())
		Expect(day.Answer).To(Equal(5))
	})
})
