package day11_test

import (
	"fmt"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"

	"aoc15/day11"
)

var _ = Describe("Password", func() {
	It("Can Create a New Password", func() {
		passwd := day11.NewPassword("craigxyz")

		Expect(passwd).ToNot(BeNil())

		data := passwd.Data()
		Expect(data[0]).To(Equal(uint8(3)))
		Expect(data[1]).To(Equal(uint8(18)))
		Expect(data[2]).To(Equal(uint8(1)))
		Expect(data[3]).To(Equal(uint8(9)))
		Expect(data[4]).To(Equal(uint8(7)))
		Expect(data[5]).To(Equal(uint8(24)))
		Expect(data[6]).To(Equal(uint8(25)))
		Expect(data[7]).To(Equal(uint8(26)))
	})

	It("Is Printable", func() {
		passwd := day11.NewPassword("craigxyz")

		Expect(passwd).ToNot(BeNil())
		Expect(passwd.Value()).To(Equal("craigxyz"))
		Expect(passwd.String()).To(Equal("craigxyz"))
		Expect(fmt.Sprintf("%s", passwd)).To(Equal("craigxyz"))
	})

	It("Can test for validity", func() {
		// Valid
		passwd := day11.NewPassword("abccaffx")
		Expect(passwd).ToNot(BeNil())
		Expect(passwd.IsValid()).To(BeTrue())

		// Not Valid: no 3-letter straight
		passwd = day11.NewPassword("ebccaffx")
		Expect(passwd).ToNot(BeNil())
		Expect(passwd.IsValid()).To(BeFalse())

		// Not Valid: More than 1  3-letter straight
		passwd = day11.NewPassword("abccxyzz")
		Expect(passwd).ToNot(BeNil())
		Expect(passwd.IsValid()).To(BeFalse())

		// Not Valid: contains `i`
		passwd = day11.NewPassword("abcciffx")
		Expect(passwd).ToNot(BeNil())
		Expect(passwd.IsValid()).To(BeFalse())

		// Not Valid: contains `o`
		passwd = day11.NewPassword("abccoffx")
		Expect(passwd).ToNot(BeNil())
		Expect(passwd.IsValid()).To(BeFalse())

		// Not Valid: contains `l`
		passwd = day11.NewPassword("abcclffx")
		Expect(passwd).ToNot(BeNil())
		Expect(passwd.IsValid()).To(BeFalse())

		// Not Valid: contains `l`
		passwd = day11.NewPassword("abcclffx")
		Expect(passwd).ToNot(BeNil())
		Expect(passwd.IsValid()).To(BeFalse())

		// Not Valid: Only 1 pair
		passwd = day11.NewPassword("abccafgx")
		Expect(passwd).ToNot(BeNil())
		Expect(passwd.IsValid()).To(BeFalse())

		// Not Valid: Pair overlaps [c[c]c]
		passwd = day11.NewPassword("acccaffx")
		Expect(passwd).ToNot(BeNil())
		Expect(passwd.IsValid()).To(BeFalse())

		// Not Valid: Pair Overlaps + pairs not unique
		passwd = day11.NewPassword("abceaaaa")
		Expect(passwd).ToNot(BeNil())
		Expect(passwd.IsValid()).To(BeFalse())
	})

	It("Can get the Next value", func() {
		passwd := day11.NewPassword("aaaaaaaa")
		passwd.Next()
		Expect(passwd.Value()).To(Equal("aaaaaaab"))

		passwd = day11.NewPassword("aaaaaaaz")
		passwd.Next()
		Expect(passwd.Value()).To(Equal("aaaaaaba"))
	})

})
