package day01_test

import (
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestDay01(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Day01 Suite")
}
