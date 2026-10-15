package day07

import "fmt"

// All the Wires in the connected circuit
type Circuit map[string]*Wire

// Circuit
func NewCircuit() Circuit {
	var circuit Circuit = make(map[string]*Wire)

	return circuit
}

func (circuit Circuit) FindWire(id string) *Wire {
	var ok bool
	var wire *Wire

	if wire, ok = circuit[id]; !ok {
		wire = NewWire(id)
		circuit[id] = wire
	}

	return wire
}

func (circuit Circuit) Build(input string) error {
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
		case "OR":
			inst.op = OR
		case "RSHIFT":
			inst.op = RSHIFT
		case "LSHIFT":
			inst.op = LSHIFT
		default:
			return fmt.Errorf("Invalid Operation [%s]", matches[2])
		}

		inst.input1 = circuit.FindWire(matches[1])
		inst.input2 = circuit.FindWire(matches[3])
		inst.output = circuit.FindWire(matches[4])
	} else if notPtrn.MatchString(input) {
		// NOT dq -> dr
		matches := notPtrn.FindStringSubmatch(input)
		inst.op = NOT
		inst.input1 = circuit.FindWire(matches[1])
		inst.output = circuit.FindWire(matches[2])
	} else if assignPtrn.MatchString(input) {
		// 44430 -> b
		// gx -> b
		matches := assignPtrn.FindStringSubmatch(input)

		inst.op = ASSIGN
		inst.input1 = circuit.FindWire(matches[1])
		inst.output = circuit.FindWire(matches[2])
	} else {
		return fmt.Errorf("Invalid instruction [%s]\n", input)
	}

	inst.output.Inst = &inst

	return nil
}

func (circuit Circuit) String() string {
	var output string
	for _, wire := range circuit {
		output += fmt.Sprintln(wire.Inst.String())
	}

	return output
}
