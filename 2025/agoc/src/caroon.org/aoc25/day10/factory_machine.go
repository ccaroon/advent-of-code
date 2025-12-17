package day10

import (
	"bytes"
)

type FactoryMachine struct {
	lightsDia []byte
	lights    []byte
	buttons   [][]int
	joltages  []int
}

const LightOff byte = '.'
const LightOn byte = '#'

func NewFactoryMachine(lightsDia []byte, buttons [][]int, joltages []int) *FactoryMachine {
	var lightCount int = len(lightsDia)
	var machine FactoryMachine = FactoryMachine{
		lightsDia,
		make([]byte, lightCount),
		buttons,
		joltages,
	}

	machine.ResetLights()

	return &machine
}

func (fm *FactoryMachine) ButtonCount() int {
	return len(fm.buttons)
}

func (fm *FactoryMachine) ResetLights() {
	for idx := 0; idx < len(fm.lights); idx++ {
		fm.lights[idx] = LightOff
	}
}

func (fm *FactoryMachine) LightsReady() bool {
	return bytes.Compare(fm.lights, fm.lightsDia) == 0
}

func (fm *FactoryMachine) ToggleLight(lightNum int) {
	if fm.lights[lightNum] == LightOff {
		fm.lights[lightNum] = LightOn
	} else {
		fm.lights[lightNum] = LightOff
	}
}

func (fm *FactoryMachine) PushButtons(btns []int) {
	for _, bNum := range btns {
		for _, lNum := range fm.buttons[bNum] {
			fm.ToggleLight(lNum)
		}
	}
}
