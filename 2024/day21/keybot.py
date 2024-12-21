class KeyBot:

    DIRECTION = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }

    def __init__(self, uid, keypad, **kwargs):
        self.__uid = uid
        self.__keypad = keypad

        start_key = kwargs.get("start_key", None)
        self.__arm_positon = self.__keypad.position(start_key)

        self.__linked_bot = None


    @property
    def uid(self):
        return self.__uid


    @property
    def keypad(self):
        return self.__keypad


    def __str__(self) -> str:
        output = ""
        if self.__linked_bot:
            output = "-> " + str(self.__linked_bot)

        key = self.__keypad.key(self.__arm_positon)
        output = f"{self.uid}[{key}] {output}"

        return output


    def link(self, other_bot):
        """
        Link this Keybot's key presses to another Keybot
        """
        self.__linked_bot = other_bot
        self.__keypad.link(other_bot.keypad)


    def move(self, arrow):
        # TODO: raise error is ever positioned over blank key space
        direction = self.DIRECTION.get(arrow)
        self.__arm_positon[0] += direction[0]
        self.__arm_positon[1] += direction[1]


    def activate(self):
        """ Press the Key under the Bot's Arm Position """
        key = self.__keypad.key(self.__arm_positon)
        self.__keypad.press(key)




#
