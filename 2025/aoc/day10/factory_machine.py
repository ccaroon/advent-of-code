class FactoryMachine:
    LIGHT_OFF = "."
    LIGHT_ON = "#"

    def __init__(self, uid, lights, buttons, joltages):
        self.__uid = uid
        # The desired state of the lights
        self.__lights_dia = lights

        # The actual state of the lights
        # Initially all off
        self.reset_lights()

        self.__buttons = buttons
        self.__joltages = joltages

    def __str__(self):
        return f"{self.__uid}) [{''.join(self.__lights_dia)}] {self.__buttons} {{{self.__joltages}}}"

    @property
    def button_count(self):
        return len(self.__buttons)

    @property
    def uid(self):
        return self.__uid

    @property
    def lights(self):
        return f"{self.__lights} / {self.__lights_dia}"

    def reset_lights(self):
        self.__lights = ["."] * len(self.__lights_dia)

    def lights_needed(self):
        needed = []

        for idx, state in enumerate(self.__lights_dia):
            if state == self.LIGHT_ON:
                needed.append(idx)

        return needed

    def lights_ready(self):
        return self.__lights == self.__lights_dia

    def lights_diff(self):
        ldiff = []

        for idx, light in enumerate(self.__lights):
            if light == self.__lights_dia[idx]:
                ldiff.append(True)
            else:
                ldiff.append(False)

        return ldiff

    def __toggle_light(self, lnum):
        self.__lights[lnum] = self.LIGHT_OFF if self.__lights[lnum] == self.LIGHT_ON else self.LIGHT_ON

    def find_buttons(self, *lights):
        buttons = []

        for idx, btn in enumerate(self.__buttons):
            found = False
            for lnum in lights:
                if lnum in btn:
                    found = True
                    break

            if found:
                buttons.append(idx)

        return buttons

    def push_buttons(self, *btns):
        for bnum in btns:
            for lnum in self.__buttons[bnum]:
                self.__toggle_light(lnum)
