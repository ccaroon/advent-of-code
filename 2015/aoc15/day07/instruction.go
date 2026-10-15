package day07

import (
	"fmt"
	"regexp"
)

const (
	AND = iota
	OR
	NOT
	LSHIFT
	RSHIFT
	ASSIGN
)

type Instruction struct {
	op     uint8
	input1 *Wire
	input2 *Wire
	output *Wire
}

var (
	assignPtrn = regexp.MustCompile(`(\d+|\w+) -> (\w+)`)
	notPtrn    = regexp.MustCompile(`NOT (\w+) -> (\w+)`)
	binaryPtrn = regexp.MustCompile(`(\d+|\w+) (AND|OR|RSHIFT|LSHIFT) (\d+|\w+) -> (\w+)`)
)

func (inst *Instruction) Exec() error {
	var err error

	switch inst.op {
	case AND:
		inst.output.AND(inst.input1, inst.input2)
	case OR:
		inst.output.OR(inst.input1, inst.input2)
	case NOT:
		inst.output.NOT(inst.input1)
	case LSHIFT:
		inst.output.LSHIFT(inst.input1, inst.input2)
	case RSHIFT:
		inst.output.RSHIFT(inst.input1, inst.input2)
	case ASSIGN:
		inst.output.ASSIGN(inst.input1)
	default:
		err = fmt.Errorf("Invalid Operation [%d]", inst.op)
	}

	return err
}

func (inst *Instruction) String() string {
	var output string

	switch inst.op {
	case AND:
		output = fmt.Sprintf("%s AND %s -> %s", inst.input1.Id(), inst.input2.Id(), inst.output.Id())
	case OR:
		output = fmt.Sprintf("%s OR %s -> %s", inst.input1.Id(), inst.input2.Id(), inst.output.Id())
	case NOT:
		output = fmt.Sprintf("NOT %s -> %s", inst.input1.Id(), inst.output.Id())
	case LSHIFT:
		output = fmt.Sprintf("%s LSHIFT %d -> %s", inst.input1.Id(), inst.input2.Signal, inst.output.Id())
	case RSHIFT:
		output = fmt.Sprintf("%s RSHIFT %d -> %s", inst.input1.Id(), inst.input2.Signal, inst.output.Id())
	case ASSIGN:
		output = fmt.Sprintf("%s -> %s", inst.input1.Id(), inst.output.Id())
	}

	return output
}
