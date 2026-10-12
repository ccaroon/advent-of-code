package day07

type Wire struct {
	id     string
	Signal uint16
}

// All the Wires in the connected circuit
var circuit map[string]*Wire = make(map[string]*Wire)

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

func FindWire(id string) *Wire {
	var ok bool
	var wire *Wire

	if wire, ok = circuit[id]; !ok {
		wire = &Wire{id: id}
		circuit[id] = wire
	}

	return wire
}
