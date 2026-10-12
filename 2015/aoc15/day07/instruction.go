package day07

import (
	"fmt"
	"regexp"
	"strconv"
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
	binaryPtrn = regexp.MustCompile(`(\w+) (AND|OR|RSHIFT|LSHIFT) (\d+|\w+) -> (\w+)`)
)

func parseInstruction(input string) (*Instruction, error) {
	var inst Instruction

	if binaryPtrn.MatchString(input) {
		// eg AND ei -> ej
		// kg OR kf -> kh
		// lf RSHIFT 2 -> lg
		// eo LSHIFT 15 -> es
		matches := binaryPtrn.FindStringSubmatch(input)

		switch matches[2] {
		case "AND":
			inst.op = AND
			inst.input2 = FindWire(matches[3])
		case "OR":
			inst.op = OR
			inst.input2 = FindWire(matches[3])
		case "RSHIFT":
			inst.op = RSHIFT
			amt, err := strconv.Atoi(matches[3])
			if err != nil {
				return nil, err
			}
			inst.input2 = &Wire{id: "__CONSTANT__", Signal: uint16(amt)}
		case "LSHIFT":
			inst.op = LSHIFT
			amt, err := strconv.Atoi(matches[3])
			if err != nil {
				return nil, err
			}
			inst.input2 = &Wire{id: "__CONSTANT__", Signal: uint16(amt)}
		default:
			return nil, fmt.Errorf("Invalid Operation [%s]", matches[2])
		}

		inst.input1 = FindWire(matches[1])
		inst.output = FindWire(matches[4])
	} else if notPtrn.MatchString(input) {
		// NOT dq -> dr
		matches := notPtrn.FindStringSubmatch(input)
		inst.op = NOT
		inst.input1 = FindWire(matches[1])
		inst.output = FindWire(matches[2])
	} else if assignPtrn.MatchString(input) {
		// 44430 -> b
		// gx -> b
		matches := assignPtrn.FindStringSubmatch(input)

		inst.op = ASSIGN

		isConstant, _ := regexp.MatchString(`^\d+$`, matches[1])
		if isConstant {
			value, err := strconv.Atoi(matches[1])
			if err != nil {
				return nil, err
			}

			inst.input1 = &Wire{id: "__CONSTANT__", Signal: uint16(value)}
		} else {
			inst.input1 = FindWire(matches[1])
		}

		inst.output = FindWire(matches[2])
	} else {
		return nil, fmt.Errorf("Invalid instruction [%s]\n", input)
	}

	return &inst, nil
}

func (inst *Instruction) Exec() error {
	var err error

	switch inst.op {
	case AND:
		inst.output.AND(inst.input1, inst.input2)
		// fmt.Printf("%s AND %s -> %s\n", inst.input1.id, inst.input2.id, inst.output.id)
	case OR:
		inst.output.OR(inst.input1, inst.input2)
		// fmt.Printf("%s OR %s -> %s\n", inst.input1.id, inst.input2.id, inst.output.id)
	case NOT:
		inst.output.NOT(inst.input1)
		// fmt.Printf("NOT %s -> %s\n", inst.input1.id, inst.output.id)
	case LSHIFT:
		inst.output.LSHIFT(inst.input1, inst.input2)
		// fmt.Printf("%s LSHIFT %d -> %s\n", inst.input1.id, inst.input2.Signal, inst.output.id)
	case RSHIFT:
		inst.output.RSHIFT(inst.input1, inst.input2)
		// fmt.Printf("%s RSHIFT %d -> %s\n", inst.input1.id, inst.input2.Signal, inst.output.id)
	case ASSIGN:
		inst.output.ASSIGN(inst.input1)
		// fmt.Printf("ASSIGN: %d -> %s\n", inst.input1.Signal, inst.output.id)
	default:
		err = fmt.Errorf("Invalid Operation [%d]", inst.op)
	}

	return err
}
