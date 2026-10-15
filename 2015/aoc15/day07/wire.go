package day07

import (
	"fmt"
	"regexp"
	"strconv"
)

type Wire struct {
	id       string
	Signal   uint16
	resolved bool
	Inst     *Instruction
}

func NewWire(id string) *Wire {
	var wire Wire

	isConstant, _ := regexp.MatchString(`^\d+$`, id)
	if isConstant {
		value, _ := strconv.Atoi(id)
		wire = Wire{id: "__CONSTANT__", Signal: uint16(value)}
	} else {
		wire = Wire{id: id}
	}

	// fmt.Printf("NewWire: Created '%s'\n", id)

	return &wire
}

func (w *Wire) AND(input1 *Wire, input2 *Wire) {
	w.Signal = input1.Signal & input2.Signal
}

func (w *Wire) OR(input1 *Wire, input2 *Wire) {
	w.Signal = input1.Signal | input2.Signal
}

func (w *Wire) NOT(input1 *Wire) {
	w.Signal = ^input1.Signal
}

func (w *Wire) LSHIFT(input1 *Wire, input2 *Wire) {
	w.Signal = input1.Signal << input2.Signal
}

func (w *Wire) RSHIFT(input1 *Wire, input2 *Wire) {
	w.Signal = input1.Signal >> input2.Signal
}

func (w *Wire) ASSIGN(input1 *Wire) {
	w.Signal = input1.Signal
}

func (w *Wire) Id() string {
	var id string

	if w.id == "__CONSTANT__" {
		id = fmt.Sprintf("<%d>", w.Signal)
	} else {
		return w.id
	}

	return id
}

func (w *Wire) Resolve() {
	var inst *Instruction = w.Inst

	if inst != nil && w.resolved == false {
		if inst.input1 != nil {
			inst.input1.Resolve()
		}

		if inst.input2 != nil {
			inst.input2.Resolve()
		}

		_ = inst.Exec()

		// Mark the wire as having it's signal resolved. No need to
		// resolve it / calculate the value again.
		w.resolved = true
	}
}

func (w *Wire) Reset() {
	w.resolved = false
}

func (w *Wire) String() string {
	var output string
	output = fmt.Sprintf("%s -> %d\n%s\n", w.id, w.Signal, w.Inst)

	return output
}
