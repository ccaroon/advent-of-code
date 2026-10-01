package day01_test

import (
	"aoc15/day01"
	"aoc15/shared"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

var _ = Describe("Day01", func() {
	Context("Part1", func() {
		It("Example", func() {
			answer := day01.Part1("data/p1-example.data")
			Expect(answer).To(Equal(3))
		})

		It("Solve", func() {
			answer := day01.Part1("data/input.data")
			shared.PrintAnswer(answer)
		})
	})

	Context("Part2", func() {
		It("Example", func() {
			answer := day01.Part2("data/p2-example.data")
			Expect(answer).To(Equal(5))
		})

		It("Solve", func() {
			answer := day01.Part2("data/input.data")
			shared.PrintAnswer(answer)
		})
	})

})
