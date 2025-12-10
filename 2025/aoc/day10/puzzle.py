import itertools
import re

from aoc.lib.puzzle import Puzzle

from .factory_machine import FactoryMachine  # noqa: TID252


class Factory(Puzzle):
    """AOC-2025 // Day10 -- Factory"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__next_uid = 1
        self.__data = []
        self._read_input(self.__parse_input)

    def __parse_input(self, line):
        # lights | buttons | joltages
        # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

        # Lights
        lights = None
        match = re.search(r"\[(.*)\]", line)
        if match:
            lights = match.group(1)
            lights = list(lights)
        else:
            msg = f"Machine Description Invalid (LIGHTS) [{line}]"
            raise ValueError(msg)

        # Buttons
        buttons = []
        match = re.search(r"\](.*)\{", line)
        if match:
            btn_data = match.group(1).strip()
            for btn in btn_data.split():
                # (1,2,3,4)
                # ignore open & close paren when split on ","
                # cast to ints
                button = [int(lnum) for lnum in btn[1:-1].split(",")]

                buttons.append(tuple(button))
        else:
            msg = f"Machine Description Invalid (BUTTONS) [{line}]"
            raise ValueError(msg)

        # Joltages
        joltages = []
        match = re.search(r"\{(.*)\}", line)
        if match:
            jlt_data = match.group(1)
            joltages = [int(jnum) for jnum in jlt_data.split(",")]
        else:
            msg = f"Machine Description Invalid (JOLTAGES) [{line}]"
            raise ValueError(msg)

        self.__data.append(FactoryMachine(self.__next_uid, lights, buttons, joltages))
        self.__next_uid += 1

    def _part1(self):
        # Fewest number of button presses to turn on the indicated lights
        # for each machine
        total_presses = 0
        for machine in self.__data:
            self._debug(machine)
            self._debug(f"  -> Needed Lights: {machine.lights_needed()}")

            # Indexes of each button i.e. the number of buttons as a list[int]
            btn_nums = list(range(machine.button_count))

            self._debug(f"  -> Buttons: [{btn_nums}]")

            fewest_presses = 0
            # Try different combinations of buttons for different numbers of
            # button presses starting with just 1
            # I.e.
            # Is there just a single button that can be pushed to light the lights - try each button in turn to check
            # No?
            # Is there a combination of 2 buttons that can be pushed to light the lights - try every combination of 2 buttons to check.
            # No?
            # Is there a combination of 3 buttons ...???
            # REPEAT for the number of buttons
            for presses in range(1, len(btn_nums) + 1):
                combos = itertools.combinations(btn_nums, presses)
                self._debug(f"  -> Trying combos of [{presses}] presses...")

                found = False
                for btn_list in combos:
                    # bnt_list is the idx of each button to be pushed
                    # NOT the actual button num list
                    machine.push_buttons(*btn_list)

                    # Buttons pushed // check if all the appropriate lights
                    # are on
                    if machine.lights_ready():
                        # if so, then record the number of buttons pushed
                        self._debug(f"  -> Success @ {btn_list}")
                        fewest_presses = presses
                        # Stop pressing button. You found what you need!!!!
                        found = True
                        break
                    # Pushing the buttons turns lights on and off
                    # We didn't find the correct buttons yet, so
                    # reset the light to their initial state.
                    machine.reset_lights()

                if found:
                    # fewest presses found for this machine
                    # Break to start checking the next machine
                    break

            # Debuggin'!
            if fewest_presses > 0:
                self._debug(f"  -> Found with {fewest_presses} presses!")
            else:
                self._debug("  -> WARNING: Machine cannot be activated!")

            # count the presses for th current machine before moving to next
            total_presses += fewest_presses

        return total_presses

    def _part2(self):
        pass
