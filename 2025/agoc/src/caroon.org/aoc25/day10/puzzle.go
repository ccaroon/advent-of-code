package day10

import (
	"fmt"
	"github.com/ernestosuarez/itertools"
	"strconv"
	"strings"
)

func solvePart1(machines []*FactoryMachine) int {
	// Fewest number of button presses to turn on the indicated lights
	// for each machine
	var totalPresses int = 0

	for _, machine := range machines {
		// fmt.Printf("=> %v\n", machine)
		// Indexes of each button i.e. the number of buttons as a list[int]
		// Ex: if a machine has 5 buttons, the btnIds = [0,1,2,3,4]
		var btnIds []int
		for bId := range machine.ButtonCount() {
			btnIds = append(btnIds, bId)
		}

		// fmt.Printf("  -> btdIds: %v\n", btnIds)

		fewestPresses := 0
		for pressCount := 1; pressCount <= len(btnIds); pressCount++ {
			combos := itertools.CombinationsInt(btnIds, pressCount)

			found := false
			// for btn_list in combos:
			for btnCombo := range combos {
				// fmt.Printf("  -> pCnt: %d | Cmb: %v\n", pressCount, btnCombo)
				// btnCombo holds the idx of each button to be pushed
				// NOT the actual button num list
				machine.PushButtons(btnCombo)

				// Buttons pushed // check if all the appropriate lights
				// are on
				if machine.LightsReady() {
					// if so, then record the number of buttons pushed
					fewestPresses = pressCount

					// Stop pressing button. You found what you need!!!!
					found = true
					break
				}

				// Pushing the buttons turns lights on and off
				// We didn't find the correct buttons yet, so
				// reset the light to their initial state.
				machine.ResetLights()
			}

			if found {
				// fewest presses found for this machine
				// Break to start checking the next machine
				break
			}
		}

		// # Debuggin'!
		// if fewestPresses > 0 {
		// 	fmt.Printf("  -> Found with %d presses!", fewestPresses)
		// } else {
		// 	fmt.Println("  -> WARNING: Machine cannot be activated!")
		// }

		// # count the presses for th current machine before moving to next
		totalPresses += fewestPresses
	}

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
		// otherData = (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
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
