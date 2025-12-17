package day10

import (
	// "caroon.org/aoc25/shared/grid"
	"fmt"
	// "github.com/ernestosuarez/itertools"
	// "math"
	"strconv"
	// "bytes"
	"strings"
)

func solvePart1(machines []*FactoryMachine) int {
	// Fewest number of button presses to turn on the indicated lights
	// for each machine
	var totalPresses int = 0

	machine := machines[0]
	// fmt.Println(machine.ButtonCount())
	// fmt.Printf("Before => %v\n", machine)
	// machine.PushButtons([]int{0, 2})
	// fmt.Printf("After => %v\n", machine)

	fmt.Println("-> Ready1: ", machine.LightsReady())
	machine.PushButtons([]int{4, 5})
	fmt.Println("-> Ready2: ", machine.LightsReady())
	// for _, machine := range machines {
	// 	// 	btn_nums = list(range(machine.button_count))
	// 	var fewestPresses int = 0
	// 	// 	for presses in range(1, len(btn_nums) + 1):
	// 	// 		combos = itertools.combinations(btn_nums, presses)
	// 	var found bool = false
	// 	// 		for btn_list in combos:
	// 	for _, btnList := range combos {
	// 		// 			machine.push_buttons(*btn_list)
	// 		// 			if machine.lights_ready():
	// 		// 				fewest_presses = presses
	// 		// 				found = True
	// 		// 				break
	// 		// 			machine.reset_lights()

	// 	}

	// 	if found == true {
	// 		break
	// 	}

	// 	totalPresses += fewestPresses
	// }

	return totalPresses
}

func solvePart2(manual []*FactoryMachine) int {
	return 0
}

func processInput(data []string) []*FactoryMachine {
	// [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
	var machines []*FactoryMachine

	for _, line := range data {
		// Lights Diagram
		lightData, otherData, _ := strings.Cut(line, "]")
		// lightData = [.##.
		lightDia := []byte(lightData[1:])

		// Button Wiring
		var buttons [][]int
		buttonData, joltageData, _ := strings.Cut(otherData, "{")
		buttonList := strings.Split(strings.TrimSpace(buttonData), " ")
		// buttonList = "(3)" | "(1,3)" | "(2)" | "(2,3)" | "(0,2)" | "(0,1)"
		for _, btnGrp := range buttonList {
			endIdx := len(btnGrp) - 1
			var buttonSet []int
			for _, bNum := range strings.Split(btnGrp[1:endIdx], ",") {
				bVal, _ := strconv.Atoi(string(bNum))
				buttonSet = append(buttonSet, bVal)
			}
			buttons = append(buttons, buttonSet)
		}

		// Joltage Values
		// joltageData = 7,5,12,7,2}
		var joltages []int
		endIdx := len(joltageData) - 1
		for _, jNum := range strings.Split(joltageData[0:endIdx], ",") {
			jVal, _ := strconv.Atoi(jNum)
			joltages = append(joltages, jVal)
		}

		machines = append(machines, NewFactoryMachine(lightDia, buttons, joltages))
	}

	return machines
}

func Exec(part string, data []string) (int, error) {
	var result int = 0
	var err error = nil

	machines := processInput(data)

	if part == "PART1" {
		result = solvePart1(machines)
	} else if part == "PART2" {
		result = solvePart2(machines)
	} else {
		err = fmt.Errorf("Day10 - Unknown Part: [%s]\n", part)
	}

	return result, err
}
