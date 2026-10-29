package day10_test

import (
	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"

	"aoc15/day10"
)

var _ = Describe("MonsterSeq", func() {
	It("Can Split", func() {
		// Test 1
		seq := day10.NewMonsterSequence("1113122113")
		seq.Split()

		Expect(seq.IsSplit()).To(BeTrue())
		Expect(seq.Left.Value).To(Equal("1113122"))
		Expect(seq.Right.Value).To(Equal("113"))

		// Test 2
		seq = day10.NewMonsterSequence("1113213211")
		seq.Split()

		Expect(seq.IsSplit()).To(BeTrue())
		Expect(seq.Left.Value).To(Equal("11132"))
		Expect(seq.Right.Value).To(Equal("13211"))

		// Test 3
		seq = day10.NewMonsterSequence("11131221133112132113212221")
		seq.Split()

		Expect(seq.IsSplit()).To(BeTrue())
		Expect(seq.Left.Value).To(Equal("1113122"))
		Expect(seq.Right.Value).To(Equal("1133112132113212221"))
	})
})
