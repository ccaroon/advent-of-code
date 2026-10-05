package day02_test

import (
	"testing"

	. "github.com/onsi/ginkgo/v2"
	. "github.com/onsi/gomega"
)

func TestDay01(t *testing.T) {
	RegisterFailHandler(Fail)
	RunSpecs(t, "Day02 Suite")
}
